import random
import string

class Game:
    #pass
    def __init__(self):
        self.grid = []
        for i in range(9) :
            self.grid.append(random.choice(string.ascii_letters).upper())


    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
