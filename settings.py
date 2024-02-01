class Settings:
    """store all setting of the game"""

    def __init__(self):
        # screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (10, 10, 255)

        # knight settings
        self.knight_speed = 1.5
        self.knight_limit = 3

        # pike settings
        self.pike_speed = 1.5
        self.pike_width = 5
        self.pike_height = 20
        self.pike_color = (50, 50 ,50)
        self.pikes_allowed = 5

        # wolf settings
        self.wolf_speed = 1.0
        self.wolfs_drop_speed = 10
        # +1 - right, - 1 - left
        self.horde_direction = 1

        
        

