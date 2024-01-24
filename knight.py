import pygame as pg

class Knight:
    """class to manage knight"""
    def __init__(self, defender):
        self.screen = defender.screen
        self.settings = defender.settings
        self.screen_rect = defender.screen.get_rect()

        # load image of knight and get its rect
        self.image = pg.transform.scale(pg.image.load(
            'images/knight.bmp'),
            (20, 16)
        )
        self.rect = self.image.get_rect()

        # start each new knight
        self.rect.midbottom = self.screen_rect.midbottom

        # decimal values
        self.x = float(self.rect.x)

        # movement indication
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update position based on movement indication
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.knight_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.knight_speed

        # update rectangle object from self.x
        self.rect.x = self.x



    def blitme(self):
        # draw knight at his location
        self.screen.blit(self.image, self.rect)