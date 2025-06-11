from settings import *

class Player():
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.body_parts = []
        self.body_parts.append([14 * BLOCK_SIZE, 14 * BLOCK_SIZE])
        self.body_parts.append([13 * BLOCK_SIZE, 14 * BLOCK_SIZE])
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
            for i in range(len(self.body_parts) - 1, 0, -1):
                print(i)
                self.body_parts[i] = self.body_parts[i - 1].copy()
            if self.direction == "right":
                self.body_parts[0][0] += BLOCK_SIZE
            if self.direction == "left":
                self.body_parts[0][0] -= BLOCK_SIZE
            if self.direction == "up":
                self.body_parts[0][1] -= BLOCK_SIZE
            if self.direction == "down":
                self.body_parts[0][1] += BLOCK_SIZE
            self.move_count += 1
            
    def update(self,dt):
        self.move(dt)
        for i in range(len(self.body_parts)):
            pygame.draw.rect(self.display_surface, PLAYER_COLOUR, (self.body_parts[i], (BLOCK_SIZE, BLOCK_SIZE)))