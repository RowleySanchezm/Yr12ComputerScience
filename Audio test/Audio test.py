import pygame

playlist = []
playlist.append("bensound-epic.mp3")
pygame.mixer.init()
pygame.mixer.music.load(playlist.pop())
pygame.mixer.music.play(-1)
