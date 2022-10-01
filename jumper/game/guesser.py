"""
guesser.py
This class is pretty concise and with some time, I likely could have had this
class pulling a little more of the weight that I put into both director and 
jumper.

for CSE 210 w03
by Alexander Turner
"""


class Guesser:
    """
    Holds our information about the word that has been guessed so far.
    """
    def __init__(self, word):
        """
        Initializes an empty word list, then sets it to a series of underscores
        equivalent to the letters in the word chosen by the jumper class.
        """
        self._current_word = []
        # print("DEBUG@Guesser: Word recieved was {}".format(word))

        for c in word:
            self._current_word.append("_")
    
    def current_word(self):
        """
        Returns the word that we have so far.
        """
        return self._current_word

    def add_letter(self, index_list, letter):
        """
        Adds a letter to our word based on a list of indices recieved.
        """
        if len(index_list) > 0:
            for i in index_list:
                self._current_word[i] = letter
            
            return True
        
        else:
            return False