from settings import *
from random import randint

class Apple():
    def __init__(self, display_surface):
        self.image = pygame.image.load("snake/images/apple.png")
        self.display_surface = display_surface

    def spawn(self, body_parts):
        valid_pos = False
        while not valid_pos:
            self.position = [randint(0, WINDOW_WIDTH - 1) // BLOCK_SIZE * BLOCK_SIZE, randint(0, WINDOW_HEIGHT - 1) // BLOCK_SIZE * BLOCK_SIZE]
            valid_pos = True
            for i in range(0, len(body_parts)):
                if self.position == body_parts[i]:
                    valid_pos = False
        return self.position

    def draw(self):
        self.display_surface.blit(self.image, self.position)