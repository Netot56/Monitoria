from typing import Any
from pygame.locals import *
import random as r
import pygame, math, sys, os
from menu import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self) # Inicia a classe pai sprites

        self.animardescendo = False
        self.animardireita = False 
        self.animarsubindo = False
        self.animaresquerda = False


        #armazenar as sprites em uma lista
        self.spritesdescendo = []
        self.spritesdireita = []
        self.spritesesquerda = []
        self.spritessubindo  = []
       
        #Chamdando a pasta onde estão as imagens do personagem
        self.pasta = './heroi/'

        #Acessando pasta
        self.itens_na_pasta = os.listdir(self.pasta)
        
        for item in self.itens_na_pasta:

            for i in range(0,3):
                #Chamando cada imagem e adicionando na lista self.sprites aqui sendo as imagens do personagem descendo
                self.spritesdescendo.append(pygame.image.load(f'heroi/Personagem{i}.png'))
           
            for i in range(3,6):
                #Chamando cada imagem e adicionando na lista self.sprites aqui sendo as imagens do personagem a direita
                self.spritesdireita.append(pygame.image.load(f'heroi/Personagem{i}.png'))
          
         
            for i in range(6,9):
                #Chamando cada imagem e adicionando na lista self.sprites aqui sendo as imagens do personagem a esquerda
                self.spritesesquerda.append(pygame.image.load(f'heroi/Personagem{i}.png'))
              
           
            for i in range(9,12):
                #Chamando cada imagem e adicionando na lista self.sprites aqui sendo as imagens do personagem subindo
                self.spritessubindo.append(pygame.image.load(f'heroi/Personagem{i}.png'))
              


        #Primeira imagem que aparece na tela
        self.atual = 0
        self.image = self.spritesdescendo[self.atual] 
        self.image = pygame.transform.scale(self.image, (15*2.5,20*2.5))

        #Define a posição como objeto Vector2 (Vetor bidimensional)
        self.pos = pygame.Vector2(x, y)
        self.rect = self.image.get_rect(center = (self.pos.x, self.pos.y)) #Define o objeto rect tendo centro no centro da image
        self.tamanho = self.rect.width #Define tamanho como largura do rect
        self.vel = 10 #Define velocidade

       

    #Fazer o personagem andar
    def andardescendo(self):
        self.animardescendo = True
         #Fazer o personagem andar para baixo
        
    def andarsubindo(self):
        self.animarsubindo = True
         #Fazer o personagem andar para cima

    def andardireita(self):
        self.animardireita = True
           #Fazer o personagem andar para direita
       
    def andaresquerda(self):
        self.animaresquerda = True
          #Fazer o personagem andar para esquerda

    #Fazer o personagem parar
    def pararsubindo(self):
        self.animarsubindo = False
       
    def parardescendo(self):
        self.animardescendo = False

    def pararesqueda(self):
        self.animaresquerda = False
    
    def parardireita(self):
        self.animardireita = False
       
       

    #Animação do personagem
    def update(self):
       
        if self.animardescendo == True:
            #Mudança de imagem na iterações
            self.atual = self.atual + 0.12
            
            #Voltando para o 0, após terminar as sprites
            if self.atual>=len(self.spritesdescendo):
                self.atual = 0
                #self.animar = False #Precisa mudar
            
            self.image = self.spritesdescendo[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (15*2.5,20*2.5))

        if self.animarsubindo == True:
            #Mudança de imagem na iterações
            self.atual = self.atual + 0.12
            
            #Voltando para o 0, após terminar as sprites
            if self.atual>=len(self.spritessubindo):
                self.atual = 0
                #self.animar = False #Precisa mudar
            
            self.image = self.spritessubindo[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (15*2.5,20*2.5))

               
        if self.animardireita == True:
            #Mudança de imagem na iterações
            self.atual = self.atual + 0.12
           
            #Voltando para o 0, após terminar as sprites
            if self.atual>=len(self.spritesdireita):
                self.atual = 0
                #self.animar = False #Precisa mudar
        
            self.image = self.spritesdireita[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (15*2.5,20*2.5))


        if self.animaresquerda == True:
            #Mudança de imagem na iterações
            self.atual = self.atual + 0.12
           
            #Voltando para o 0, após terminar as sprites
            if self.atual>=len(self.spritesesquerda):
                self.atual = 0
                #self.animar = False #Precisa mudar
        
            self.image = self.spritesesquerda[int(self.atual)]
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

def nova_pos(velha_pos, vel, angulo):
    mover_vec = pygame.math.Vector2()
    mover_vec.from_polar((vel, angulo))
    return velha_pos + mover_vec

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, dano, vel, tamanho, grupoJogador):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("inimigos/morcego.png")
        self.image = pygame.transform.scale(self.image, tamanho)
        self.pos = (x, y)

        self.rect = self.image.get_rect(center = self.pos)

        self.vel = vel
        self.dano = dano

    def update(self, janela):

        p0 = [self.pos[0], self.pos[1]] #Define p0 na coordenada do player
        p0p1 = Vetor(p0, [janela.get_width(), self.pos[1]]) #Define o vetor p0p1 que é entre o p0 e o ponto mais a direita da tela
        p0p2 = Vetor(p0, grupoJogador.sprite.pos) #Define o vetor p0p2 que é entre p0 e o ponto do mouse

        if p0p2.y <= 0:
            print("<0")
            self.pos = nova_pos(self.pos, self.vel, -p0p1.angulo_para(p0p2))
        if p0p2.y > 0:
            print(">0")
            self.pos = nova_pos(self.pos, self.vel, -(180 +(180 - p0p1.angulo_para(p0p2))))
        self.rect.center = round(self.pos[0]), round(self.pos[1])
        if not janela.get_rect().colliderect(self.rect):
            self.kill()
        if grupoJogador.sprite.rect.colliderect(self.rect):
            self.kill()


class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direc, vel, tamanho):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("objetos/bala.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, direc)
        self.rect = self.image.get_rect(center = (x, y))
        self.pos = (x, y)
        self.direcao = direc
        self.vel = vel

    def update(self, janela):
        self.pos = nova_pos(self.pos, self.vel, -self.direcao)
        self.rect.center = round(self.pos[0]), round(self.pos[1])
        if not janela.get_rect().colliderect(self.rect):
            self.kill()

class Vetor():
    def __init__(self, ponto1 : list, ponto2 : list):
        self.x = int(ponto2[0] - ponto1[0])
        self.y = int(ponto2[1] - ponto1[1])

    def angulo_para(self, vetor2):
        return int(math.degrees(math.acos((self.x * vetor2.x + self.y * vetor2.y) / (math.sqrt((self.x ** 2) + (self.y ** 2)) * math.sqrt((vetor2.x ** 2) + (vetor2.y ** 2))))))

# Inicializa e configura o Pygame
pygame.init()
clock = pygame.time.Clock()

# Configurações da janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Inicio Pygame")

# Variáveis do círculo
raio = 50
x_circulo = largura // 2
y_circulo = altura // 2

#Define objeto e grupo Jogador
jogador = Jogador(largura / 2, altura /2)
grupoJogador = pygame.sprite.GroupSingle()
grupoJogador.add(jogador)

#Define o grupo de sprites gerais
spr = pygame.sprite.Group()

#Carrega
cenario = pygame.image.load('cenario/mapa.png')
cenario = pygame.transform.scale(cenario,(largura, altura))

spawn_positions = []
for i in range(240, 330, 10):
    spawn_positions.append((-20, i))

delay_tiro = 50
pode_atirar = True

# Loop principal
while True:
    clock.tick(60)
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            jogador.andardireita()

        else:
            jogador.parardireita()

        if keys[pygame.K_w]:
            jogador.andarsubindo()
        
        else:
            jogador.pararsubindo()

        if keys[pygame.K_a]:
           
            jogador.andaresquerda()

        else:
            jogador.pararesqueda()

        if keys[pygame.K_s]:
            jogador.andardescendo()
        
        else:
            jogador.parardescendo()

        
            
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

    if keys[pygame.K_e]:
        spr.add(Inimigo(*r.choice(spawn_positions), 15, 10, (25, 25), grupoJogador))

    #Recebe e lida com inputs do mouse
    mouse = pygame.mouse.get_pressed()

    if mouse[0] and pode_atirar == True:
        pode_atirar = False
        tempo_tiro = pygame.time.get_ticks()
        ponto_mouse = pygame.mouse.get_pos() #Pega a posição (x, y) do mouse
        print(ponto_mouse)
        p0 = [grupoJogador.sprite.pos.x, grupoJogador.sprite.pos.y] #Define p0 na coordenada do player
        p0p1 = Vetor(p0, [janela.get_width(), grupoJogador.sprite.pos.y]) #Define o vetor p0p1 que é entre o p0 e o ponto mais a direita da tela
        p0p2 = Vetor(p0, ponto_mouse) #Define o vetor p0p2 que é entre p0 e o ponto do mouse

        if p0p2.y <= 0: #Se o mouse está na metade de cima da tela
            spr.add(Bala(*grupoJogador.sprite.pos, p0p1.angulo_para(p0p2), 15, (10, 10)))
        if p0p2.y > 0: #Se o mouse está na metade de baixo da tela
            spr.add(Bala(*grupoJogador.sprite.pos, 180 + (180 - p0p1.angulo_para(p0p2)), 15, (10, 10)))


    if pode_atirar == False:
        if pygame.time.get_ticks() - tempo_tiro >= delay_tiro:
            pode_atirar = True
                
    # Limpa a tela
    janela.fill((255, 255, 255))
    janela.blit(cenario, (0, 0))

    #Desenha e atualiza o jogador na tela
    grupoJogador.draw(janela)
    grupoJogador.update()

    #Desenha e atualiza todo sprite na tela
    spr.draw(janela)
    spr.update(janela)

    # Atualiza a tela
    pygame.display.flip()
    pygame.display.update()
