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
                print('Вправо')
            elif event.key == pygame.K_LEFT:
                # влево
                gun.mleft = True
                print('Влево')
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = False
                print('Стоп право')
                # влево
            if event.key == pygame.K_LEFT:
                gun.mleft = False
                print('Стоп лево')
