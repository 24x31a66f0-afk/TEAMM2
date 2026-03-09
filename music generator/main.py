from emotion_detector import detect_emotion
from environment_sound import detect_environment
from music_generator import generate_music
from player import play_music
from duration_extractor import extract_duration

while True:

    scene = input("\nDescribe your scene (or type 'exit'): ")

    if scene.lower() == "exit":
        print("Exiting generator...")
        break

    emotion = detect_emotion(scene)

    duration = extract_duration(scene)

    env_sounds = detect_environment(scene)

    print("Detected emotion:", emotion)
    print("Music duration:", duration, "seconds")

    generate_music(emotion, duration)

    play_music(env_sounds, duration)