import pygame
import numpy as np

class Renderer():
    def __init__(self, lidar):
        self.lidar = lidar

    def update(self):

        pygame.draw.circle(self.lidar.surf, (0, 0, 255), (720 + self.lidar.x, self.lidar.y), 10)

        for i in range(len(self.lidar.data)):
            if self.lidar.data[i][2] != 0:
                angle, distance = self.lidar.data[i][0], self.lidar.data[i][1] / self.lidar.data[i][2]
                x, y = self.lidar.x + 720 + distance / 2 * np.cos(angle), self.lidar.y + distance / 2 * np.sin(angle)
                pygame.draw.circle(self.lidar.surf, (0, 0, 0), (x, y), 2)