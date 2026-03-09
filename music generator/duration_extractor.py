import pygame
import time

def play_music(environment_sounds, duration):

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("generated_music.mid")
    pygame.mixer.music.play()

    channels = []

    for s in environment_sounds:

        sound = pygame.mixer.Sound(s)

        channel = sound.play(-1)

        channels.append(channel)

    print(f"Playing music for {duration} seconds...")

    time.sleep(duration)

    pygame.mixer.music.stop()

    for ch in channels:
        ch.stop()