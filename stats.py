import pygame as pg

class GameStats:
    """track statistics of the game"""
    def __init__(self, defender):
        self.settings = defender.settings
        self.reset_stats()
        # start game in an active state
        self.game_active = True
    
    def reset_stats(self):
        self.knights_left = self.settings.knight_limit