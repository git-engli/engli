import sys
import termios
import tty
import re

class SuggestionEngine:
    def __init__(self):
        self.suggestions = {
            "Train a classification model: ": 
            "I want you to act as a data scientist and code for me. "
            "I have a dataset of `[describe dataset]`. "
            "Please build a machine learning model that predicts `[target variable]`.", 

            "Automatic machine learning": 
            "I want you to act as an automatic machine learning (AutoML) bot using TPOT for me. "
            "I am working on a model that predicts `[...]`. "
            "Please write Python code to find the best classification model with the highest AUC score on the test set."
        }

    def generate_suggestion(self, user_input):
        suggestion = 'No available suggestions.'
        likelihood = 0
        for phrase, completion in self.suggestions.items():
            if phrase.lower().startswith(user_input.lower()):
                likelihood = len(user_input) / len(phrase) 
                suggestion = f"{completion} \n likelihood: {likelihood}"
        return suggestion

    def get_char(self):
        # Function to handle the character by character input
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def run(self):
        print('Start typing...')
        user_text = ''

        while True:
            char = self.get_char()
            if char == '\n':
                user_text = ''  # reset text on new line
                print('New line detected. Resetting suggestions...')
                continue
            user_text += char
            print('Current text:', user_text)
            print('Suggested:', self.generate_suggestion(user_text))


if __name__ == "__main__":
    engine = SuggestionEngine()
    engine.run()