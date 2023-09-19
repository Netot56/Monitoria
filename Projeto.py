import pygame
import sys

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("playerPH.png")
        self.image = pygame.transform.scale(self.image, (25, 50))
        self.pos = pygame.Vector2(x, y)
        self.rect = self.image.get_rect(center = (self.pos.x, self.pos.y))

        self.size = self.rect.width
        self.speed = 1

    def move(self, direction):
        if self.pos.y < self.size: self.pos.y = self.size
        if self.pos.y > altura - self.size: self.pos.y = altura - self.size
        if self.pos.x < self.size - 14: self.pos.x = self.size - 14
        if self.pos.x > largura - self.size + 11 : self.pos.x = largura - self.size + 11
        
        if direction == "up" and self.pos.y != self.size:
            self.pos.y -= self.speed
        if direction == "down" and self.pos.y != altura - self.size:
            self.pos.y += self.speed
        if direction == "left" and self.pos.x != self.size - 14:
            self.pos.x -= self.speed
        if direction == "right" and self.pos.x != largura - self.size + 11:
            self.pos.x += self.speed
        self.rect = self.image.get_rect(center=(self.pos.x, self.pos.y))

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

#Define objeto Jogador
jogador = Jogador(largura / 2, altura / 2)
grupoJogador = pygame.sprite.GroupSingle()
grupoJogador.add(jogador)

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        grupoJogador.sprite.move("up")
    if keys[pygame.K_s]:
        grupoJogador.sprite.move("down")
    if keys[pygame.K_a]:
        grupoJogador.sprite.move("left")
    if keys[pygame.K_d]:
        grupoJogador.sprite.move("right")

    # Limpa a tela
    janela.fill(branco)

    #Desenha o jogador na tela
    grupoJogador.draw(janela)
    # Atualiza a tela
    pygame.display.update()
