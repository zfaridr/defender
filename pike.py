import pygame as pg
from pygame.sprite import Group, Sprite

class Pike(Sprite):
    """to manage pikes from knight"""
    def __init__(self, defender):
        # create pike at the knight's position
        super().__init__()
        self.screen = defender.screen
        self.settings = defender.settings
        self.color = self.settings.pike_color

        # create pike rectangle at (0,0) and then set position
        self.rect = pg.Rect(0, 0, self.settings.pike_width,
            self.settings.pike_height)
        self.rect.midtop = defender.knight.rect.midtop

        # store position
        self.y = float(self.rect.y)

    def update(self):
        # moving pike up
        self.y -= self.settings.pike_speed
        self.rect.y = self.y

    def draw_pike(self):
        pg.draw.rect(self.screen, self.color, self.rect)
