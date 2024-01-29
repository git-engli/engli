import spacy
import re

nlp = spacy.load('en_core_web_sm')

# Create dictionary for mapping English statements to Python code
CODE_MAP = {
    # Assignments
    'Give (\w*) the value (\w*)': r'\1 = \2',
    
    # Comparisons
    '(\w*) is less than (\w*)': r'\1 < \2',
    '(\w*) is less than or equal to (\w*)': r'\1 <= \2',
    '(\w*) is not equal to (\w*)': r'\1 != \2',
    '(\w*) is equal to (\w*)': r'\1 == \2',
    '(\w*) is greater than (\w*)': r'\1 > \2',
    '(\w*) is greater than or equal to (\w*)': r'\1 >= \2',
    '(\w*) is between (\w*) and (\w*)': r'\2 <= \1 <= \3',
    
    # Control flows
    'If (.*), then (.*) else (.*)': r'if \1: \2\n else: \3',
    
    # Loops
    'Repeat (.*):': r'while True: \1',
    'until (.+):': r'while not (\1):',
    'as long as (.+):': r'while \1:',
    '(.+) times:': r'for _ in range(\1):',
    'Perform (.*) until (.*)':  r'\1\nwhile not \2:\n\t\1',
    'foreach (\w*) in (\w*), do (.*)': r'for \1 in \2: \3',
    'for each (\w*) in (\w*), do (.*)': r'for \1 in \2: \3',
    'for every (\w*) in (\w*), do (.*)': r'for \1 in \2: \3',

    # Functions
    'Define a function (\w*) that takes (\w*), and returns (.*)': r'def \1(\2): return \3',
    'Call the function (\w*) with the parameter (\w*)': r'\1(\2)',

    # Print statement
    'Print (\w*)': r'print(\1)',
}


def engli_to_python(code):
    """Translates English code into Python code."""
    doc = nlp(code)
    
    for pattern, replacement in CODE_MAP.items():
        code = re.sub(pattern, replacement, code, flags=re.IGNORECASE)
    
    return code

# Test the function
print(engli_to_python('If x is less than y, then Give x the value 10 else Print y'))