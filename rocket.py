import sys
import pygame

class Rocket:
    """A class to represent a rocket the user can move around the screen."""
    def __init__(self):
        """Initializes the game attributes assets and behavior."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280,720))
        self.screen_rect = self.screen.get_rect()
        self.rocketship = pygame.image.load('rocketship.bmp')
        self.rocketship = pygame.transform.scale(self.rocketship, (100, 200))
        self.rect = self.rocketship.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.screen.fill((13, 14, 45))

            # Draw rocketship
            self.screen.blit(self.rocketship, self.rect)

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

if __name__ == '__main__':
    r = Rocket()
    r.run_game()