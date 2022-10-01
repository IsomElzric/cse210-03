"""
jumper.py
The Jumper class holds our information and functions for our poor jumper.
This class quickly got out of hand, and with a bit more time and consideration,
I would have loved to trim this whole thing up and clean a lot.

for CSE 210 w03
by Alexander Turner
"""


from random import randint


WORD_LIST_FILE = "jumper/game/assets/word_list.txt"
JUMP_GUY_FILE = "jumper/game/assets/jump_guy.txt"
GUESSES_ALLOWED = 5


class Jumper:
    """ 
    Holds our variables and functions for both our image, and for the word
    that the guesser is trying to figure out.
    """    
    def __init__(self):
        """
        Initializes our word list, and the image of our jump guy.
        """
        self._word = []
        self._word_list = self.load_word_list()
        self._jump_guy = self.load_jump_guy()
        self._guesses = GUESSES_ALLOWED

    def generate_word(self):
        """
        Picks a word from our word list for the guesser to solve.
        """
        self._word = list(self._word_list[randint(0, len(self._word_list))])
        # print("DEBUG@Jumper: Chosen word is {}".format(self._word))
        return self._word

    def get_guess_indices(self, letter):
        """
        Takes a guessed letter and checks if it is in the word we have, it will
        return a list of all the indices of that letter.
        """
        index_list = []
        if letter in self._word:
            count = 0
            for c  in self._word:
                try:
                    index_list.append(self._word.index(letter, count))
                    # print("DEBUG@Jumper: Getting index {} for {}".format(index_list, letter))
                    count += 1

                except ValueError:
                    break

        return index_list

    def get_jump_guy(self):
        """
        Returns the image of the jump guy.
        """
        return self._jump_guy

    def guessed_wrong(self):
        """
        Handles cutting another line of our jump guy image when the wrong letter is
        guessed.
        """
        # print("DEBUG@Jumper: Guessed wrong, removing {}".format(self._jump_guy[0]))
        # print("DEBUG@Jumper: List length is {}".format(len(self._jump_guy)))
        
        if len(self._jump_guy) > self._guesses:
            self._jump_guy = self._jump_guy[1:]
        
        elif len(self._jump_guy) == self._guesses:
            # print("DEBUG@Jumper: List length is 5 changing {}".format(self._jump_guy[0]))
            self._jump_guy[0] = "    X" # Definitely wanted to do better than this
            return False

        return True

    def check_win(self, word):
        """
        Checks if the word that was guessed is the same as the word we picked.
        """
        if word == self._word:
            return True
        else:
            return False

    def load_jump_guy(self):
        """
        Loads our image of the jump guy from a .txt file.
        """
        jump_guy = []
        with open(JUMP_GUY_FILE, "r") as file:
            for line in file:
                jump_guy.append(line.strip("\n"))
        return jump_guy

    def load_word_list(self):
        """
        Loads our word list from a .txt file.
        """
        word_list = []
        with open(WORD_LIST_FILE, "r") as file:
            for word in file:
                word_list.append(word.strip("\n"))
        return word_list