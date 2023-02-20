import pygame
from pygame.locals import *
from objects import Wall, Lidar


pygame.init()
vec = pygame.math.Vector2

WIDTH = 1280
HEIGHT = 720
FPS = 60

fps = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lidar Test")

w1 = Wall(100, 100, 100, 100)
w2 = Wall(800, 100, 100, 500)

all_sprites = pygame.sprite.Group()
all_sprites.add(w1)
all_sprites.add(w2)

walls = [w1, w2]
lidar = Lidar(displaysurface, 200, 200, 0.03, walls)

def display():

    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        
        displaysurface.fill((255,255,255))
    
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)

        lidar.update()

        pygame.display.update()
        fps.tick(FPS)

def isValid(x, y):
    if x < 0 or y < 0:
        return False
    if x >= WIDTH or y >= HEIGHT:
        return False
    return True
    
