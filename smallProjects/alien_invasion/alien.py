import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    create an alien
    """

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def blitme(self):
        """
        draw an alien in the specified loc
        :return: no
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        move to rightward
        :return: no
        """
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """
        check if an alien is in the edge
        :return: true or false
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

