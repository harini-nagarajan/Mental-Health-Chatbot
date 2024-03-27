from flask import Flask, render_template, request, jsonify, send_file
import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import difflib

app = Flask(__name__, static_folder='static')

# Load data from JSON file
with open("data/intents1.json", encoding="utf-8") as file:
    data = json.load(file)['intents']

# Load tokenizer
patterns = []
responses = []
for intent in data:
    patterns.extend(intent['patterns'])
    responses.extend(intent['responses'])

# Tokenize the text data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(patterns)
total_words = len(tokenizer.word_index) + 1

# Create input sequences and labels
input_sequences = []
for line in patterns:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_length = max(len(seq) for seq in input_sequences)

# Load trained model
model = load_model("model/mental_health_chatbot_model.h5")

def generate_response(user_input, model, tokenizer, max_sequence_length, data, temperature=0.1):
    user_input = user_input.lower()
    user_input = ' '.join(user_input.split())

    matching_responses = []

    for intent in data:
        cleaned_patterns = [' '.join(pattern.lower().split()) for pattern in intent['patterns']]
        similarities = [difflib.SequenceMatcher(None, user_input, pattern).ratio() for pattern in cleaned_patterns]
        max_similarity = max(similarities)

        if max_similarity > 0.7:
            matching_responses.append(random.choice(intent['responses']))

    if matching_responses:
        return random.choice(matching_responses)

    seed_text = user_input
    generated_response = seed_text

    max_attempts = 1000  # Set a maximum number of attempts
    attempt = 0

    while attempt < max_attempts:
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_length-1, padding='pre')
        predicted_probs = model.predict(token_list, verbose=0)[0]

        scaled_probs = np.log(predicted_probs) / temperature
        soft_probs = np.exp(scaled_probs) / np.sum(np.exp(scaled_probs))

        predicted_index = np.random.choice(len(predicted_probs), p=soft_probs)

        predicted_response = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted_index:
                predicted_response = word
                break

        seed_text += " " + predicted_response
        generated_response += " " + predicted_response

        if predicted_response.endswith(('.', '!', '?')):
            return generated_response

        attempt += 1

    return "Can you please elaborate more?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = generate_response(user_input, model, tokenizer, max_sequence_length, data, temperature=0.1)
    return jsonify({'response': response})

@app.route('/play_meditation_audio', methods=['GET'])
def play_meditation_audio():
    # Provide the path to your meditation audio file
    audio_file_path = "static/audio/meditation_audio.mp3"
    return send_file(audio_file_path, mimetype='audio/mpeg')

@app.route('/get_image/<image_name>', methods=['GET'])
def get_image(image_name):
    # Provide the path to your images directory
    image_path = os.path.join(app.root_path, 'static', 'images', image_name)
    return send_file(image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
