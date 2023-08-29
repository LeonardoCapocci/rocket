import pygame

class Rocketship:
    """Class to represent the physical ship."""
    def __init__(self, game):
        """Initializes the rocketship's attributes"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.rocketship = pygame.image.load('rocketship.bmp')
        self.rocketship = pygame.transform.scale(self.rocketship, (100, 200))
        self.rect = self.rocketship.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        self.rocketship_speed = 7
    def update(self, game):
        """Updates the positioning of the rocketship"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.rocketship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.rocketship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.rocketship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.rocketship_speed