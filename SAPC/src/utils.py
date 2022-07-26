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
    stdscr.vline(3, 3, curses.ACS_VLINE, height - 5)
    stdscr.vline(3, width - 3, curses.ACS_VLINE, height - 5)
    stdscr.hline(3, 3, curses.ACS_HLINE, width - 5)
    stdscr.hline(height - 3, 3, curses.ACS_HLINE, width - 5)