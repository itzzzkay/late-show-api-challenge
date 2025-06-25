from server.app import create_app
from server.models import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

from werkzeug.security import generate_password_hash
from datetime import date

app = create_app()

with app.app_context():
    print('Deleting all tables....')
    db.drop_all()

    print('Creating all tables....')
    db.create_all()

    print('Seeding Users....') 
    user1 = User(
        username = 'mahomes',
        email = 'mahomes@example.com',
        password_hash =generate_password_hash('animerocks1')
    )
        
    print('seeding guests chill one sec.....')

    
    guest1 = Guest(name="Emma Stone", occupation="Actress")
    guest2 = Guest(name="Elon Musk", occupation="Entrepreneur")
    guest3 = Guest(name="Trevor Noah", occupation="Comedian")

    print("Seeding episodes...")
    episode1 = Episode(date=date(2024, 5, 1), number=101)
    episode2 = Episode(date=date(2024, 5, 2), number=102)
    episode3 = Episode(date=date(2024, 5, 3), number=103)

    print("Seeding appearances...")
    appearance1 = Appearance(rating=8, guest_id=1, episode_id=1)
    appearance2 = Appearance(rating=9, guest_id=2, episode_id=2)
    appearance3 = Appearance(rating=7, guest_id=3, episode_id=3)

    print("Adding and committing to database...")
    db.session.add_all([user1, guest1, guest2, guest3, episode1, episode2, episode3, appearance1, appearance2, appearance3])
    db.session.commit()

    print("Seeding complete!")