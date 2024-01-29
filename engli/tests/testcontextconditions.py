import spacy

# Load English tokenizer, parser, NER and Word vectors
nlp = spacy.load('en_core_web_sm')

# Define a mapping from English phrases to Python code
english_to_python = {
    "it rains": "weather=='rain'", 
    "take an umbrella": "umbrella = True",
    "enjoy the walk": "umbrella = False",
    "it is hot": "temperature > 35",
    "take a water bottle": "drink = 'water'",
    "take a jacket": "clothing = 'jacket'"
}

# Initialize variables that might be used
context = { 
    "weather": "'rain'", # default weather condition
    "temperature": "35", # default temperature
    "umbrella": "False", # default umbrella status
    "drink": "'None'", # default drink
    "clothing" : "'None'" # default clothing
}

def parse_conditional_statements(sentence):
    doc = nlp(sentence)
    conditional_structure = ""
    for token in doc:
        if token.text.lower() == "if":
            conditional_structure += "if ("
        elif token.text.lower() == "then":
            conditional_structure += "):"
        elif token.text.lower() == "else":
            conditional_structure += "else:"
        else:
            if english_to_python.get(token.text):
                    conditional_structure += english_to_python.get(token.text) + " "
            else:
                    conditional_structure += token.text + " "

    conditional_structure = conditional_structure.replace(" )", ")").replace(": ", ":\n\t")
    conditional_structure = conditional_structure.replace(".", "")
    return conditional_structure

def test_conditions1():
    # Example usage
    sentences = ["If it rains then take an umbrella else enjoy the walk.", 
                "If it is hot then take a water bottle else take a jacket."]

    for sentence in sentences:
        # Concatenate Python variables declarations
        py_variables = '\n'.join([f"{var} = {val}" for var, val in context.items()])
        conditional_structure = parse_conditional_statements(sentence)
        print(py_variables)
        print(conditional_structure)


# weather = 'rain'
# temperature = 35
# umbrella = False
# drink = 'None'
# clothing = 'None'
# if (weather=='rain'):
# 	umbrella = True
# else:
# 	umbrella = False
# weather = 'rain'
# temperature = 35
# umbrella = False
# drink = 'None'
# clothing = 'None'
# if (temperature > 35):
# 	drink = 'water'
# else:
# 	clothing = 'jacket'

test_conditions1()