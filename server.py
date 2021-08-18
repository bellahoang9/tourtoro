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

# @app.route('/')
# def homepage():
#     """Show home page"""
#     return render_template('homepage.html')

# @app.route('/login', method = ['POST'])
# def user_login():
#     """ User log in"""

#     fname = request.form.get('fname')
#     lname = request.form.get('lname')
#     email = request.form.get('email')
#     pass_word = request.form.get('password')



# if __name__ == "__main__":
#     # DebugToolbarExtension(app)
#     connect_to_db(app)
#     import sys
#     app.run(host="0.0.0.0", debug=True)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)