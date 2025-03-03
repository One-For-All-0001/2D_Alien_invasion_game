import sys
import pygame

#From the file settings import the class 'Settings'.
from settings import Settings



class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()
        # Creating a clock
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #Creating a display window.And using the Height and width Attriutes from the Settings class.
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")




    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            # Using the Background color attribute of the class Settings.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            # This will run the loop exactlt 60 times per second.
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()