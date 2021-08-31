from model import (db, User, Itinerary, Planner, Activity, connect_to_db)
import json
import os
import requests
from pprint import pprint
from datetime import date, time, timedelta
from twilio.rest import Client

YELP_API_KEY = os.environ['YELP_API_KEY']   
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

""" Database query functions"""


def get_user_by_email(email):
    """ Look up for user by email """

    return User.query.filter(User.email == email).first()

def get_trip_by_user(user):
    """ Look up for intineraries by user """

    adventures = db.session.query(Planner.trip_id, Itinerary.trip_name, Itinerary.city).join(Itinerary).filter(Planner.user_id == user.user_id).all()
    adventures_list = []

    for adventure in adventures:
        adven_dict = {'trip_id': adventure[0], 'trip_name':adventure[1]}
        adventures_list.append(adven_dict)
    return adventures_list

def get_trip_by_id(trip_id):
    """Look up itinerary by id."""
    return Itinerary.query.get(trip_id)


def get_trip_name(trip_id):
    """ Look up trip name by id"""
    trip = get_trip_by_id(trip_id)
    return trip.trip_name


def get_activities_by_trip_id(given_id):
    """ Look up Activities associated with an itinerary"""
    return Activity.query.filter_by(trip_id = given_id).all()

""" Compile data in JSON ready format"""

def itinerary_by_id(given_id):
    """serialize itinerary to jsonify"""
    trips = get_trip_by_id(given_id)
    return {'trip_id': trips.trip_id,
            'trip_name': trips.trip_name,
            'city': trips.city,
            'state': trips.state,
            'start_date': trips.start_date,
            'end_date': trips.end_date,
            'lat': trips.lat,
            'lng': trips.lng
            }

def list_activities_by_trip(given_id):
    """serialize activities to jsonify"""

    activities = get_activities_by_trip_id(given_id)
    json_activ = []

    for a in activities:
        a_dict = {'activ_id' : a.activ_id,
                'trip_id' : a.trip_id,
                'activ_name' : a.activ_name,
                'address' : a.address,
                'lat': a.lat,
                'lng': a.lng, 
                'activ_date' : a.activ_date,
                'activ_time': a.activ_time, 
                'activ_note' : a.activ_note
                }

        json_activ.append(a_dict)
    return json_activ

def list_users_for_trip(given_id, user_id):
    """Return a list of all users associated with an itinerary except
    the logged in user"""

    return db.session.query(User.fname).join(Planner).filter(Planner.trip_id == given_id, User.user_id != user_id).all()

def json_intinerary_activities(given_id):
    """ return itinerary and associated activities."""
    trips = itinerary_by_id(given_id)
    activities = list_activities_by_trip(given_id)

    return {'trips': trips, 'activities': activities}

def jsonify_all_itinerary_data(given_id, user_id):
    """Return all data for an individual itinerary in jsonable format."""

    trips = itinerary_by_id(given_id)
    activities = list_activities_by_trip(given_id)
    start_date = trips['start_date']
    end_date = trips['end_date']
    dates = create_dates_list(start_date, end_date)
    friends = list_users_for_trip(given_id, user_id)
    return {'trips': trips, 
            'activities': activities,
            'dates': dates,
            'friends': friends
            }

""" Functions to work with date data""" 
def create_dates_list(start_date, end_date):
    """ Return list of days in range of start and end date for itinerary."""

    delta = end_date - start_date
    dates = []
    for d in range(delta.days + 1):
        dates.append(start_date + timedelta(days = d))
    return dates

class DateTimeEncoder(json.JSONEncoder):
    """Makes time and date objects jsonifiable."""

    def default(self, o):
        if isinstance(o, date):
            return o.isoformat()
        if isinstance(o, time):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

            
""" YELP """ 
def getting_recommendation(city, zip_code, term):
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    headers = {
            'Authorization': 'Bearer %s' %YELP_API_KEY
        }
    
    PARAMS = {'limit':10, 'location':city,'zip_code': zip_code, 'term':term,'sort_by': 'review_count'}
    res = requests.get(url=ENDPOINT, params=PARAMS, headers=headers)
    recommends = []
    data = res.json()

    for business in data['businesses']:
        yep_name = business['name']
        yep_rating = business['rating']
        yep_location = business['location']['display_address']
        yep_address = yep_location[0] + yep_location[1]
        recommend = {'yep_name': yep_name,
                'yep_rating': yep_rating,
                'yep_address': yep_address}
        recommends.append(recommend)
        
    return recommends

# def explore_list(city, zip_code, term):
#     recommends = getting_recommendation(city, zip_code, term)
#     explore = []

#     for recommend in recommends:
#         name = recommend['yep_name']
#         rating = recommend['yep_rating']
#         address = recommend['yep_address']

#         business = f'{name} {rating} {address}'

#         explore.append(business)

#     return explore


def getting_yelp_address(decision, city, zip_code, term):
    recommends = getting_recommendation(city, zip_code, term)

    for idx in range(0, len(recommends)):
        recommend = recommends[idx]
        if idx == decision:
            return recommend['yep_address']






if __name__ == '__main__':
    from server import app
    connect_to_db(app)