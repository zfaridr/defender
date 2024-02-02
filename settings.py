class Settings:
    """store all setting of the game"""

    def __init__(self):
        # static settings
        # screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (10, 10, 255)

        # knight settings
        self.knight_limit = 3

        # pike settings
        self.pike_width = 5
        self.pike_height = 20
        self.pike_color = (50, 50 ,50)
        self.pikes_allowed = 5

        # wolf settings
        
        self.wolfs_drop_speed = 10

        # how quickly the enimies will icrease their speed
        self.speedup_scale = 1.1

        # increase of point value level by level
        self.score_scale = 2
        self.initialize_dynamic_settings()
        

    def initialize_dynamic_settings(self):
        # settings that change during the game
        self.knight_speed = 1.5
        self.pike_speed = 1.5
        self.wolf_speed = 0.8
        # +1 - right, - 1 - left
        self.horde_direction = 1
        # scoring
        self.wolf_points = 100

    def increase_speed(self):
        
        self.knight_speed *= self.speedup_scale
        self.pike_speed *= self.speedup_scale
        self.wolf_speed *= self.speedup_scale

        self.wolf_points = int(self.wolf_points * self.score_scale)



        
        

