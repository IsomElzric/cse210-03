from game.guesser import Guesser
from game.jumper import Jumper
from game.terminal import Terminal


class Director:
    def __init__(self):
        self._terminal = Terminal()
        self._jumper = Jumper()
        self._guesser = Guesser(self._jumper.generate_word())
        self._guess = ""
        self._run = True
        self._win = False        

    def start_game(self):
        while self._run:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def do_updates(self):
        if not self._guesser.add_letter(self._jumper.get_guess_indices(self._guess), self._guess):
            if not self._jumper.guessed_wrong():
                self._terminal.write_text("\nYou didn't guess the word!\n")
                self._win = False
        if self._jumper.check_win(self._guesser.current_word()):
            self._terminal.write_text("\nYou guessed the word!\n")
            self._win = True
        

    def do_outputs(self):
        # print("DEBUG@Director: Word from guesser -> terminal is {}".format(self._guesser.current_word()))
        self._terminal.display_game(self._guesser.current_word(), self._jumper.get_jump_guy())
        

    def get_inputs(self):
        self._guess = self._terminal.prompt_guess()