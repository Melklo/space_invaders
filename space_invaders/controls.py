import sys

import pygame


def events(gun):
    '''''обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = True
                print('right_key_on')
            elif event.key == pygame.K_LEFT:
                # влево
                gun.mleft = True
                print('left_key_on')
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = False
                print('right_key_off')
                # влево
            if event.key == pygame.K_LEFT:
                gun.mleft = False
                print('left_key_off')
