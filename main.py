import pygame as pg
import sys

from game import Game, GameState
pg.init()

#GLOBAL VARIABLES

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SCREEN_CAPTION = "Tetris Clone Pygame"
FPS = 60
TIME_SINCE_LAST_FRAME = 1000
DARK_BLUE = (44,44,127)

game_clock = pg.time.Clock()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption(SCREEN_CAPTION)


game = Game()    
#GAME LOOP
while game.game_state == GameState.RUNNING:
    dt = game_clock.tick(FPS) / TIME_SINCE_LAST_FRAME
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                game.move_left()
            if event.key == pg.K_RIGHT:
                game.move_right()
            if event.key == pg.K_UP:
                game.rotate()
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_DOWN]:
        game.move_down()
    #UPDATES
    game.update(dt)
    #DRAW
    screen.fill(DARK_BLUE)
    game.draw(screen)
    pg.display.update()
