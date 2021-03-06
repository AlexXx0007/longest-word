import random
import string
import requests

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
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
