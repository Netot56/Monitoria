import pygame
pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("heroi/personagem0.png")
        self.pos = pygame.math.Vector2(x, y)
        self.rect = self.image.get_rect(center = (self.pos.x, self.pos.y))

        self.direction = pygame.math.Vector2

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1