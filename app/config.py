import datetime
import secrets
import string

from .schemas import Profile

ALPHABET = string.ascii_letters + string.digits + "-_"

data = Profile(
    first_name="Hasan Sezer",
    last_name="Taşan",
    username="hasansezertasan",
    password="".join(secrets.choice(ALPHABET) for i in range(20)),
    email="hasansezertasan@gmail.com",
    phone_number="1234567890",
    profession="Software Developer",
    date_of_birth=datetime.date(1999, 6, 19),
    city="Ankara",
    address="Ankara, Turkey",
    biography="I am a software developer. I am interested in web development, and web scraping.",
    interests=["Web Development", "Web Scraping"],
    profile_picture="https://avatars.githubusercontent.com/u/13135006?v=4",
    website="http://www.hasansezertasan.com",
)

API_CONFIG = {
    "title": "Random Profile",
    "description": "Random profile generator for designers. Name, surname, biography, username...",
    "version": "0.0.1",
    "contact": {
        "name": "Hasan Sezer Taşan",
        "url": "http://www.hasansezertasan.com",
        "email": "hasansezertasan@gmail.com",
    },
}
