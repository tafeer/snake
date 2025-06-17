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
        self.font = pygame.font.Font("snake/images/Oxanium-Bold.ttf", 20)

        #apple
        self.apple = Apple(self.display_surface)

        #player
        self.player = Player(self.display_surface, self.apple)

        #text

    def display_score(self):
        self.score = self.font.render("Score: " + str(len(self.player.body_parts) - 2), True, "White")
        return self.score

    def run(self):
        while self.running:
            dt = self.clock.tick(100) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display_surface.fill("Black")
            self.display_score
            self.display_surface.blit(self.display_score(), (10, 5))
            self.apple.draw()
            self.player.update()

            pygame.display.update()
            if self.player.collide():
                self.running = False

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()