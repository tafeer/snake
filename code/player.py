from settings import *

class Player():
    def __init__(self, display_surface, apple):
        self.display_surface = display_surface
        self.apple = apple
        self.body_parts = []
        self.body_parts.append([14 * BLOCK_SIZE, 14 * BLOCK_SIZE])
        self.body_parts.append([13 * BLOCK_SIZE, 14 * BLOCK_SIZE])
        self.move_count = 1
        self.direction = "right"
        self.has_moved = True
        self.apple_pos = self.apple.spawn(self.body_parts)


    def move(self):
        keys = pygame.key.get_pressed()
        if self.has_moved:
            if keys[pygame.K_RIGHT] and self.direction != "left":
                self.direction = "right"
                self.has_moved = False
            elif keys[pygame.K_LEFT] and self.direction != "right":
                self.direction = "left"
                self.has_moved = False
            elif keys[pygame.K_UP] and self.direction != "down":
                self.direction = "up"
                self.has_moved = False
            elif keys[pygame.K_DOWN] and self.direction != "up":
                self.direction = "down"
                self.has_moved = False
        current_time = pygame.time.get_ticks()
        if current_time // MOVE_TIME >= self.move_count:
            for i in range(len(self.body_parts) - 1, 0, -1):
                self.body_parts[i] = self.body_parts[i - 1].copy()
            if self.direction == "right":
                self.body_parts[0][0] += BLOCK_SIZE
                if self.body_parts[0][0] >= WINDOW_WIDTH:
                    self.body_parts[0][0] = 0
            if self.direction == "left":
                self.body_parts[0][0] -= BLOCK_SIZE
                if self.body_parts[0][0] < 0:
                    self.body_parts[0][0] = WINDOW_WIDTH - BLOCK_SIZE
            if self.direction == "up":
                self.body_parts[0][1] -= BLOCK_SIZE
                if self.body_parts[0][1] < 0:
                    self.body_parts[0][1] = WINDOW_HEIGHT - BLOCK_SIZE
            if self.direction == "down":
                self.body_parts[0][1] += BLOCK_SIZE
                if self.body_parts[0][1] >= WINDOW_HEIGHT:
                    self.body_parts[0][1] = 0
            self.move_count += 1
            self.has_moved = True
            if self.body_parts[0] == self.apple_pos:
                self.apple_pos = self.apple.spawn(self.body_parts)
                self.body_parts.append(self.body_parts[len(self.body_parts) - 1])
            
    def update(self):
        self.move()
        for i in range(len(self.body_parts)):
            rectt = pygame.rect.Rect((self.body_parts[i], (BLOCK_SIZE, BLOCK_SIZE)))
            pygame.draw.rect(self.display_surface, PLAYER_COLOUR, rectt)