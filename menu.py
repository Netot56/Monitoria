import pygame,main, sys, settings as const

pygame.init()
screen = const.tela
pygame.display.set_caption("Menu")

tela_atual = "menu"

#CONTROLANDO AS SETAS NO MENU PRINCIPAL DO JOGO
def desenhar_botao(x, y, largura, altura, cor, texto, cor_texto):
    pygame.draw.rect(screen, cor, (x, y, largura, altura))
    fonte = const.font(20)
    texto_surface = fonte.render(texto, True, cor_texto)
    texto_retangulo = texto_surface.get_rect()
    texto_retangulo.center = (x + largura / 2, y + altura / 2)
    screen.blit(texto_surface, texto_retangulo)

def exit():
    return sys.exit()

def play(): 
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

        main.Game()

    return "sair"

def main_menu():
    menuText = const.font(100).render("Mudinho Adventure", True, "#b68f40")
    menuRect = menuText.get_rect(center=(640, 100))
    
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if const.width/2 - 50 <= mouse[0] <= const.width/2 + 50 and const.height/2 - 25 <= mouse[1] <= const.height/2 + 25:
                    return "jogo"
                if const.width/2 - 50 <= mouse[0] <= const.width/2 + 50 and const.height/2 - (-50) <= mouse[1] <= const.height/2 + (-50):
                    return "sair"

        
        mouse = pygame.mouse.get_pos()

        
        screen.fill("white")
        screen.blit(menuText,menuRect)

        
        desenhar_botao(const.width/2 - 50, const.height/2 - 25, 100, 50, "gray", "Iniciar", "white")
        desenhar_botao(const.width/2 - 50, const.height/2 - (-50), 100, 50, "gray", "Sair", "white")

        pygame.display.update()

    return "sair"

while tela_atual != "sair":
    if tela_atual == "menu":
        tela_atual = main_menu()
    elif tela_atual == "jogo":
        tela_atual = play()
    elif tela_atual == "sair":
        tela_atual = exit()

    pygame.display.flip()

pygame.quit()
sys.exit()