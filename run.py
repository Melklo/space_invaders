import pygame, controls

from space_invaders.gun import Gun


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('космокринж')
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update_rotation()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()


run()