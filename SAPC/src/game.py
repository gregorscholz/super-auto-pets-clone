import curses

from src.sapc import SAPC
from src.utils import draw_border


def start_game(stdscr):
    game = SAPC()
    while 1:
        stdscr.clear()
        draw_border(stdscr)
        
        if game.state == 'chill':
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