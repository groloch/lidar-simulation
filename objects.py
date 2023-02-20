import pygame 
import numpy as np
import env


SPEED = 20

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.surf = pygame.Surface((w, h))
        self.surf.fill((60,60, 60))
        self.rect = self.surf.get_rect(center = (x, y))

class Lidar():
    def __init__(self, surf, x, y, dangle, walls):
        self.surf = surf
        self.x = x
        self.y = y
        self.angle = -np.pi/4
        self.dangle = dangle
        self.walls = walls
        self.beams = [LaserBeam(self, surf, x, y, self.angle)]
        self.data = []

    def draw(self):
        pygame.draw.circle(self.surf, (255, 0, 0), (self.x, self.y), 10)
        pygame.draw.line(self.surf, (255, 0, 0), (self.x, self.y), (self.x + np.cos(self.angle) * 100, self.y + np.sin(self.angle) * 100))


    def update(self):
        self.draw()
        self.angle += self.dangle
        self.beams.append(LaserBeam(self, self.surf, self.x, self.y, self.angle))
        for beam in self.beams:
            beam.update()
        for beam in self.beams:
            beam.draw()
        print(len(self.data))

    def beamFeedback(self, beam):
        for b in self.beams:
            if beam == b:
                self.beams.remove(b)
        ratio = env.FPS * SPEED
        self.data.append(0)
        self.data[-1] = [beam.angle, beam.time/2]

class Hitbox():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.time = 0

    def intersects(self, x, y):
        if x >= self.x and x <= self.x + self.w and y >= self.y and y <= self.y + self.h:
            return True
        return False
    

class LaserBeam():
    def __init__(self, lidar, surf, x, y, angle) :
        self.lidar = lidar
        self.surf = surf
        self.x = x
        self.y = y
        self.angle = angle
        self.dx = np.cos(self.angle)
        self.dy = np.sin(self.angle)
        self.collided = False
        self.time = 0
    

    def update(self):

        for i in range(SPEED):
            if not env.isValid(int(self.x + self.dx), int(self.y + self.dy)):
                self.collided = True
                self.dx *= -1
                self.dy *= -1
            else:
                color = self.surf.get_at((int(self.x + self.dx), int(self.y + self.dy)))[:3]
                if color != (255, 255, 255):
                    if self.collided and color == (255, 0, 0):
                        self.lidar.beamFeedback(self)
                        break
                    elif not self.collided and color != (255, 0, 0):
                        self.collided = True
                        self.dx *= -1
                        self.dy *= -1

            self.x+=self.dx
            self.y+=self.dy
            self.time += 1

    def __eq__(self, other) -> bool:
        if isinstance(other, LaserBeam):
            return other.angle == self.angle and other.collided == self.collided
        return False

    
    def draw(self):
        pygame.draw.circle(self.surf, (0, 255, 0), (self.x, self.y), 1)

    
