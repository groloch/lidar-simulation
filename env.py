import pygame
from pygame.locals import *
from objects import Wall

def display():
    pygame.init()
    vec = pygame.math.Vector2

    HEIGHT = 1280
    WIDTH = 720
    ACC = 0.5
    FRIC = -0.12
    FPS = 60

    fps = pygame.time.Clock()
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Lidar Test")

    w = Wall(10, 10, 100, 100)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(w)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        displaysurface.fill((0,0,0))
    
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)
    
        pygame.display.update()
        fps.tick(FPS)
