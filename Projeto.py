import pygame
import sys

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self) # Inicia a classe pai sprite
        self.image = pygame.image.load("playerPH.png") #Carrega a image do jogador
        self.image = pygame.transform.scale(self.image, (25, 50)) #Diminui o tamanho da image
        self.pos = pygame.Vector2(x, y) #Define a posição como objeto Vector2 (Vetor bidimensional)
        self.rect = self.image.get_rect(center = (self.pos.x, self.pos.y)) #Define o objeto rect tendo centro no centro da image

        self.tamanho = self.rect.width #Define tamanho como largura do rect
        self.vel = 1 #Define velocidade

    def move(self, direcao):
        #Checks para que o jogador não saia do limite da tela
        if self.pos.y < self.tamanho: self.pos.y = self.tamanho
        if self.pos.y > altura - self.tamanho: self.pos.y = altura - self.tamanho
        if self.pos.x < self.tamanho - 14: self.pos.x = self.tamanho - 14
        if self.pos.x > largura - self.tamanho + 11 : self.pos.x = largura - self.tamanho + 11
        
        #Sistema de movimentação do jogador
        if direcao == "up" and self.pos.y != self.tamanho:
            self.pos.y -= self.vel
        if direcao == "down" and self.pos.y != altura - self.tamanho:
            self.pos.y += self.vel
        if direcao == "left" and self.pos.x != self.tamanho - 14:
            self.pos.x -= self.vel
        if direcao == "right" and self.pos.x != largura - self.tamanho + 11:
            self.pos.x += self.vel
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

    #Recebe e lida com inputs do teclado
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
