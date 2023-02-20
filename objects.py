import pygame 


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.surf = pygame.Surface((w, h))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (10, 420))