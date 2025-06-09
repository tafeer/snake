from settings import *

class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.running = True

        #groups
        self.all_sprites = pygame.sprite.Group()

        #player
        self.player = Player()

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display_surface.fill("Black")
