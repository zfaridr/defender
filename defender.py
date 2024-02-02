import sys
from time import sleep
import pygame as pg
from settings import Settings
from knight import Knight
from pike import Pike
from enemy import Enemy
from stats import GameStats
from button import Button
from scoreboard import Scoreboard

class Defender:
    """class for game assets and behaviour"""
    def __init__(self):
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pg.display.set_caption('Defender')

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.knight = Knight(self)
        self.pikes = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.wolfs = pg.sprite.Group()

        self.create_horde()
        
        # make play button
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """start game"""
        while True:
            self.check_events()
            
            if self.stats.game_active:
                self.knight.update()
                self.update_pikes()
                self.update_wolfs()

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
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self.check_play_button(mouse_pos)
    
    def check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
        # start new game when player click Play
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_knights()
            self.enemies.empty()
            self.pikes.empty()

            #  new horde and center knight
            self.create_horde()
            self.knight.center_knight()
            
            # hide mouse
            pg.mouse.set_visible(False)

                    
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

        self.check_pikes_wolfs_collisions()

        
        
        

    def check_pikes_wolfs_collisions(self):
        # check collisions pikes with wolfs
        collisions = pg.sprite.groupcollide(self.pikes, self.enemies, True, True)
        if collisions:
            for wolf in collisions.values():
                self.stats.score += self.settings.wolf_points * len(wolf)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.enemies:
            # destroy left pikes and create new horde
            self.pikes.empty()
            self.create_horde()
            self.settings.increase_speed()

            #  increase level
            self.stats.level += 1
            self.sb.prep_level()
    
    def knight_hit(self):
        
        if self.stats.knights_left > 0:
            # decrease num of lifes left
            self.stats.knights_left -= 1
            self.sb.prep_knights()
            # delete all remaining pikes and wolfs
            self.enemies.empty()
            self.pikes.empty()

            # create new horde of wolfs and knight
            self.create_horde()
            self.knight.center_knight()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pg.mouse.set_visible(True)


    def check_wolfs_bottom(self):
        # check if wolfs reach bottom of the screen
        screen_rect = self.screen.get_rect()
        for wolf in self.enemies.sprites():
            if wolf.rect.bottom >= screen_rect.bottom:
                # treat as knight was hit
                self.knight_hit()
                break


    def update_wolfs(self):
        #  check position of each wolf regarding the edge of screen, then update the position
        self.check_horde_edges()
        self.enemies.update()
        if pg.sprite.spritecollideany(self.knight, self.enemies):
            self.knight_hit()

        # looking for wolfs hitting bottom
        self.check_wolfs_bottom()


    def create_horde(self):
        # create horde of wolves
        wolf = Enemy(self)
        wolf_width, wolf_height = wolf.rect.size
        avilable_space_x = self.settings.screen_width - (2 * wolf_width)
        number_wolfs_x = avilable_space_x // (2 * wolf_width)
        
        # determine number of rows
        knight_height = self.knight.rect.height
        avilable_space_y = (self.settings.screen_height - (3 * wolf_height) - knight_height)
        number_rows = avilable_space_y // (2 * knight_height)

        # create full horde
        for row_num in range(number_rows):
            for wolf_num in range(number_wolfs_x):
                self.create_wolf(wolf_num, row_num)
           

    def create_wolf(self, wolf_num, row_num):
        wolf = Enemy(self)
        wolf_width, wolf_height = wolf.rect.size
        wolf.x = wolf_width + 2 * wolf_width * wolf_num
        wolf.rect.x = wolf.x
        wolf.rect.y = wolf.rect.height + 2 * wolf.rect.height * row_num
        self.enemies.add(wolf)

    def check_horde_edges(self):
        for wolf in self.enemies.sprites():
            if wolf.check_edges():
                self.change_horde_direction()
                break

    def change_horde_direction(self):
        for wolf in self.enemies.sprites():
            wolf.rect.y += self.settings.wolfs_drop_speed
        self.settings.horde_direction *= -1


    def update_screen(self):
         # redraw the screen each pass of loop
        self.screen.fill(self.settings.bg_color)
        self.knight.blitme()
        for pike in self.pikes.sprites():
            pike.draw_pike()
        self.enemies.draw(self.screen)

        self.sb.show_score()

        # draw the play button
        if not self.stats.game_active:
            self.play_button.draw_button()

        # rmost ecently drawn screen
        pg.display.flip()

    

if __name__ == '__main__':
    # run the game
    defender = Defender()
    defender.run_game()            