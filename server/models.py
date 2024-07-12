from config import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


class Doctor(db.Model):

    __tablename__ = 'doctors_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Patient(db.Model):

    __tablename__ = 'patients_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Appointment(db.Model):

    __tablename__ = 'appointments_table'

    def to_dict(self):
        return {
            "id": self.id
        }

    id = db.Column(db.Integer, primary_key=True)


# PRACTICE EXERCISES #


class VideoGame(db.Model):
    
    __tablename__ = 'video_games_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)


class Publication(db.Model):

    __tablename__ = 'publications_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Review(db.Model):

    __tablename__ = 'reviews_table'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, default=0)