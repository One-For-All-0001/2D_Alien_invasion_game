import sys
import pygame

#From the file settings import the class 'Settings'.
from settings import Settings
#From the fiel ship import the class 'Ship'.
from ship import Ship



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
        self.ship = Ship(self)



    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Manages events and keystrokes.
            self._check_events()
            #Draws the background and the ship and flips the screen.
            self._update_screen()
            # This will run the loop exactlt 60 times per second.
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


    def _update_screen(self):
        # Update images on the screen, and flip to the new screen.
        # Using the Background color attribute of the class Settings.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()