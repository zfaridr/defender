import pygame as pg

class GameStats:
    """track statistics of the game"""
    def __init__(self, defender):
        self.settings = defender.settings
        self.reset_stats()
        # start game in an inactive state
        self.game_active = False
        # record high score
        self.high_score = 0
    
    def reset_stats(self):
        self.knights_left = self.settings.knight_limit
        self.score = 0
        self.level = 1