import pygame, sys
from fonts import *


largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))

def playScreen():
    while True:
        posMouse = pygame.mouse.get_pos()

        janela.fill("black")

        textoTela = fontPlayScreen(45).render("Welcome to Duck's Adventure", True, "White")

        posTextoTela = textoTela.get_rect(center=(640,260))

        janela.blit(textoTela,posTextoTela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            '''if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(posMouse):
                    playScreen()'''

        pygame.display.update()