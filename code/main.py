from settings import *
from player import Player
from apple import Apple

class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.running = True

        #apple
        self.apple = Apple(self.display_surface)

        #player
        self.player = Player(self.display_surface, self.apple)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display_surface.fill("Black")
            self.apple.draw()
            self.player.update()

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()