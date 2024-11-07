import pygame
from players import PlayerClass
from puck import Puck
import time

pygame.init()

WHITE = (255,255,255)
BLUE=(143, 227, 255)
RED=(255, 143, 143)
GREEN = (40, 74, 49)

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong game")
 
playerL = PlayerClass(RED, 20, 100)
playerL.rect.x = 10
playerL.rect.y = 360
 
playerR = PlayerClass(BLUE, 20, 100)
playerR.rect.x = 1260
playerR.rect.y = 200
 
puck = Puck(WHITE,20,20)
puck.rect.x = 640
puck.rect.y = 360

sprites = pygame.sprite.Group()
 

sprites.add(playerL)
sprites.add(playerR)
sprites.add(puck)
 
gameRunning = True
 
clock = pygame.time.Clock()

scoreL = 0
scoreR = 0

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              gameRunning = False
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                     gameRunning=False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerL.up(10)
    if keys[pygame.K_s]:
        playerL.down(10)
    if keys[pygame.K_UP]:
        playerR.up(10)
    if keys[pygame.K_DOWN]:
        playerR.down(10)    
 
    sprites.update()
    
    if puck.rect.x>=1265:
        scoreL+=1
        puck.speed[0] = -puck.speed[0]
    if puck.rect.x<=0:
        scoreR+=1
        puck.speed[0] = -puck.speed[0]
    if puck.rect.y>700:
        puck.speed[1] = -puck.speed[1]
    if puck.rect.y<0:
        puck.speed[1] = -puck.speed[1]     
 
    if pygame.sprite.collide_mask(puck, playerL) or pygame.sprite.collide_mask(puck, playerR):
      puck.bounce()

    screen.fill(GREEN)
    pygame.draw.line(screen, WHITE, [640, 0], [640, 720], 5)
    
    sprites.draw(screen) 
 
    font = pygame.font.Font("monofett.ttf", 100)
    text = font.render(str(scoreL), 1, WHITE)
    screen.blit(text, (320,10))
    text = font.render(str(scoreR), 1, WHITE)
    screen.blit(text, (960,10))
 
    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()