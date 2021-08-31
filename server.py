# """Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify, make_response


from jinja2 import StrictUndefined
from model import connect_to_db
import crud
import helper
import os
import json
from passlib.hash import argon2
from datetime import date, time

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined
GG_API_KEY = os.environ['GG_API_KEY']
YELP_API_KEY = os.environ['YELP_API_KEY']

@app.route('/')
def homepage():
    """Show home page"""
    return render_template('homepage.html')


@app.route('/login', methods = ['POST'])
def user_login():
    """ User log in"""

    email = request.form.get('email')
    input_password = request.form.get('password')
    user = helper.get_user_by_email(email)
    if user == None:
        flash("This email has not register")
        return redirect('/')
    else:
        if argon2.verify(input_password, user.password):
            session['EMAIL'] = user.email
            session['NAME'] = user.fname 
            session['ID'] = user.user_id
            return redirect (f'users/profile/{user.fname}')  
        else:
            flash('Incorrect Password. Please try again.')
            return redirect ('/') 

@app.route('/logout')
def user_logout():
    """Log out user"""

    session.clear()
    return redirect('/')

@app.route('/users/create-user.json', methods=['POST'])
def new_user():
    """Create new user"""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = helper.get_user_by_email(email)

    if user != None:
        return jsonify('This email is already exists.')
    else:
        crud.create_user(fname, lname, email, password)
        return jsonify('Your account has been created. Please log in.')

@app.route('/users/profile/<fname>')
def show_user_profile(fname):
    """Show logged in user profile"""

    return render_template('user_profile.html', fname=fname)

@app.route('/users/profile/api')
def get_user_infomation():

    user = helper.get_user_by_email(session['EMAIL'])
    user_iti = helper.get_trip_by_user(user)
    return jsonify({'fname': user.fname, 'lname': user.lname, 'email': user.email,
                    'trips': user_iti})

@app.route('/users/trips/new-trip.json', methods = ['POST'])
def new_itinerary():
    """Creates a new itinerary for a user and returns data as JSON."""
    
    user = helper.get_user_by_email(session['EMAIL'])
    trip_name = request.form['trip_name']
    city = request.form['city']
    state = request.form['state']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    num_days = crud.calculate_itinerary_days(start_date, end_date)
    lat, lng = crud.get_latitude_longitude_for_itinerary(city)
    new_itinerary = crud.create_itinerary(trip_name, city, state, start_date, end_date, lat, lng)
    crud.create_planner(user.user_id, new_itinerary.trip_id)
    print(trip_name)
    
    return jsonify({'trip_id': new_itinerary.trip_id, 'trip_name': new_itinerary.trip_name, 'city': new_itinerary.city})


@app.route('/users/trips/add-trip.json', methods=['POST'])
def link_itinerary():
    """Links a user to an existing itienrary and returns data as JSON"""

    user = helper.get_user_by_email(session['EMAIL'])
    trip_id = request.form.get('id')
    trip = helper.get_trip_by_id(trip_id)
    crud.create_planner(user.user_id, trip_id)
    return jsonify({'trip_id': trip_id, 'trip_name': trips.trip_name})


@app.route('/users/trips/<trip_id>')
def show_itinerary(trip_id):
    """Show individual trip itinerary"""

    session['TRIP'] = trip_id
    return render_template('my_trip.html')


@app.route('/users/trips/api')
def return_json_for_maps():
    """ Reutrn json to JS for my_trip google map."""

    json_data = helper.json_intinerary_activities(session['TRIP'])
    return json.dumps(json_data, cls=helper.DateTimeEncoder)


@app.route('/users/itinerary/api')
def return_json_for_itinerary():
    """ Return json to Js for my_trip page"""

    json_data = helper.jsonify_all_itinerary_data(session['TRIP'], session['ID'])
    return json.dumps(json_data, cls=helper.DateTimeEncoder)


@app.route('/users/trips/activities')
def activity_search():
    """Return itinerary info for activity search page"""

    trip_name = helper.get_trip_name(session['TRIP'])
    return render_template('activitysearch.html', trip_name=trip_name)


@app.route('/users/trips/activities.json')
def return_map_render_json():
    """Return itinerary info for activity search map"""

    json_data = helper.itinerary_by_id(session['TRIP'])
    return json.dumps(json_data, cls=helper.DateTimeEncoder)


@app.route('/users/trips/new-activity/api', methods=['POST'])
def add_new_activity():
    """Add new activity to DB"""

    trip_id = session['TRIP']
    trip_name = helper.get_trip_name(trip_id)
    email = session['EMAIL']
    activ_name = request.form.get('name')
    address = request.form.get('address')
    lat_lng = request.form.get('latlng')
    lat_lng = lat_lng.strip('()').split(', ')
    lat = float(lat_lng[0])
    lng = float(lat_lng[1])

    # lat_lng = crud.get_latitude_longitude_for_itinerary(address)
    # lat = lat_lng[0]
    # lng = lat_lng[1]
    print('\n\n\n\n\n\n\n')
    print(lat_lng)
    print(address)
    print(activ_name)
    print('\n\n\n\n\n\n\n')

    activ_date = request.form.get('activity-date')
    if activ_date == '':
        activ_date = None
    
    activ_time = request.form.get('activity-time')
    if activ_time == '':
        activ_time = None

    activ_note = request.form.get('activity-note')
    if activ_note == '':
        activ_note = None

    crud.create_activity(trip_id, activ_name, address,lat, lng, activ_date,  activ_time, activ_note)
    flash('This activity has been added to your trip')
    return redirect (f'/users/trips/{trip_id}')


# YELP API recommend --------------

@app.route('/users/trips/explore.json', methods=['POST'])
def show_recommend():
    """Creates a new itinerary for a user and returns data as JSON."""
    
    city = request.form['city']
    zip_code = request.form['zipcode']
    term = request.form['term']
    
    recommends = helper.getting_recommendation(city, zip_code, term)

    #jsonify{city:city,}
    return jsonify({'recommends':recommends})

    # return json.dumps(data)

@app.route('/users/trips/explore')
def recommend_search():
    return render_template('activitysearch.html')



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    # import sys
    app.run(host="0.0.0.0", debug=True)


