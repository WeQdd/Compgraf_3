class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 represents right; -1 represents left
        
        self.ship_limit = 3
        
        self.bullets_allowed = 3
        
        self.alien_points = 50