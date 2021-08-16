import os
import requests
from pprint import pprint

# API_KEY = os.environ['YELP_API_KEY']
API_KEY = 'YELP_API_KEY'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
headers = {
         'Authorization': 'Bearer %s' %API_KEY
     }

PARAMETERS = {'limit':10, 'location':'San Jose, CA', 'zip_code':95121,'attributes':'hot and new', 'term':'coffee'}

res = requests.get(url=ENDPOINT, params=PARAMETERS, headers=headers)

data = res.json()

for business in data['businesses']:
    print(business['name'], business['rating'])