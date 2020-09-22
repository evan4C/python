import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    manage the bullet shot from the ship
    """

    def __init__(self, ai_settings, screen, ship):
        """
        create the bullet in the location of the ship
        :param ai_settings: game settings
        :param screen: game surface
        :param ship: ship object
        """
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # location of the bullet
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """
        move the bullet up
        :return: no
        """
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """
        draw the bullet
        :return: no
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
