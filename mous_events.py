import pygame as pg
import sys

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

pg.init()
sc = pg.display.set_mode((400, 300))
sc.fill(WHITE)
pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

        sc.fill(WHITE)

        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                pg.draw.circle(
                    sc, RED, i.pos, 20)
                pg.display.update()
            elif i.button == 3:
                pg.draw.circle(
                    sc, BLUE, i.pos, 20)
                pg.draw.rect(
                    sc, GREEN,
                    (i.pos[0] - 10,
                     i.pos[1] - 10,
                     20, 20))
                pg.display.update()
            elif i.button == 2:
                sc.fill(WHITE)
                pg.display.update()

    if pg.mouse.get_focused():
        pos = pg.mouse.get_pos()
        pg.draw.rect(
            sc, BLUE, (pos[0] - 10,
                       pos[1] - 10,
                       20, 20))
    pg.display.update()

    pg.time.delay(20)