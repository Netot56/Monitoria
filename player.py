import pygame
from settings import import_folder


pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("heroi/personagem0.png")
        self.pos = pygame.math.Vector2(x, y)
        self.rect = self.image.get_rect(center = (self.pos.x, self.pos.y))


        # Definição graficas do personagem
        self.import_player_assets()
        self.status = 'down' # Definição da posição inicial
        self.flame_index = 0
        self.animation_speed = 0.15 # Velocidade da transição das imagem
    
    def import_player_assets(self):
        character_path = '../sprites/hero/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
            'right_idle': [], 'left_idle': [], 'up_idle':[] ,'down_idle': [], 
            'right_attack':[], 'left_attack':[], 'up_attack':[], 'down_attack':[]}
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations [animation] = import_folder(full_path)
    
    def get_status(self):

        #idle status
        if self.direction_x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        
        

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed

        # Para não passar a quantidade de imagens
        if self.frame_index >= len(animation):
            self.frame_index = 0 # reiniciando as imagem 
        
        # Definição da imagem do personagem
        self.image = animation [int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        self.direction = pygame.math.Vector2

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1

