from src.shop import Shop


class SAPC():

    def __init__(self):
        self.state = 'chill'
        self.board = [None, None, None, None, None]
        self.round = 0
        self.gold = 10
        self.lives = 10
        self.cups = 0
        self.shop = Shop()
        
    def buy(self, stdscr):
        while True:
            key = stdscr.getch()
            if key == ord('b'):
                break
            elif key >= ord('1') and key <= ord('5'):
                if self.shop.board[key - 49] is None:
                    break
                else:
                    pet = self.shop.board[key - 49]
                    while True:
                        key = stdscr.getch()
                        if key == ord('b'):
                            break
                        elif key >= ord('1') and key <= ord('5'):
                            pnum = key - 49
                            if self.board[pnum] == None:
                                self.board[pnum] = pet
                                self.gold -= 3
                                break
                            elif type(self.board[pnum]) == type(pet):
                                #self.board[pnum].level += 1
                                self.gold -= 3
                        break
            break
                   
    def reroll(self):
        self.shop.generate_pshop(round=self.round)
        self.gold -= 1
        
    def battle(self):
        self.state = 'battle' 
        
    def new_round(self):
        self.round += 1
        self.gold = 10
        self.shop.generate_pshop(round=self.round)   
        
    def check_status(self):
        if self.lives <= 0:
            return False
        elif self.cups == 10:
            return True
        else:
            return None 
        
    def lose_lives(self):
        round = self.round
        if round <= 4:
            self.lives =- 2
        elif round >=5 and round <= 7:
            self.lives =- 3
        else:
            self.lives =- 4         