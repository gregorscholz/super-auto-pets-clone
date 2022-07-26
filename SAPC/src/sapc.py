from src.shop import Shop


class SAPC():

    def __init__(self):
        self.state = 'chill'
        self.board = [None, None, None, None, None]
        self.round = 0
        self.gold = 0
        self.lives = 10
        self.cups = 0
        self.shop = Shop()
        
    def buy(self):
        while True:
            key = self.scr.getch()
            if key == BUY:
                break
            elif key >= 49 and key <= 53:
                if self.shop.offer[key - 48] is None:
                    break
                else:
                    while True:
                        key = self.scr.getch()
                        if key == BUY:
                            break
                        elif key >= 49 and key <= 53:
                            pill = key - 48
                            if self.board[pill] == None:
                                self.board[pill] = self.shop.offer[pill]
                                self.gold -= 3
                                waiting = False
                            elif type(self.board[pill]) == type(self.shop.offer[pill]):
                                self.board[key - 48].level += 1
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