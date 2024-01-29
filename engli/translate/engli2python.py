import spacy
import re
import argparse


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


FUNCTION_MAP = {
    # Defining function to calculate average
    "calculate average": r'''def calculate_average(numbers):
    return sum(numbers) / len(numbers)''',

    # Download file from url
    "download file": r'''
import requests
def download_file(url):
    response = requests.get(url)
    with open('file', 'wb') as f:
        f.write(response.content)''',

    # Extract text from a file
    "extract text": r'''
def extract_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text''',

    # Sort a list
    "sort list": r'''
def sort_list(lst):
    return sorted(lst)''',

    # Validate user credentials
    "validate user": r'''
def validate_user(username, password):
    if username in database and database[username] == password:
        return True
    else:
        return False''',

    # Send an email
    "send email": r'''
import smtplib
def send_email(sender, recipient, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, "password")
    message = 'Subject: {}\n\n{}'.format(subject, body)
    server.sendmail(sender, recipient, message)
    server.quit()''',

    # Fetch data from a database
    "fetch data": r'''
import sqlite3
def fetch_data(query):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data''',

    # Update a record in a database
    "update record": r'''
def update_record(id, new_info):
    conn = sqlite3.connect('my_database.db')
    conn.execute("UPDATE my_table SET info = ? WHERE id = ?", (new_info, id))
    conn.commit()
    conn.close()'''
}

def engli_to_python(code):
    """Translates English code into Python code."""
    doc = nlp(code)
    
    for pattern, replacement in CODE_MAP.items():
        code = re.sub(pattern, replacement, code, flags=re.IGNORECASE)
    
    return code


def process_input(args):
    code = english_to_python(args.sentence)
    print(code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translate English to Python')
    parser.add_argument('sentence', type=str, help='English sentence to translate')
    process_input(parser.parse_args())


