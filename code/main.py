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
        self.font = pygame.font.Font("snake/images/Pixeltype.ttf", 30)
        self.font2 = pygame.font.Font("snake/images/Pixeltype.ttf", 60)
        self.game_state = 1

        #text
        self.game_over_message_surf = self.font2.render("GAME OVER", False, "White")
        self.game_over_message_rect = self.game_over_message_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 50))
        self.starting_message_surf = self.font2.render("PRESS ANY KEY TO START", False, "White")
        self.starting_message_rect = self.starting_message_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def display_score(self, running):
        if running:
            self.score_surf = self.font.render("Score: " + str(len(self.player.body_parts) - 2), False, "White")
            self.score_rect = self.score_surf.get_frect(topleft = (10, 5))
        else:
            self.score_surf = self.font.render("Final Score: " + str(len(self.player.body_parts) - 2), False, "White")
            self.score_rect = self.score_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50))
        self.display_surface.blit(self.score_surf, self.score_rect)

    def run(self):
        while self.running:
            dt = self.clock.tick(100) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and self.game_state != 2:
                    self.game_state = 2
                    self.apple = Apple(self.display_surface)
                    self.player = Player(self.display_surface, self.apple, pygame.time.get_ticks())

            self.display_surface.fill("Black")
            if self.game_state == 1:
                self.display_surface.blit(self.starting_message_surf, self.starting_message_rect)

            elif self.game_state == 2:
                self.player.update()
                self.display_score(True)
                self.apple.draw()

                if self.player.collide():
                    self.game_state = 3
                    
            elif self.game_state == 3:
                self.display_surface.blit(self.game_over_message_surf, self.game_over_message_rect)
                self.display_score(False)

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()