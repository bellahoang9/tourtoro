from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Data model for user"""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = dc.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} fname={self.fname} email={self.email}>'


class Itinerary(db.Model):
    """Itinerary - data of spefific trip created by user"""
    __tablename__ = 'trips'

    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_name = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    num_days = db.Column(db.Integer)

    # user_id = db.Column(db.Integer,
    #                     db.ForeignKey('users.user_id'),
    #                     nullable=False)
    # user = db.relationship('User', backref='trips')
    def __repr__(self):
        return f'<Itinerary trip_id={self.trip_id} trip_name={self.trip_name}>'


class Planner(db.Model):
    """Trip planner of specific trip created by user"""
    __tablename__ = 'planner'

    planner_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    trip_id = db.Column(db.Integer, 
                        db.ForeignKey('trips.trip_id'),
                        nullable=False)
    user = db.relationship('User', backref='planner')
    trip = db.relationship('Itinerary', backref='planner')

    def __repr__(self):
        return f'<Planner planner_id={self.planner_id}'



def connect_to_db(flash_app, db_uri="postgresql:///travvel", echo=True):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = flask_app
    db.init_app(flask_app)


if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')
