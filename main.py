# --------------------------------- EL PYTHONCITO  XD 🐍🐍🐍🐍
import pygame
import time
import random
from song import times, subtitles, music_emojis

# Initialize pygame
pygame.mixer.init()
pygame.mixer.music.load("./Three_Little_Birds.mp3")
pygame.mixer.music.play()

print("\n" * 500)
print("EL PYTHONCITO XD 🐍🐍🐍🐍!!!!")
start_time = time.time()
for i in range(len(subtitles)):
    while time.time() - start_time < times[i]:
        time.sleep(0.1)
    print(f"{random.choice(music_emojis)}", end="")
    # Typewritter effect
    for letter in subtitles[i]:
        print(f"{letter}", end="", flush=True)
        time.sleep(0.05)
    print()
