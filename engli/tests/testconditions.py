import spacy
from spacy.matcher import Matcher

# Load English tokenizer, parser, NER and Word vectors
nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

# Pattern for matching variables, for example, "x is 5"
pattern1 = [{"POS": "NOUN"}, 
           {"LEMMA": "be", "OP": "?"}, 
           {"LIKE_NUM": True}]

# Pattern for expressions like "x plus y"
pattern2 = [{"POS": "NOUN"},
            {"LOWER": {"IN": ["plus", "minus"]}},
            {"POS": "NOUN"}]

matcher.add("variable", [pattern1])
matcher.add("expression", [pattern2])
# Mapping English to Python code
english_python_map = {
    "greater than": ">",
    "less than": "<",
    "equal to": "==",
    "plus": "+",
    "minus": "-",
    "increment": " += 1",
    "decrement": " -= 1",
    "print": "print"
}

def map_english_python(phrase):
    return english_python_map.get(phrase, phrase)

def parse_conditional_statements(sentence, context):
    doc = nlp(sentence)
    
    # Process number assignments and expressions
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  
        span = doc[start:end]  

        # Checking string_id can help you determine what kind of pattern you matched 
        if string_id == 'variable':  
            var, val = span.text.split()
            context[var] = val
        
        elif string_id == 'expression':
            var1, operation, var2 = span.text.split()
            expression = f"{context.get(var1, var1)} {map_english_python(operation)} {context.get(var2, var2)}"
            context[var1] = expression # The result of the expression is assigned to the first variable

    conditional_structure = ""
    for token in doc:
        
        # Placeholder logic for identifying and structuring conditional statements
        if token.text.lower() == "if":
            conditional_structure += "if ("
        elif token.text.lower() == "then":
            conditional_structure += "):"
        elif token.text.lower() == "else":
            conditional_structure += "else:"
            
        # Replace variable assignments with python equivalents
        elif token.text in context:
            conditional_structure += context[token.text] + " "
        else:
            conditional_structure += map_english_python(token.text.lower()) + " "

    conditional_structure = conditional_structure.replace(" )", ")").replace(": ", ":\n\t")
    conditional_structure = conditional_structure.replace(".", "")
    return conditional_structure


def test_conditions():
    # Initialize context
    context = {}

    # Example usage
    sentences = [
        "x is 5. If x is greater than zero then increment x else print zero.", 
        "y is 10. If y is less than x then decrement y else print x.",
        "z is x plus y. If z is equal to 15 then print z else print y."
    ]

    for sentence in sentences:
        conditional_structure = parse_conditional_statements(sentence, context)
        print(conditional_structure)

# if (5 > zero):
#     x += 1 
# else:
#     print zero
# if (10 < 5):
#     y -= 1 
# else:
#     print x
# if (5 + 10 == 15):
#     print z 
# else:
#     print y

#python3 -m spacy download en_core_web_sm
test_conditions()