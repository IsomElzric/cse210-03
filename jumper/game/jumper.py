from random import randint
import re


WORD_LIST_FILE = "jumper/game/word_list.txt"
JUMP_GUY_FILE = "jumper/game/jump_guy.txt"


class Jumper:    
    def __init__(self):
        self._word = []
        self._word_list = self.load_word_list()
        self._jump_guy = self.load_jump_guy()

    def generate_word(self):
        self._word = list(self._word_list[randint(0, len(self._word_list))])
        print("DEBUG@Jumper: Chosen word is {}".format(self._word))
        return self._word

    def get_guess_indices(self, letter):
        index_list = []
        if letter in self._word:
            count = 0
            for c  in self._word:
                try:
                    index_list.append(self._word.index(letter, count))
                    print("DEBUG@Jumper: Getting index {} for {}".format(index_list, letter))
                    count += 1
                except ValueError:
                    break

        return index_list

    def get_jump_guy(self):
        return self._jump_guy

    def guessed_wrong(self):
        # print("DEBUG@Jumper: Guessed wrong, removing {}".format(self._jump_guy[0]))
        # print("DEBUG@Jumper: List length is {}".format(len(self._jump_guy)))
        if len(self._jump_guy) > 5:
            self._jump_guy = self._jump_guy[1:]
        
        elif len(self._jump_guy) == 5:
            # print("DEBUG@Jumper: List length is 5 changing {}".format(self._jump_guy[0]))
            self._jump_guy[0] = "    X"
            return False

        return True

    def check_win(self, word):
        if word == self._word:
            return True
        else:
            return False

    def load_jump_guy(self):
        jump_guy = []
        with open(JUMP_GUY_FILE, "r") as file:
            for line in file:
                jump_guy.append(line.strip("\n"))
        return jump_guy

    def load_word_list(self):
        word_list = []
        with open(WORD_LIST_FILE, "r") as file:
            for word in file:
                word_list.append(word.strip("\n"))
        return word_list