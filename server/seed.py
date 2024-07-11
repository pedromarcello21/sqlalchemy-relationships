from config import app, db
from models import Doctor, Patient, Appointment, VideoGame, Publication, Review

if __name__ == '__main__':
    with app.app_context():

        print("Starting seed...")

        print("Clearing old data...")
        
        Doctor.query.delete()
        Patient.query.delete()
        Appointment.query.delete()

        Review.query.delete()
        VideoGame.query.delete()
        Publication.query.delete()

        db.session.commit()

        print("Adding Doctors...")

        d1 = Doctor(name="Doom")
        d2 = Doctor(name="Doolittle")
        d3 = Doctor(name="Mario")

        db.session.add_all([d1, d2, d3])
        db.session.commit()

        print("Adding Patients...")

        p1 = Patient(name="Sakib")
        p2 = Patient(name="Chett")
        p3 = Patient(name="Ben")
        p4 = Patient(name="Kash")
        p5 = Patient(name="Praveen")
        p6 = Patient(name="Ricardo")

        db.session.add_all([p1, p2, p3, p4, p5, p6])
        db.session.commit()

        print("Adding Appointments...")

        print("----------THE SEED FILE IS INCOMPLETE ADD APPOINTMENTS TO SEED----------")

        # print("Adding VideoGames...")

        # v1 = VideoGame(title="Tetris")
        # v2 = VideoGame(title="Joust")
        # v3 = VideoGame(title="Galaga")

        # db.session.add_all([v1, v2, v3])
        # db.session.commit()

        # print("Adding Publications...")

        # pb1 = Publication(name="IGN")
        # pb2 = Publication(name="Polygon")
        # pb3 = Publication(name="Gamespot")

        # db.session.add_all([pb1, pb2, pb3])
        # db.session.commit()

        # print("Adding Reviews...")

        # print("----------THE SEED FILE IS INCOMPLETE ADD REVIEWS TO SEED----------")

        print("Seeding complete...")