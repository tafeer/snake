from settings import *
from random import randint

class Apple():
    def __init__(self, display_surface):
        self.image = pygame.image.load("snake/images/apple.png")
        self.display_surface = display_surface

    def spawn(self):
        self.position = [randint(0, WINDOW_WIDTH - 1) // BLOCK_SIZE * BLOCK_SIZE, randint(0, WINDOW_HEIGHT - 1) // BLOCK_SIZE * BLOCK_SIZE]
        return self.position

    def draw(self):
        self.display_surface.blit(self.image, self.position)