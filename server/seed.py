#!/usr/bin/env python3

from random import choice as rc
from faker import Faker

from app import app
from models import db, Message

fake = Faker()

usernames = [fake.first_name() for i in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    with app.app_context():
        # Delete existing messages
        Message.query.delete()
        db.session.commit()

        messages = []

        for i in range(20):
            message = Message(
                content=fake.sentence(),  # ✅ Corrected field name
                sender=rc(usernames),      # ✅ Corrected field name
            )
            messages.append(message)

        db.session.add_all(messages)
        db.session.commit()        

if __name__ == '__main__':
    make_messages()
