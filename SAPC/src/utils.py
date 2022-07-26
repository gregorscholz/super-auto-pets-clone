import curses


def init_scr():
    curses.initscr()
    window = curses.newwin(32, 100, 0, 0)
    window.timeout(100) 
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    return window

def draw_border(stdscr):
    height, width = stdscr.getmaxyx()
    stdscr.vline(1, 3, curses.ACS_VLINE, height - 2)
    stdscr.vline(1, width - 3, curses.ACS_VLINE, height - 2)
    stdscr.hline(1, 3, curses.ACS_HLINE, width - 5)
    stdscr.hline(height - 1, 3, curses.ACS_HLINE, width - 5)
    
def draw_lives(stdscr, lives):
    stdscr.addstr(2, 5, f'HP: {str(lives)}')
            
def draw_cups(stdscr, cups):
    stdscr.addstr(2, 14, f'TROPHIES: {str(cups)}')
            
def draw_gold(stdscr, gold):
    stdscr.addstr(2, 29, f'GOLD: {str(gold)}')

def draw_own_board(stdscr, board):
    x = 0
    for pet in board:
        # draw pillar
        stdscr.hline(16, 20 + x, curses.ACS_HLINE, 10)
        x += 12

def draw_shop_board(stdscr, board):
    x = 0
    for pet in board:
        # draw pillar
        stdscr.hline(28, 10 + x, curses.ACS_HLINE, 10)
        x += 12