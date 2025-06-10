from settings import *

class Player():
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.head = [14 * BLOCK_SIZE, 14 * BLOCK_SIZE]
        self.tail = [13 * BLOCK_SIZE, 14 * BLOCK_SIZE]
        self.move_count = 1
        self.direction = "right"

    def move(self,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction = "right"
        if keys[pygame.K_LEFT]:
            self.direction = "left"
        if keys[pygame.K_UP]:
            self.direction = "up"
        if keys[pygame.K_DOWN]:
            self.direction = "down"
        current_time = pygame.time.get_ticks()
        if current_time // MOVE_TIME >= self.move_count:
            if self.direction == "right":
                self.tail = self.head
                self.head[0] += BLOCK_SIZE
            if self.direction == "left":
                self.tail = self.head
                self.head[0] -= BLOCK_SIZE
            if self.direction == "up":
                self.tail = self.head
                self.head[1] -= BLOCK_SIZE
            if self.direction == "down":
                self.tail = self.head
                self.head[1] += BLOCK_SIZE
            self.move_count += 1
            
    def update(self,dt):
        self.move(dt)
        pygame.draw.rect(self.display_surface, PLAYER_COLOUR, ((self.tail), (BLOCK_SIZE, BLOCK_SIZE)))
        pygame.draw.rect(self.display_surface, PLAYER_COLOUR, ((self.head), (BLOCK_SIZE, BLOCK_SIZE)))

