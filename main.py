from curses import wrapper

from src.sapc import SAPC

def main(stdscr):
    game = SAPC(stdscr)
    if game.__game__():
        pass # won
    else:
        pass # lost
    
if __name__ == '__main__':
    wrapper(main)