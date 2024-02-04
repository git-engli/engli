codemap = {
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

    # Dictionaries
    'Create a dictionary named (\w*)': r'\1 = {}',
    'In the dictionary (\w*), set the key (\w*) with the value (\w*)': r'\1[\2] = \3',

    # Class and Object Oriented Programming
    'Create a class named (\w*)': r'class \1:\n\tdef __init__(self):\n\t\tpass',
    'In the class (\w*), create a method named (\w*) that does the following: (.*)': r'class \1:\n\tdef \2(self):\n\t\t\3',
    'Create an object named (\w*) from the class (\w*)': r'\1 = \2()',
    
    # Loops
    'Repeat (.*):': r'while True: \1',
    'until (.+):': r'while not (\1):',
    'as long as (.+):': r'while \1:',
    '(.+) times:': r'for _ in range(\1):',
    'Perform (.*) until (.*)':  r'\1\nwhile not \2:\n\t\1',
    'foreach (\w*) in (\w*), do (.*)': r'for \1 in \2: \3',
    'for each (\w*) in (\w*), do (.*)': r'for \1 in \2: \3',
    'for every (\w*) in (\w*), do (.*)': r'for \1 in \2: \3',
    'Repeat the following until (\w*) is (\w*): (.*)': r'while not \1 == \2: \3',
    'For each item in (\w*), do the following: (.*)': r'for item in \1: \2',


    # Functions
    'Define a function (\w*) that takes (\w*), and returns (.*)': r'def \1(\2): return \3',
    'Call the function (\w*) with the parameter (\w*)': r'\1(\2)',
    'Define a function named (\w*) that takes (\w*), and returns (.*)': r'def \1(\2): return \3',
    'Call the function (\w*) with the parameters (\w*)': r'\1(\2)',
    
    # Print statement
    'Print (\w*)': r'print(\1)',
}