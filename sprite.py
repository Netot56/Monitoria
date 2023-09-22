import pygame
from pygame.locals import *

from sys import exit

from pygame.sprite import _Group

pygame.init()

largura, altura = 640, 480

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('personagem')

preto = (0,0,0)

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)



while True:
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()