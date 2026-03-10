from flask import Flask, request, jsonify, send_from_directory
from emotion_detector import detect_emotion
from duration_extractor import extract_duration
from environment_sound import get_environment_sounds
from music_generator import generate_music
from player import play_music

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    scene = data["scene"]

    emotion = detect_emotion(scene)
    duration = extract_duration(scene)
    sounds = get_environment_sounds(scene)

    generate_music(emotion)
    play_music(sounds, duration)

    return jsonify({"status": "Music Generated"})

if __name__ == '__main__':
    app.run(debug=True)