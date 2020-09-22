class GameStats:
    """
    collect the stats info during the game
    """

    def __int__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """
        reset the stats info in a game
        :return:
        """
        self.ships_left = self.ai_settings.ship_limit
