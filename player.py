import pygame
from settings import import_folder


pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("heroi/personagem0.png")
        self.pos = pygame.math.Vector2(x, y)
        self.rect = self.image.get_rect(center = (self.pos.x, self.pos.y))

    
