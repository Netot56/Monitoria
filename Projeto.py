from typing import Any
from pygame.locals import *
import pygame
import sys
import os

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self) # Inicia a classe pai sprites
    
        #armazenar as sprites em uma lista
        self.sprites = []

        #Chamdando a pasta onde estão as imagens do personagem
        self.pasta = './heroi/'

        #Acessando pasta
        self.itens_na_pasta = os.listdir(self.pasta)
        
        for item in self.itens_na_pasta:
            for i in range(0,11):
                #Chamando cada imagem e adicionando na lista self.sprites
                self.sprites.append(pygame.image.load(f'heroi/Personagem{i}.png'))

        #Primeira imagem que aparece na tela
        self.atual = 0
        self.image = self.sprites[self.atual] 
        self.image = pygame.transform.scale(self.image, (15*2.5,20*2.5))

        #Define a posição como objeto Vector2 (Vetor bidimensional)
        self.pos = pygame.Vector2(x, y)
        self.rect = self.image.get_rect(center = (self.pos.x, self.pos.y)) #Define o objeto rect tendo centro no centro da image
        self.tamanho = self.rect.width #Define tamanho como largura do rect
        self.vel = 1 #Define velocidade


        self.animar = False

    #Fazer o personagem andar
    def andar(self):
        self.animar = True

    #Fazer o personagem parar
    def parar(self):
        self.animar = False

    #Animação do personagem
    def update(self):
        if self.animar == True:
            #Mudança de imagem na iterações
            self.atual = self.atual + 0.2
            
            #Voltando para o 0, após terminar as sprites
            if self.atual>=len(self.sprites):
                self.atual = 0
                #self.animar = False #Precisa mudar
            
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (15*2.5,20*2.5))



    def move(self, direcao):
        #Checks para que o jogador não saia do limite da tela
        if self.pos.y < self.tamanho:
            self.pos.y = self.tamanho

        if self.pos.y > altura - self.tamanho: 
            self.pos.y = altura - self.tamanho

        if self.pos.x < self.tamanho - 14:
            self.pos.x = self.tamanho - 14

        if self.pos.x > largura - self.tamanho + 11: 
            self.pos.x = largura - self.tamanho + 11
        
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

# Inicializa e configura o Pygame
pygame.init()
clock = pygame.time.Clock()

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
'''todas_sprites = pygame.sprite.Group()'''
jogador = Jogador(largura / 2, altura /2)
'''todas_sprites.add(jogador)'''
grupoJogador = pygame.sprite.GroupSingle()
grupoJogador.add(jogador)

cenario = pygame.image.load('cenario/mapa.png')
cenario = pygame.transform.scale(cenario,(largura, altura))

# Loop principal
while True:
    clock.tick(60)
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s]:
            jogador.andar()
        
        else:
            jogador.parar()
            
    #Desenhando meu jogador        
    #todas_sprites.draw(janela)
    #todas_sprites.update()
    

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

    janela.blit(cenario, (0, 0))

    #Desenha o jogador na tela
    grupoJogador.draw(janela)

    pygame.display.flip()

    grupoJogador.update()
    # Atualiza a tela
    pygame.display.update()
