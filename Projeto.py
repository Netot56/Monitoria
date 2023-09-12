import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Inicio Pygame")

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Variáveis do círculo
raio = 50
x_circulo = largura // 2
y_circulo = altura // 2

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpa a tela
    janela.fill(branco)


    # Atualiza a tela
    pygame.display.update()
