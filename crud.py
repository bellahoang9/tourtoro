from model import (db, User, Itinerary, Planner, Activity, connect_to_db)
from datetime import datetime 
import geocoder
import os
from passlib.hash import argon2

""" CRUD operations for tourtoro"""
GG_API_KEY = os.environ['GG_API_KEY']


def create_user(fname, lname, email, password):
    """Create and return a new user."""

    user = User(fname=fname, 
        lname=lname,
        email=email, 
        # password=argon2.hash(password)
        password=password
       )

    db.session.add(user)
    db.session.commit()

    return user

def create_itinerary(trip_name, city, state, zip_code, start_date, end_date,lat, lng):
    trip = Itinerary(trip_name=trip_name, 
                    city=city,state=state,
                    zip_code=zip_code,
                    start_date=start_date, end_date=end_date, lat=lat, lng=lng)

    db.session.add(trip)
    db.session.commit()

    return trip

def create_planner(user_id, trip_id):
    planner = Planner(user_id=user_id, trip_id=trip_id)

    db.session.add(planner)
    db.session.commit()

    return planner

def create_activity(trip_id, activ_name, address,lat, lng, activ_date,  activ_time, activ_note):
    """Create and return a new activity."""
    activity = Activity(trip_id=trip_id,
                        activ_name=activ_name,
                        address=address,
                        lat=lat,
                        lng=lng,
                        activ_date=activ_date,
                        activ_time=activ_time,
                        activ_note=activ_note)
    
    db.session.add(activity)
    db.session.commit()

    return activity

def calculate_itinerary_days(start_date, end_date):
    """ Calculate num_days for itinerary data based on start and end dates."""

    date_format = "%Y-%M-%d"
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    delta = end - start

    return delta.days

def get_latitude_longitude_for_itinerary(trip_name):
    """Find latitude and longitude for new itinerary map"""

    g = geocoder.google(trip_name, key = GG_API_KEY)
    lat_lng_tuple = (g.lat, g.lng)

    return lat_lng_tuple


if __name__ == '__main__':
    from server import app
    connect_to_db(app)