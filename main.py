import pygame

from settings import *
import sys

class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Inicio Pygame")
        self.clock = pygame.time.Clock()

    def run(self):

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            pygame.display.update()
            self.clock.tick(fps)

if __name__ == "__main__":
    game = Game()
    game.run()

            

    
    
