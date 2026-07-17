import pygame
#from settings import Settings

class Ship:

    """to manage our ship"""

    def __init__(self,ai_game):

        """initialise ship and set its starting position"""
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #load ship image and get its rect

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        #start each a new ship at bottm center of the screen
        self.rect.midbottom=self.screen_rect.midbottom

        #store a float for ship horiztonal postiion(eract)
        self.x=float(self.rect.x)

        #movement flag , start with a ship not moving
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """update the ships postition based on movement flag"""
        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0:
            self.x -= self.settings.ship_speed
        #update rect bkect form self.x
        self.rect.x=self.x

    def blitme(self):
        """draw the ship at current location"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """center the ship on screen"""
        self.rect.midbottom =self.screen_rect.midbottom
        self.x = float(self.rect.x)

