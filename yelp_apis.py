import os
import requests
from pprint import pprint

YELP_API_KEY = os.environ['YELP_API_KEY']
# YELP_API_KEY = 'YELP_API_KEY'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
headers = {
         'Authorization': 'Bearer %s' %YELP_API_KEY
     }
# #categories:
# # -fun :escapegames,gokarts,hiking,parks,cinema,festivals,museums,shoppingcenters
# #hotelstravel: carrental, hotels,motorcycle_rental, rvrental)
# #transport
# #tours
# #localflavor: yelpevents
# #nightlife: 
# #restaurants,coffee,desserts,bubbletea,sushi,, 
# PARAMETERS = {'limit':10, 'location':'San Jose, CA', 'zip_code':95121,'attributes':'hot and new', 'term':'coffee'}
#sort_by: rating
PARAMETERS = {'limit':10, 'location':'San Jose, CA','zip_code': 95121, 'term':'restaurant','sort_by': 'review_count'}
res = requests.get(url=ENDPOINT, params=PARAMETERS, headers=headers)

data = res.json()
# print(data)
for business in data['businesses']:
    print(business['name'], business['rating'], business['location']['display_address'])



