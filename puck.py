import pygame
from random import randint
 
class Puck(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.speed = [randint(6,10),randint(-6,6)]
        
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
          
    def bounce(self):
        self.speed[0] = -self.speed[0]
        self.speed[1] = randint(-8,8)