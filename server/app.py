from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)

# Retrieve all messages
@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([msg.to_dict() for msg in messages])

# Retrieve a message by ID
@app.route('/messages/<int:id>', methods=['GET'])
def get_message_by_id(id):
    message = Message.query.get_or_404(id)
    return jsonify(message.to_dict())

# Create a new message
@app.route('/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    if not data or 'content' not in data or 'sender' not in data:
        return make_response(jsonify({"error": "Missing required fields"}), 400)

    new_message = Message(content=data["content"], sender=data["sender"])
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.to_dict()), 201

# Update an existing message
@app.route('/messages/<int:id>', methods=['PUT'])
def update_message(id):
    message = Message.query.get_or_404(id)
    data = request.get_json()

    if 'content' in data:
        message.content = data['content']
    
    db.session.commit()
    return jsonify(message.to_dict())

# Delete a message
@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message = Message.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"}), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
