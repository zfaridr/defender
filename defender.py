import sys
import pygame as pg
from settings import Settings
from knight import Knight
from pike import Pike

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
        self.pikes = pg.sprite.Group()
        

    def run_game(self):
        """start game"""
        while True:
            self.check_events()
            self.knight.update()
            self.update_pikes()
            
            print(len(self.pikes))

            
            self.update_screen()
            

    def check_events(self):
        # watch for events from keyboard and mouse
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.check_keydown_event(event)
                             
            elif event.type == pg.KEYUP:
                self.check_keyup_event(event)
                    
    def check_keydown_event(self, event):
        if event.key == pg.K_RIGHT:
            self.knight.moving_right = True
        elif event.key == pg.K_LEFT:
            self.knight.moving_left = True
        elif event.key == pg.K_q:
            sys.exit()
        elif event.key == pg.K_SPACE:
            self.drop_pike()

    def check_keyup_event(self, event):
        if event.key == pg.K_RIGHT:
            self.knight.moving_right = False
        elif event.key == pg.K_LEFT:
            self.knight.moving_left = False

    def drop_pike(self):
        # create new pike and add it to the group
        if len(self.pikes) < self.settings.pikes_allowed:
            new_pike = Pike(self)
            self.pikes.add(new_pike)   

    def update_pikes(self):
        self.pikes.update()
        # delete disappeared pikes from memory
        for pike in self.pikes.copy():
            if pike.rect.bottom <= 0:
                self.pikes.remove(pike)




    def update_screen(self):
         # redraw the screen each pass of loop
        self.screen.fill(self.settings.bg_color)
        self.knight.blitme()
        for pike in self.pikes.sprites():
            pike.draw_pike()

        # rmost ecently drawn screen
        pg.display.flip()

if __name__ == '__main__':
    # run the game
    defender = Defender()
    defender.run_game()            