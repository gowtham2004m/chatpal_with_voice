from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import json
import random
app = Flask(__name__)
socketio = SocketIO(app)

# Load responses from JSON file
with open('responses.json', 'r', encoding='utf-8') as file:
    responses = json.load(file)

@app.route('/')
def chat_interface():
    return render_template('chatbot.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['message']
    response = get_response(user_input)
    return jsonify({"response": response})

@socketio.on('user_message')
def handle_user_message(data):
    user_input = data['message']
    response = get_response(user_input)
    socketio.emit('bot_response', {'response': response})

def get_response(text):
    text = text.lower()
    matching_responses = []

    for entry in responses['responses']:
        user_input = entry.get('user', '').lower()
        bot_responses = entry.get('bot', [])

        for keyword in user_input.split():
            if keyword in text:
                matching_responses.extend(bot_responses)

    if matching_responses:
        return random.choice(matching_responses)

    return "I'm here to chat. How can I assist you?"

if __name__ == '__main__':
    socketio.run(app, debug=True)
