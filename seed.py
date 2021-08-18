import os, json, crud, server, model
from datetime import datetime


os.system('dropdb travel')
os.system('createdb travel')

model.connect_to_db(server.app)

model.db.create_all()

# # Create users
# create_user(fname, lname, email, password)
crud.create_user('thu', 'hoang', 'thu@hoang', 'thuhoang')
crud.create_user('jackson', 'wang', 'jack@son', 'got7')
crud.create_user('sisi', 'hughey', 'si@si', 'hughey')

# #create itineraries
# (trip_name, city, state, zip_code, start_date, end_date, lat, lng)
crud.create_itinerary('Fancy','San Francisco', 'CA','94111', '2021-12-01', '2021-12-05', 37.7576793, -122.5076413)

# #associate users with itineraries
# create_planner(user_id, trip_id)
crud.create_planner(1, 1)
crud.create_planner(2, 1)
crud.create_planner(3, 1)

# #create activities for Itinerary
# create_activity(trip_id, activ_name, address,  lat, lng, activ_date, activ_time,  activ_note)
crud.create_activity(1, 'Dinner with Friends', '5231 Wendell Lane, Sebastopol, CA, 95472', 38.348009, -122.7702767, '2021-12-4', '17:00', 'get tipsy later')
