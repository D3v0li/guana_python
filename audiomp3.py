'''PROGRAMA QUE ABRE E REPRODUZ O AUDIO DE UM ARQUIVO MP3'''

import pygame

pygame.init()
pygame.mixer.music.load('flamengo.mp3')  
pygame.mixer.music.play()

input("Pressione Enter para parar...")  
