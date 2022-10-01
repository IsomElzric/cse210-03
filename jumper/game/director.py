"""
director.py
This got messy fast, I'm not exactly happy with how it turned out, but by the time I
started to really see just how overworked this project was, it was pretty late into it.
In any case, given time I would have loved to cut this up and move parts into classes of
their own, overall it just turned into a bit of a mess.

for CSE 210 w03
by Alexander Turner
"""


from game.guesser import Guesser
from game.jumper import Jumper
from game.terminal import Terminal


class Director:
    """
    Handles the terminal, jumper, and guesser classes and runs the game loop with some
    logic.
    """
    def __init__(self):
        """
        Initializes the other classes and a few variables.
        """
        self._terminal = Terminal()
        self._jumper = Jumper()
        self._guesser = Guesser(self._jumper.generate_word())
        self._guess = ""
        self._run = self.check_game_end()
        self._end = False
        self._outcome = ""        

    def start_game(self):
        """
        Runs the game loop.
        """
        while self._run:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def do_updates(self):
        """
        Passes the letter entered to the jumper class and handles the result.
        """
        if not self._guesser.add_letter(self._jumper.get_guess_indices(self._guess), self._guess):
            if not self._jumper.guessed_wrong():
                # self._terminal.write_text("\nYou didn't guess the word!\n")    
                self._end = True
                self._outcome = "lose"
        if self._jumper.check_win(self._guesser.current_word()):
            # self._terminal.write_text("\nYou guessed the word!\n")
            self._end = True
            self._outcome = "win"

        self._run = self.check_game_end(self._end, self._outcome)
        

    def do_outputs(self):
        """
        Calls the terminal class to display the game board.
        """
        # print("DEBUG@Director: Word from guesser -> terminal is {}".format(self._guesser.current_word()))
        self._terminal.display_game(self._guesser.current_word(), self._jumper.get_jump_guy())
        

    def get_inputs(self):
        """
        Calls the terminal class to prompt the user for a letter.
        """
        self._guess = self._terminal.prompt_guess()

    def check_game_end(self, ended=False, outcome=""):
        """
        Checks if the game has ended and how, calls the terminal to print a message.
        """
        if ended:
            self.do_outputs()

            if outcome == "win":
                self._terminal.write_text("\nYou guessed the correct word!\n")
            
            elif outcome == "lose":
                self._terminal.write_text("\nYou didn't guess the word!\n")
            
            else:
                self._terminal.write_text("\nSomething went horribly wrong and the game has ended!\n")
            
            return False

        else:
            return True