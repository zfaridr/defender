import pygame.font
from pygame.sprite import Group
from knight import Knight

class Scoreboard:
    # class to report score information
    def __init__(self, defender):
        self.defender = defender
        self.screen = defender.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = defender.settings
        self.stats = defender.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_knights()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.knights.draw(self.screen)

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect_centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect_right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_knights(self):
        # how many lifes are left
        self.knights = Group()
        for knight_number in range(self.stats.knights_left):
            knight = Knight(self.defender)
            knight.rect.x = 10 + knight_number * knight.rect.width
            knight.rect.y = 10
            self.knights.add(knight)