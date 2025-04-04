class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        #Width of the game window.
        self.screen_width = 1200
        #Height of the game window.
        self.screen_height = 700
        #Background color.
        self.bg_color = (230,230,230)
        # Ship settings
       
        self.ship_limit = 3

        # Bullet settings
       
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        self.flag = 0
        
        
        # Alien settings
        self.fleet_drop_speed = 10
        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        #Scoring settings
        self.alien_points = 50


    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        self.bullet_width *= self.speedup_scale
        if self.flag >= 2:
            self.bullets_allowed += 1
            self.flag = 0

        else:
            self.flag += 1