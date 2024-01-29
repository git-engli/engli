import argparse
import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

pattern1 = [{"POS": "NOUN"}, {"LEMMA": "be", "OP": "?"}, {"LIKE_NUM": True}]
pattern2 = [{"POS": "NOUN"}, {"LOWER": {"IN": ["plus", "minus"]}}, {"POS": "NOUN"}]

matcher.add("variable", [pattern1])
matcher.add("expression", [pattern2])

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

    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  
        span = doc[start:end]  

        if string_id == 'variable':  
            var, val = span.text.split()
            context[var] = val
        
        elif string_id == 'expression':
            var1, operation, var2 = span.text.split()
            expression = f"{context.get(var1, var1)} {map_english_python(operation)} {context.get(var2, var2)}"
            context[var1] = expression 

    conditional_structure = ""
    for token in doc:
        
        if token.text.lower() == "if":
            conditional_structure += "if ("
        elif token.text.lower() == "then":
            conditional_structure += "):"
        elif token.text.lower() == "else":
            conditional_structure += "else:"
        elif token.text in context:
            conditional_structure += context[token.text] + " "
        else:
            conditional_structure += map_english_python(token.text.lower()) + " "

    conditional_structure = conditional_structure.replace(" )", ")").replace(": ", ":\n\t")
    conditional_structure = conditional_structure.replace(".", "")
    return conditional_structure

def process_sentences(args):
    context = {}
    for sentence in args.sentences:
        conditional_structure = parse_conditional_statements(sentence, context)
        print(conditional_structure)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process sentences into python code.')
    parser.add_argument('sentences', nargs="+", help='List of sentences')
    process_sentences(parser.parse_args())