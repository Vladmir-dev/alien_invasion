class Settings:
    """a class to store all setings for alien invasion"""

    def __init__(self):
        """Initialise the games's settings"""
        # screen settings
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10

        # how quckly the game speeds up
        self.speedup_scale = 1.1
        # how quickly the alien pont values increase
        self.score_scale = 1.5
        self.initalise_dynamic_settings()

    def initalise_dynamic_settings(self):
        """Initialise settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet directon of 1 represents right; fleet directon -1 represents right
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """increase speed setings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
