import pygame, sys

largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))


def getFont(size):
    return pygame.font.Font("assets/font.ttf", size)

def playScreen():
    pygame.display.set_caption("Play")

    while True:

        pos_play_mouse = pygame.mouse.get_pos()

        janela.fill("black")


    play_text = get_font(45).render("Duck's Adventure", True, "white")
