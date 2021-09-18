# Tourtoro
Tourtoro is a full stack web application that allows users to make a trusty trip planner, add activities and places for their adventures. Users can also get suggestions for places to visit and eat based on their selected location.



![Homepage](/static/img/gif/home.png "Homepage")

## Contents
 - [Technologies](#technologies)
 - [Features](#features)
 - [API](#api)
 - [Installation](#installation)
 - [About the Developer](#aboutthedeveloper)



### Technologies
* Python 3.7
* PostgresSQL
* Jinja
* Flask
* Ajax
* SQLAlchemy
* Javascript
* JQuery
* Bootstrap
* HTML/CSS
* Google Maps for JavaScript
* Google Geocoder

## <a name="features"></a>Features
#### Landing Page
Users  can register or login on the Jinja2 and Javascript rendered landing page. Passwords are encrypted using argon2 hashing for user security.
![alt text](/static/img/gif/homepage.gif "Toutoro landing page")

#### User Profile Page
After a user has created an account and logged in they will be redirected to their profile page.  Here the user can see all of their existing trips, plan a new trip by entering a place and dates.
![alt text](/static/img/gif/userprofile.gif "Toutoro user profile page")

#### Itinerary Pages
Users can see their itinerary with all activities broken down by day and time for a trip.  Undated activities will appear at the bottom of the itinerary.  All activities will also appear on the trip map, and clicking a marker will quickly show the user what day their activity is planned for.  This space also allows users to get suggestions for places to visit and eat based on their selected location, print their itinerary.
![alt text](/static/img/gif/trip.gif "Tourtoro itinerary page")

#### Activity insert
The activity insert page is linked to the itinerary and features an autocomplete map. Both maps are rendered using the Google Maps JavaScript API with the help of Google Places and Google Geocoder.  Users can insert for address, museums, restaurants and activities and will be offered autocomplete suggestions based on the latitude and longitude of their trip.  Once an activity is selected, the user can add a date, time and additional notes if desired before adding the item to their trip.
![alt text](/static/img/gif/activity.gif "Tourtoro activity insert page")

#### Getting suggestion
If users don't know what to do, where to go and eat around the area of their adventure. This feature is the best way to give suggestion for user to explore places to visit and eat based on their selected location by using Yelp APIs. Users can insert for city, zip-code, and term they would like to search, it will give mostly 10 suggestion with bussiness name, ratings, address and photo base on highly ratings.
![alt text](/static/img/gif/suggestion.gif "Tourtoro suggestion")

#### Print trip planner
If users would like to print out their suggestion or itinerary, this feature will give user that opportunity.
![alt text](/static/img/gif/print.gif "Tourtoro print itinerary")


## <a name="future"></a>The Future of Adventure Awaits
There are lots of new features planned for additional sprints:
* Archiving of past trips
* Functionality to edit or delete activities and notes from itineraries
* Adding user photo profile.
* Integrating a flight search and hotel API
The goal is to make this a one stop travel planning app that includes everything a user needs to plan the perfect trip all in one place.

### <a name="api"></a> API
* [Google APIs](https://developers.google.com/maps) 
* [Yelp APIs](https://www.yelp.com/developers) 

---
### Installation
#### Prerequisites
To run Tourtoro, you must have installed:
 - [PostgreSQL](https://www.postgresql.org/)
 - [Python 3.7](https://www.python.org/downloads/)
 - [API key for Google's APIs](https://developers.google.com/maps)
 - [API key for Yelp APIs](https://www.yelp.com/developers)


 #### Run Tourtoro on your local computer

 Clone or fork repository:
 ```
 $ git clone https://github.com/bellahoang9/tourtoro
 ```

Create and activate a virtual environment within your Tourtoro directory:
```
$ virtualenv env
$ source env/bin/activate
```
Install dependencies:
```
$ pip3 install -r requirements.txt
```

Get an API key from Google's APIs and Yelp's APIs, add your API key to a secrets.sh file.
Sign up to use the [Yelp API](https://www.yelp.com/developers)
Sign up to use the [Google Maps Javascript, Google Places and Geocoder APIs](https://cloud.google.com/maps-platform/)
You will need to register for 2 API keys.  One will be used in the JavaScript front-end and one for the Python back-end.  Your front-end API key will need to be locked to your personal IP address and included in your script tags, the back-end key will need to be saved as below:
Save your API keys in a file called <kbd>secrets.sh</kbd> using this format:
```
export YELP_API_KEY='YOUR_KEY_HERE'
export GG_API_KEY='YOUR_KEY_HERE'
```
Source your keys from your secrets.sh file into your virtual environment:
```

Run the secrets.sh file 
```
$ source secrets.sh
```

Run model.py to create all SQL database models
```
$ python3 model.py
```

Create database 'travel':
```
$ createdb travel
```

To run the app from the command line:
```
$ python3 server.py
```

You can now navigate to 'localhost:5000/' to access Tourtoro.

---

### <a name="aboutthedeveloper"></a> About the Developer
Tourtoro developer Thalia Lietz is a new grad software engineer. This is her first full-stack project and was only possible with the support of her teachers at Hackbright Academy. She can be found on [LinkedIn](https://www.linkedin.com/in/thuhoang-bella/) and on [Github](https://github.com/bellahoang9).