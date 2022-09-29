class Guesser:
    def __init__(self, word):
        self._current_word = []
        # print("DEBUG@Guesser: Word recieved was {}".format(word))

        for c in word:
            self._current_word.append("_")
    
    def current_word(self):
        return self._current_word

    def add_letter(self, index_list, letter):
        if len(index_list) > 0:
            for i in index_list:
                self._current_word[i] = letter
            
            return True
        
        else:
            return False