
import pygame, sys, button, settings as const
from button import Button

pygame.init()
screen = const.tela
pygame.display.set_caption("Menu")

#CONTROLANDO AS SETAS NO MENU PRINCIPAL DO JOGO

def font(size):
    return pygame.font.Font("fonts/Triforce.ttf", size)

def play():
    playMousePos = pygame.mouse.get_pos()

    const.tela.fill("black")

    playText = font(45).render("This is the PLAY screen.", True, "White")
    playRect = playText.get_rect(center=(640, 260))
    screen.blit(playText, playRect)

    playBack = button.Button(image=None, pos=(640, 460), 
                        text_input="BACK", font=font(75), base_color="White", hovering_color="Green")

    playBack.changeColor(playMousePos)
    playBack.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playBack.checkForInput(playMousePos):
                main_menu()

    pygame.display.update()

def main_menu():
    menuText = font(100).render("Mudinho Adventure", True, "#b68f40")
    

    startButtonText = font(50).render("Inicar", True, "white")
    

    exitButtonText = font(50).render("Sair",True, "white")
    
    while True:

        menuPosMouse = pygame.mouse.get_pos()

        menuRect = menuText.get_rect(center=(640, 100))
        startButtonRect = startButtonText.get_rect(center=(470,160))
        exitButtonRect = exitButtonText.get_rect(center=(472,260))

        const.tela.blit(menuText, (400, 160))
        const.tela.blit(startButtonText, (472, 260))
        const.tela.blit(exitButtonText, (510, 360))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButtonText.checkForInput(menuPosMouse):
                    play()
                if exitButtonText.checkForInput(menuPosMouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()