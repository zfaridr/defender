import sys
import pygame as pg
from settings import Settings
from knight import Knight

class Defender:
    """class for game assets and behaviour"""
    def __init__(self):
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pg.display.set_caption('Defender')

        self.knight = Knight(self)
        

    def run_game(self):
        """start game"""
        while True:
             self.check_events()
             self.knight.update()
             self.update_screen()
            

    def check_events(self):
            # watch for events from keyboard and mouse
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        self.knight.moving_right = True
                    elif event.key == pg.K_LEFT:
                        self.knight.moving_left = True  
                
                
                
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT:
                        self.knight.moving_right = False
                    elif event.key == pg.K_LEFT:
                        self.knight.moving_left = False

            
            
    def update_screen(self):
         # redraw the screen each pass of loop
        self.screen.fill(self.settings.bg_color)
        self.knight.blitme()
            
        # rmost ecently drawn screen
        pg.display.flip()

if __name__ == '__main__':
    # run the game
    defender = Defender()
    defender.run_game()            