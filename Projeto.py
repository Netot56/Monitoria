import pygame
import sys

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("playerPH.png")
        self.image = pygame.transform.scale(self.image, (25, 50))
        self.pos = pygame.Vector2(x, y)
        self.rect = self.image.get_rect(center = (self.pos.x, self.pos.y))

        self.group = pygame.sprite.GroupSingle()
        self.group.add(self)

    

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
