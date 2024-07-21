import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, ship, bullets):
    """
    response to the operations of mouse and keyboard
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
    response to the key down operation
    :param bullets: bullets group
    :param screen: screen class
    :param ai_settings: settings
    :param event: user operation on keyboard
    :param ship: ship object
    :return: no
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """
    response to the key up operation
    :param event: user operation on keyboard
    :param ship: ship object
    :return: no
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """
    update the images in the screen
    """
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """
    update the loc of bullets and delete the bullets outside of the screen
    :param ship: ship of the player
    :param screen: screen class
    :param ai_settings: ai_settings
    :param aliens: aliens
    :param bullets: bullets group
    :return: no
    """
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """
    check the collisions between bullet and alien and set the response
    :param ai_settings: ai settings
    :param screen: game screen
    :param ship: ship object
    :param aliens: aliens
    :param bullets: bullets
    :return:
    """

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """
    if bullets <= 3, create a new bullet
    :param ai_settings: settings
    :param screen: screen surface
    :param ship: ship object
    :param bullets: bullets group
    :return: no
    """
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """
    calculate how many aliens in a row
    :param ai_settings: settings
    :param alien_width: alien width
    :return: number of aliens in a row
    """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens = int(available_space_x / (2 * alien_width))
    return number_aliens


def get_number_rows(ai_settings, ship_height, alien_height):
    """
    how many rows for aliens in a screen
    :param ai_settings: settings
    :param ship_height: ship height
    :param alien_height: alien height
    :return: number of rows
    """
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """
    create a alien and put it into the current row
    :param row_number: the No of rows for the alien
    :param ai_settings: settings
    :param screen:screen class
    :param aliens:alien object
    :param alien_number: selected alien
    :return:no
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """
    create a fleet of aliens
    :param ship: to calculate the height of a ship
    :param ai_settings: settings
    :param screen: screen class
    :param aliens: alien object
    :return: no
    """
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """
    response to the collision
    :param ai_settings:ai_setting
    :param stats: stats info
    :param screen: screen class
    :param ship: ship object
    :param aliens: aliens
    :param bullets: bullets
    :return:
    """
    if stats.ship_left > 0:
        stats.ship_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)

    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """
    check if the alien reach the bottom of the screen
    :param ai_settings: game settings
    :param stats: game stats info
    :param screen: screen
    :param ship: ship object
    :param aliens: aliens group
    :param bullets: bullets group
    :return:
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """
    update the loc of all the aliens
    :param bullets: bullets
    :param screen: screen
    :param stats: game stats
    :param ship: ship object
    :param ai_settings: settings
    :param aliens: aliens group
    :return: no
    """
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """
    change the moving direction when an alien moves to the edge
    :param ai_settings:settings
    :param aliens:aliens group
    :return:no
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """
    move the alien row down and change moving direction to left
    :param ai_settings:settings
    :param aliens:alien group
    :return:no
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
