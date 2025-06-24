from server.app import create_app
from server.models import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

app = create_app()

with app.app_context():
    print("Resetting database...")
    db.drop_all()
    db.create_all()

    print("Seeding data...")

    user = User(username="admin")
    user.set_password("adminpass")

    guest = Guest(name="Trevor Noah")
    episode = Episode(date="2025-06-25", number=1)  

    appearance = Appearance(guest=guest, episode=episode, rating=9.5)

    db.session.add_all([user, guest, episode, appearance])
    db.session.commit()

    print(" Done seeding!")
