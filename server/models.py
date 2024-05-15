from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# BUILD OUT THE FOLLOWING MODELS

# YOU WILL NEED ADDITIONAL COLUMNS FOR THE FOREIGN KEYS


class VideoGame(db.Model):
    
    __tablename__ = 'video_games_table'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)

    reviews = db.relationship('Review', back_populates='videogame')

    publications = association_proxy('reviews', 'publication')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "publications": [ pub.to_dict() for pub in self.publications ]
        }


class Publication(db.Model):

    __tablename__ = 'publications_table'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)

    reviews = db.relationship('Review', back_populates='publication')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Review(db.Model):

    __tablename__ = 'reviews_table'

    id = db.Column(db.Integer, primary_key=True)

    rating = db.Column(db.Integer, default=0)

    videogame_id = db.Column(db.Integer, db.ForeignKey( 'video_games_table.id' ))
    publication_id = db.Column(db.Integer, db.ForeignKey( 'publications_table.id' ))

    publication = db.relationship('Publication', back_populates='reviews')
    videogame = db.relationship('VideoGame', back_populates='reviews')

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "videogame_id": self.videogame_id,
            "publication_id": self.publication_id,
            "videogame": self.videogame.to_dict(),
            "publication": self.publication.to_dict()
        }
    
    def __repr__(self):
        return f"Review(id={self.id}, rating={self.rating}, publication={self.publication.name})"


# Publication ---< Review >--- VideoGame

                # publication_id  
                # videogame_id