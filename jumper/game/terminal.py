"""
terminal.py
This class just handles the output and input for the project, I would have
liked to move just a bit more into here.

for CSE 210 w03
by Alexander Turner
"""


class Terminal:
    def read_text(self, prompt):
        return input(prompt).lower()

    def write_text(self, text):
        print(text)

    def prompt_guess(self):
        return self.read_text("Guess a letter [a-z]: ")

    def display_game(self, word, list):
        self.write_text("Jumper\n")
        # print("DEBUG@Terminal: Text to join is {}".format(word))
        self.write_text(" ".join(word))
        self.write_text("")
        
        for l in list:
            self.write_text(l)