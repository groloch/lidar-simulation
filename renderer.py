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
                x, y = self.lidar.x + distance / 2 * np.cos(angle), self.lidar.y + distance / 2 * np.sin(angle)
                pygame.draw.circle(self.lidar.surf, (0, 0, 0), (720 + x, y), 2)

    def scale(self):
        map = []
        for i in range(len(self.lidar.data)):
            if self.lidar.data[i][2] != 0:
                angle, distance = self.lidar.data[i][0], self.lidar.data[i][1] / self.lidar.data[i][2]
                x, y = self.lidar.x + distance / 2 * np.cos(angle), self.lidar.y + distance / 2 * np.sin(angle)
                map.append(0)
                map[-1] = [x, y, distance]
        return map
    
    def graph(self, map):
        graph = [1 for i in range(len(map))]
        avg = 0
        for i in range(1, len(map)):
            avg += np.sqrt((map[i][0] - map[i-1][0]) ** 2 + (map[i][1] - map[i-1][1]) ** 2)
        avg /= len(map)
        for i in range(1, len(map)):
            if np.sqrt((map[i][0] - map[i-1][0]) ** 2 + (map[i][1] - map[i-1][1]) ** 2) > 3 * avg:
                graph[i] = 0
        if np.sqrt((map[0][0] - map[-1][0]) ** 2 + (map[0][1] - map[-1][1]) ** 2) > 3 * avg:
            graph[0] = 0
        return graph