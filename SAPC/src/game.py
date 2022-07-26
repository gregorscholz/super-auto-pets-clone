import curses

from src.sapc import SAPC
from src.utils import (draw_border, draw_cups, draw_gold, draw_lives,
                       draw_own_board, draw_shop_board)


def start_game(stdscr):
    game = SAPC()
    while 1:
        stdscr.clear()
        draw_border(stdscr)
        
        if game.state == 'chill':
            draw_lives(stdscr, game.lives)
            draw_cups(stdscr, game.cups)
            draw_gold(stdscr, game.gold)
            draw_own_board(stdscr, game.board)
            draw_shop_board(stdscr, game.shop.board)
            key = stdscr.getch()
            # resize event
            if key == curses.KEY_RESIZE:
                stdscr.resize(32, 100)
            # esc
            elif key == 27:
                pass
            # enter
            elif key == 10:
                game.state = 'battle'
            # b, buy
            elif key == ord('b'):
                game.buy(stdscr)
            # r, roll
            elif key == ord('r'):
                game.reroll()
        
        elif game.state == 'battle':
            pass