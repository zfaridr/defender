import pygame as pg
from pygame.sprite import Sprite

class Enemy(Sprite):
    """Class represents single enemy"""

    def __init__(self, defender):
        super().__init__()
        self.screen = defender.screen
        self.settings = defender.settings

        self.image = pg.transform.scale(pg.image.load(
            'images/wolf2.bmp'),
            (30, 24)
        )
        self.rect = self.image.get_rect()

        # start new wolf near the top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        # move the wolf to the right
        self.x += self.settings.wolf_speed * self.settings.horde_direction
        self.rect.x = self.x   
