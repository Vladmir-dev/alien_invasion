class GameStats:
    """Tracks statistics for the game"""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.score = 0
        self.level = 1
        # start Alien invasion in an active state
        self.game_active = False

        #high score shouldn't be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialise statistics that csn change during the game"""
        self.ships_left = self.settings.ship_limit
