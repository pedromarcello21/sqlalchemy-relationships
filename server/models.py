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