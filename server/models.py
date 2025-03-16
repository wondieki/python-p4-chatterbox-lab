from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)  # Use 'content' instead of 'body'
    sender = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    serialize_rules = ("-timestamp",)  # Exclude timestamp if not needed
