from . import db
from sqlalchemy.orm import relationship

class Episode (db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    number = db.Column(db.Integer, nullable = False)

    appearance = db.relationship('Appearance', backref = 'episode', cascade = 'all, delete-orphan')

    def __repr__(self):
         return f"<Episode id={self.id} number={self.number} date={self.date}>"