import sys
import termios
import tty
from prettytable import PrettyTable
from fuzzywuzzy import process
from engli.engli.translate.promptsmap import suggestionsmap
class SuggestionEngine:
    def __init__(self):
        self.phrases = suggestionsmap
        

    def generate_suggestion(self, user_input):
        matches = process.extract(user_input, self.phrases.keys(), limit=15)
        self.print_table(matches)
        return matches[0] if matches else ('No available suggestions.', 0)

    def print_table(self, matches):
        table = PrettyTable()
        table.field_names = ["Suggestion", "Likelihood", "Full Text"]

        for match, score in matches:
            table.add_row([match, score, self.phrases[match]])
        print(table)

    def get_char(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def run(self):
        print('Start typing...')
        user_text = ''
        while True:
            char = self.get_char()
            if char == '\x7f':
                user_text = user_text[:-1]
            elif char == '\n':
                user_text = ''  # reset text on new line
                print('New line detected. Resetting suggestions...')
                continue
            else:
                user_text += char
            print('Current text:', user_text)
            print('Suggested:', self.generate_suggestion(user_input=user_text))

if __name__ == "__main__":
    engine = SuggestionEngine()
    engine.run()