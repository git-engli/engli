import spacy
import re
import argparse
from codesmap import codemap
from functionsmap import functionmap

nlp = spacy.load('en_core_web_sm')

# Create dictionary for mapping English statements to Python code
CODE_MAP = functionmap

FUNCTION_MAP = functionmap, codemap

def engli_to_python(code):
    """Translates English code into Python code."""
    doc = nlp(code)
    
    for pattern, replacement in CODE_MAP.items():
        code = re.sub(pattern, replacement, code, flags=re.IGNORECASE)
    
    return code


def process_input(args):
    code = engli_to_python(args.sentence)
    print(code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translate English to Python')
    parser.add_argument('sentence', type=str, help='English sentence to translate')
    process_input(parser.parse_args())


