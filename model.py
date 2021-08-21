from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    """Data model for user"""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    password = db.Column(db.String)



    def __repr__(self):
        return f'<User user_id={self.user_id} fname={self.fname} email={self.email}>'

class Itinerary(db.Model):
    """Itinerary - data of spefific trip created by user"""
    __tablename__ = 'trips'

    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_name = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    #secondary = planner
    users = db.relationship('User', secondary='planner', backref='trips')
    
    def __repr__(self):
        return f'<Itinerary trip_id={self.trip_id} trip_name={self.trip_name}>'


class Planner(db.Model):  
    """Association table for User and Itinerary"""
    __tablename__ = 'planner'

    planner_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    
    trip_id = db.Column(db.Integer, 
                        db.ForeignKey('trips.trip_id'),
                        nullable=False)

    # user = db.relationship('User', backref='planner')
    # trip = db.relationship('Itinerary', backref='planner')

    def __repr__(self):
        return f'<User Itinerary Association: user_id: {self.user_id} trip_id: {self.trip_id}>'

class Activity(db.Model):
    """ Activities added to itineraries by users."""
    __tablename__ = 'activities'

    activ_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    trip_id = db.Column(db.Integer,
                    db.ForeignKey('trips.trip_id'))
    activ_name = db.Column(db.String)
    address = db.Column(db.String)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    activ_date = db.Column(db.Date, nullable=True)
    activ_time = db.Column(db.Time, nullable=True)
    activ_note = db.Column(db.Text, nullable=True)

    trip = db.relationship('Itinerary', backref='activities')

    def __repr__(self):
        return f'<Activities: activ_id: {self.activ_id} activ_name: {self.activ_name}>'


def example_data():
    """Data for test"""

    User.query.delete()
    Itinerary.query.delete()
    Planner.query.delete()
    Activity.query.delete()

    user1 = User(fname='bella', lname='hoang', email='funny@bunny', password='shhh')
    user2 = User(fname='sisi', lname='hughey', email='hi@best', password='shhh')
    seattle = Itinerary(trip_name='Seattle', city='seattle',state='WA', start_date='2021-10-05', end_date='2021-10-10', lat=51.528308, lng=-0.3817846)
    sanjose = Itinerary(trip_name='San Jose', city='san jose',state='CA', start_date='2021-09-04', end_date='2021-09-09')
    planner = Planner(user_1=2, trip_id=2)
    museum = Activity(trip_id=2,activ_name='the lab', address='san francisco',lat=51.5094269, lng=-0.1303103, activ_date='2021-09-05', activ_time='12:00', activ_note='awesome')


    db.session.add_all([user1, user2, seattle, sanjose, museum])
    db.session.commit()


def connect_to_db(flask_app, db_uri="postgresql:///travel", echo=True):
    """Connect the database to our Flask app."""

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = flask_app
    db.init_app(flask_app)


if __name__ == '__main__':
    from server import app


    connect_to_db(app)
    print('Connected to db!')
