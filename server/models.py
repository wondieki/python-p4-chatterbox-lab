from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime  # ✅ Import datetime

db = SQLAlchemy()

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    username = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # ✅ Ensure created_at exists
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Message by {self.username}: {self.body[:10]}...>'