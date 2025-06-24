from server.models import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Float)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    guest = db.relationship('Guest', backref='appearances')
    episode = db.relationship('Episode', backref='appearances')

    def __repr__(self):
        return f"<Appearance Guest: {self.guest_id} Episode: {self.episode_id} Rating: {self.rating}>"
