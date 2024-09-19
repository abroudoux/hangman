import pygame

from src.game import Game

class Gui:
    def __init__(self):
        pygame.init()

        self.game = Game(cheat=False, random=False, max_len=4)

        self.dimensions_screen = 600
        self.screen = pygame.display.set_mode((self.dimensions_screen, self.dimensions_screen))
        self.clock = pygame.time.Clock()
        self.running = True

    def start_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill("purple")
            self.game.play()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()