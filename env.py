import pygame
from pygame.locals import *
from objects import Wall, Lidar
from renderer import Renderer


pygame.init()
vec = pygame.math.Vector2

WIDTH = 1440
HEIGHT = 720
FPS = 60

fps = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lidar Test")

w1 = Wall(100, 100, 100, 100)
w2 = Wall(600, 100, 100, 500)

all_sprites = pygame.sprite.Group()
all_sprites.add(w1)
all_sprites.add(w2)

walls = [w1, w2]
lidar = Lidar(displaysurface, 200, 200, 0.1, walls, 1000, 10)
renderer = Renderer(lidar)
map = []
vertices = []

def run():
    global lidar, renderer, map, vertices

    while True:
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            
            displaysurface.fill((255,255,255))
        
            for entity in all_sprites:
                displaysurface.blit(entity.surf, entity.rect)
            
            for i in range(len(map)):
                if vertices[i]:
                    pygame.draw.line(displaysurface, (255, 255, 0), (map[i-1][0] + 720, map[i-1][1]), (map[i][0] + 720, map[i][1]), 4)
                else:
                    pygame.draw.line(displaysurface, (255, 128, 0), (map[i-1][0] + 720, map[i-1][1]), (map[i][0] + 720, map[i][1]), 4)

            lidar.update()
            if lidar.done:
                m2 = renderer.scale()
                if len(map) == 0:
                    map = m2
                else:
                    pass
                vertices = renderer.graph(map) 
                break
            pygame.draw.line(displaysurface, (0, 0, 0), (720, 0), (720, 720))

            renderer.update()



            pygame.display.update()
            fps.tick(FPS)
        lidar = Lidar(displaysurface, 200, 300, 0.1, walls, 1000, 7)
        renderer = Renderer(lidar)
        


def isValid(x, y):
    if x < 0 or y < 0:
        return False
    if x >= 720 or y >= HEIGHT:
        return False
    return True
    
