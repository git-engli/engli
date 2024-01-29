import sys
import termios
import tty
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
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
        suggestions = []
        for phrase, completion in self.suggestions.items():
            if phrase.lower().startswith(user_input.lower()):
                likelihood = len(user_input) / len(phrase) 
                suggestions.append((completion, likelihood))

        suggestions.sort(key=lambda x: x[1], reverse=True)

        self.visualize_suggestions(suggestions)
        return suggestions[0] if suggestions else ('No available suggestions.', 0)

    def visualize_suggestions(self, suggestions):
        df = pd.DataFrame(suggestions, columns=['suggestion', 'likelihood'])
        date = datetime.now()
        plt.figure(figsize=(10, 8))
        sns.barplot(data=df[:15], y='suggestion', x='likelihood', orient='h')
        plt.title('Top 15 Suggestions')
        plt.savefig(f'{date}suggestions.png')  # Save figure

    def get_char(self):
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
            # handle backspace
            if char == '\x7f':
                user_text = user_text[:-1]
            elif char == '\n':
                user_text = ''  # reset text on new line
                print('New line detected. Resetting suggestions...')
                continue
            else:
                user_text += char

            print('Current text:', user_text)
            print('Suggested:', self.generate_suggestion(user_text))

if __name__ == "__main__":
    engine = SuggestionEngine()
    engine.run()