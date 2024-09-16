from config import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


class Doctor(db.Model, SerializerMixin):

    __tablename__ = 'doctors_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    appointments = db.relationship('Appointment', back_populates='doctor')

    serialize_rules = ("-appointments.doctor", "patients")

    patients = association_proxy('appointments', 'patient')


class Appointment(db.Model, SerializerMixin):

    __tablename__ = 'appointments_table'

    id = db.Column( db.Integer, primary_key=True )
    doctor_id = db.Column( db.Integer, db.ForeignKey('doctors_table.id') )
    patient_id = db.Column( db.Integer, db.ForeignKey('patients_table.id') )
    datetime = db.Column( db.DateTime )

    doctor = db.relationship('Doctor', back_populates='appointments')
    patient = db.relationship('Patient', back_populates='appointments')

    serialize_rules = ("-doctor", "-patient")


class Patient(db.Model, SerializerMixin):

    __tablename__ = 'patients_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    appointments = db.relationship('Appointment', back_populates='patient')

    doctors = db.relationship('appointments', 'doctor')

    serialize_rules = ('-appointments.patient',)


# PRACTICE EXERCISES #


class VideoGame(db.Model, SerializerMixin):
    
    __tablename__ = 'video_games_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

    #way to talk to Publication and Review

    publications = db.relationship("Publication", back_populates = "video_game")

    serialize_rules = ("publications.video_game", "reviews")

    reviews = association_proxy('publications', 'video_game')



class Publication(db.Model, SerializerMixin):

    __tablename__ = 'publications_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    #way to talk to videogame and Review
    video_games = db.relationship("VideoGame", back_populates = "publication")

    # reviews = 




class Review(db.Model, SerializerMixin):

    __tablename__ = 'reviews_table'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, default=0)
    
    # need a foreign key for videogame and publication
    video_game_id = db.Column(db.Integer, db.ForeignKey('video_games_table'))
    publication_id = db.Column(db.Integer, db.ForeignKey('publications_table'))

