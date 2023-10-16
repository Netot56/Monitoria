import pygame
from settings import *
from sys import exit
from pygame.locals import *

from time import sleep

def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Inicio Pygame")

def menu():

    pygame.init()

    #DEFININDO A FONTE USADA PARA EXIBIR AS OPÇÕES
    fonteOpcao = pygame.font.SysFont(fonte, 25, True)


    #LISTA DE OPÇÕES DO MENU E A AUTORIA DA CRIAÇÃO DO JOGO
    opc1 = fonteOpcao.render("Inciar", True, "black")
    

    while True:
        relogio.tick(fps)
 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
        tela.fill()
        
        pygame.draw.rect(tela,"white", (410, 140, 300, 80))
        
        tela.blit(opc1, (470, 160))
        
        tecla = pygame.key.get_pressed()
        
      
        

        

        pygame.display.flip()
