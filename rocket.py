import sys
import pygame

from rocketship import Rocketship

class Rocket:
    """A class to represent a rocket the user can move around the screen."""
    def __init__(self):
        """Initializes the game attributes assets and behavior."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280,720))
        self.rocketship = Rocketship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.screen.fill((13, 14, 45))

            # Update rocketship
            self.rocketship.update(self)

            # Draw rocketship
            self.screen.blit(self.rocketship.rocketship, self.rocketship.rect)

            self.clock.tick(60)
            pygame.display.flip()
            
    def _check_events(self):
        """Check for events in the app: keypresses and exits"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_UP:
                    self.rocketship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.rocketship.moving_down = True
                if event.key == pygame.K_LEFT:
                    self.rocketship.moving_left = True
                if event.key == pygame.K_RIGHT:
                    self.rocketship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.rocketship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.rocketship.moving_down = False
                if event.key == pygame.K_LEFT:
                    self.rocketship.moving_left = False
                if event.key == pygame.K_RIGHT:
                    self.rocketship.moving_right = False

if __name__ == '__main__':
    r = Rocket()
    r.run_game()