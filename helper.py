from model import (db, User, Itinerary, Planner, Activity, connect_to_db)
import json
import os
from datetime import date, time, timedelta
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

""" Database query functions"""


def get_user_by_email(email):
    """ Look up for user by email """

    return User.query.filter(User.email == email).first()

def get_trip_by_user(user):
    """ Look up for intineraries by user """

    adventures = db.session.query(Planner.trip_id, Planner.trip_name).join(Itinerary).filter(Planner.user_id == user.user_id).all()
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
    itinerary = itinerary_by_id(given_id)
    activities = list_activities_by_trip(given_id)

    return {'itinerary': ititerary, 'activities': activities}

def jsonify_all_itinerary_data(given_id, user_id):
    """Return all data for an individual itinerary in jsonable format."""

    itinerary = itinerary_by_id(given_id)
    activities = list_activities_by_trip(given_id)
    start_date = itinerary.start_date
    end_date = itinerary.end_date
    dates = create_dates_list(start_date, end_date)
    friends = list_users_for_trip(given_id, user_id)
    return {'itinerary': itinerary, 
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




if __name__ == '__main__':
    from server import app
    connect_to_db(app)