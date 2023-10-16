import pygame
import sys


pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo com Menu')

tela_atual = "menu"

fonte = pygame.font.Font(None, 36)
texto = fonte.render('Precisa importar o código aqui', True, "red")
posicao_texto = texto.get_rect(center=(largura // 2, altura // 2))

# Função para desenhar o botão
def desenhar_botao(x, y, largura, altura, cor, texto, cor_texto):
    pygame.draw.rect(tela, cor, (x, y, largura, altura))
    fonte = pygame.font.Font(None, 36)
    texto_surface = fonte.render(texto, True, cor_texto)
    texto_retangulo = texto_surface.get_rect()
    texto_retangulo.center = (x + largura / 2, y + altura / 2)
    tela.blit(texto_surface, texto_retangulo)

# Função para exibir o menu
def menu():
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if largura/2 - 50 <= mouse[0] <= largura/2 + 50 and altura/2 - 25 <= mouse[1] <= altura/2 + 25:
                    return jogo()

        
        mouse = pygame.mouse.get_pos()

        
        tela.fill("white")

        
        desenhar_botao(largura/2 - 50, altura/2 - 25, 100, 50, "red", "Iniciar", "white")

        pygame.display.update()

    return "sair"



def jogo():
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

        
        tela.fill(("white"))
        tela.blit(texto, posicao_texto)


        pygame.display.update()

    return "sair"

# Loop principal
while tela_atual != "sair":
    if tela_atual == "menu":
        tela_atual = menu()
    elif tela_atual == "jogo":
        tela_atual = jogo()

pygame.quit()
sys.exit()
