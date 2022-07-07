from src.package.shop import Shop

ENTER = 10      # enter
ROLL = 114      # r
BUY = 98        # b
ONE = 49       # 1
TWO = 50       # 2
THREE = 51     # 3
FOUR = 52      # 4
FIVE = 53      # 5

class SAPC():

    def __init__(self, stdscr):
        self.state = 'chill'
        self.board = [None, None, None, None, None]
        self.round = 0
        self.gold = 0
        self.lives = 10
        self.cups = 0
        self.shop = Shop()
        self.scr = stdscr

    def lose_lives(self, round: int):
        if round <= 4:
            self.lives =- 2
        elif round >=5 and round <= 7:
            self.lives =- 3
        else:
            self.lives =- 4

    def __game__(self):
        if self.lives <= 0:
            return False
        elif self.cups == 10:
            return True
        else:
            if self.state == 'chill':
                self.__chill__()
            elif self.state == 'battle':
                self.__battle__()
        
    def __chill__(self):
        self.round += 1
        self.gold = 10
        self.shop.generate_pshop(round=self.round)
        
        while self.state == 'chill':
            key = self.scr.getch()
            if key == ENTER:
                self.state = 'battle'
                
            elif key == ROLL:
                self.shop.generate_pshop(round=self.round)
                self.gold -= 1
                
            elif key == BUY:
                buying = True
                while buying:
                    key = self.scr.getch()
                    if key == BUY:
                        buying = False
                    elif key >= 49 and key <= 53:
                        if self.shop.offer[key - 48] is None:
                            buying = False
                        else:
                            waiting = True
                            while waiting:
                                key = self.scr.getch()
                                if key == BUY:
                                    waiting = False
                                elif key >= 49 and key <= 53:
                                    pill = key - 48
                                    if self.board[pill] == None:
                                        self.board[pill] = self.shop.offer[pill]
                                        self.gold -= 3
                                        waiting = False
                                    elif type(self.board[pill]) == type(self.shop.offer[pill]):
                                        self.board[key - 48].level += 1
                                        self.gold -= 3
                                        waiting = False
                            buying = False
                        
        self.__game__()   
            
    def __battle__(self):
        self.state = 'battle'