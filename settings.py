class Settings:
    """a class to store all settings"""


    def __init__(self):
        """initialise game settings"""
        #screen settings

        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(125, 133, 151) #to set backgroung color

        self.ship_speed=1.8
        self.ship_limit=3

        #bullet settings
        self.bullet_speed=2.6
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=5
        self.alien_speed=1.2
        self.alien_drop_speed=10
        self.fleet_drop_speed=10
        #fleet direction fo 1 represent right and -1 represents left
        self.fleet_direction=1
        
 