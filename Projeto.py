from typing import Any
from pygame.locals import *
import pygame, math, sys, os
from telas import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self) # Inicia a classe pai sprites
    
        #armazenar as sprites em uma lista
        self.sprites = []

        #Chamdando a pasta onde estão as imagens do personagem
        self.pasta = './personagem/'

        #Acessando pasta
        self.itens_na_pasta = os.listdir(self.pasta)
        
        for item in self.itens_na_pasta:
            for i in range(1,len(item)):
                #Chamando cada imagem e adicionando na lista self.sprites
                self.sprites.append(pygame.image.load(f'personagem/run-{i}.png'))

        #Primeira imagem que aparece na tela
        self.atual = 0
        self.image = self.sprites[self.atual] 

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
            #self.image = pygame.transform.scale(self.image, (128*3,64*3))



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
        self.x = ponto2[0] - ponto1[0]
        self.y = ponto2[1] - ponto1[1]

    def angulo_para(self, vetor2):
        return math.degrees(math.acos((self.x * vetor2.x + self.y * vetor2.y) / (math.sqrt((self.x ** 2) + (self.y ** 2)) * math.sqrt((vetor2.x ** 2) + (vetor2.y ** 2)))))

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

        if keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s]:
            jogador.andar()
        
        else:
            jogador.parar()
            
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

    #Recebe e lida com inputs do mouse
    mouse = pygame.mouse.get_pressed()

    if mouse[0] and pode_atirar == True:
        pode_atirar = False
        tempo_tiro = pygame.time.get_ticks()
        ponto_mouse = pygame.mouse.get_pos() #Pega a posição (x, y) do mouse
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
