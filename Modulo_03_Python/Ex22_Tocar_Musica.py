
import pygame

# pylint: disable=no-member
pygame.init()
pygame.mixer.music.load(
    'C:/Users/klebe/Dropbox/PC/Documents/CURSOS/Python/Modulo_03_Python/Ex22.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# Wait until the song ends before exiting program