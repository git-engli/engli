# Engli

Engli is a free and open-source programming language developed and maintained by Predict Expert AI. It is a verbose syntactical superset of Python, and adds english-like syntax to the language. 
It included a dictionary of 3000 most used english words, as extension of Oxford 3000.

# Generator for prime numbers

```python
def primes():
    x = 1
    while True:
        was_divided = False
        x += 1
        for y in xrange(2, x):
            if x % y == 0:
                was_divided = True
        
        if not was_divided:
            yield x
```

### Engli


## Conditions

"x is 5. If x is greater than zero then increment x else print zero.", 
"y is 10. If y is less than x then decrement y else print x.",
"z is x plus y. If z is equal to 15 then print z else print y."

```python
cd translate && python3 conditions.py "x is 5. If x is greater than zero then increment x else print zero." "y is 10. If y is less than x then decrement y else print x." "z is x plus y. If z is equal to 15 then print z else print y."
```

# Context Conditions

 "If it rains then take an umbrella else enjoy the walk."
"If it is hot then take a water bottle else take a jacket."

```python
cd translate && python3 contextconditions.py "If it rains then take an umbrella else enjoy the walk." "If it is hot then take a water bottle else take a jacket."
```


## Translation

If x is less than y, then Give x the value 10 else Print y

```python
cd translate && python3 engli2python.py "Define a function add that takes x, and returns x plus 5"
```

```python
cd translate && python3 engli2python.py "Predict diabetes risk"
```
```python
cd translate && python3 engli2python.py "make a web app for automatic plant disease detection"
```
```python
cd translate && python3 engli2python.py "create web app with rest api to analyse stocks from custom formulas"
```

## Suggestions

```python
cd translate && python3 suggestions.py 
```



## Tests
```python
cd tests && python3 testconditions.py
```

```python
cd tests && python3 testcontextconditions.py
```
```python
cd tests && python3 testengli2python.py
```


# Usage
#### Loops
| Engli | Python Equivalent |
|:-------:|:-------------------:|
| ```until password is equal to '123':```|```while password != '123':```|
|```as long as user.is_connected(): ```| ```while user.is_connected():```|
|```10 times: print "Hello"```|``` for _ in xrange(10): print "Hello"```|
|```for each user in group: print user.age```| ```for user in group: print user.age```
|```for every user in group: print user.name```| ```for user in group: print user.name```
|```foreach user in group: print user.address```| ```for user in group: print user.address```

#### Comparisons
| Engli | Python Equivalent |
|:-------:|:-------------------:|
| ```if a is equal to b:```|```if a == b:```|
| ```if a is not equal to b:```|```if a != b:```|
| ```if a is greater than or equal to b:```|```if a >= b:```|
| ```if a is greater than or equal to b:```|```if a > b:```|
| ```if a is less than or equal to b:```|```if a <= b:```|
| ```if a is less than b:```|```if a < b:```|
| ```if a is between b and c:```|```if b <= a <= c:```|

#### Unit Testing
| Engli | Python Equivalent |
|:-------:|:-------------------:|
| ```assert that user.is_connected()```|```self.assertTrue(user.is_connected())```|
| ```user.name should be "Dan"```|```assert user.name == "Dan"```|
| ```user.name should not be "Daniel"```|```assert user.name != "Daniel"```|
| ```assert that sock.connect raises socket.error```|```self.assertRaises(sock.connect, socket.error)```|
| ```assert raises NotImplementedError: a = AbstractClass()```|```with self.assertRaises(NotImplementedError): a = AbstractClass()```|
|```name should be equal to get_admin_name()```| ```assert name == get_admin_name()```|
|```connection should be CLOSED```|```assert connection is CLOSED```|
|```file_content should not be equal to "Engli v0.1"```|```assert file_content != "Engli v0.1"```|
|```user_number should be greater than or equal to 6```|```assert user_number >= 6```|


Assignment Patterns
This script supports specific styles of assignments in English:

"X the value Y", which will be translated to "X = Y"

Comparison patterns
This script supports specific styles of comparison in English:

X is less than Y
X is less than or equal to Y
X is not equal to Y
X is equal to Y
X is greater than Y
X is greater than or equal to Y
X is between Y and Z
The above formats are translated to their respective comparison operators in Python.

Control Flow
This script supports a specific style of an if-else statement in English:

If condition, then action else alternative action

Loops
This script has support for specific styles of loops and iteration in English which includes:

Repeat
Until
Perform
Foreach X in Y, do Z

Function
This script supports specific styles of function definitions and function calls in English:

Define a function
Call the function

Print Statement
This script supports a specific style of the print statement in English:

Print object

# Semi-Pythonic

```python
def primes():
    for every prime x:
        yield x
```

```python
def primes():
    yield every natural x if there is no y from 2 to x where x is divided by y
```

```python
def primes():
    yield x for every number x from 1 to inifinity if there is no number y from 2 to x  where x divides y
```

Some of Engli's important features as we keep in mind are
  - 100% full backwards compatability with python.
  - Easy to use and intuitive.
  - English syntax
  - Strong tests for easy refactoring
  - Hard-coded knowledge base

# Supports:
  * Unittests
  * Comparisons
  * Loops

# Future Support:
 * ~~Unittests~~
  * ~~Comparisons~~
  * ~~Loops~~
 * ~~Conditions~~
 * Exit codes
 * Strong typing 
 * File I/O
 * Socket I/O
 * Threading
 * Waits (Explicit, Conditions, Implicit)
 * Math
 * Logging
 * Dates
 * [Strangle](http://www.github.com/d-kiss/strangle)
 * Abstract classing
 * Interfaces
 * Equation Return value
 * Switch-case
 * Elegant Hex Usage
 * Event-based programming
 * [Monoikers](http://www.yegor256.com/2017/05/16/monikers.html)
 * Then-Success-Failure angular-like promise
 * Engli ignore
 * Recursive walking through directories





Engli translates English sentences into Python code, supporting variable assignments, arithmetic operations (addition and subtraction), and conditional statements. It uses SpaCy's NLP capabilities along with a Matcher to parse the sentences and a dictionary mapping to translate from English to Python code.

```sh
#test_conditions() function:
import spacy
from spacy.matcher import Matcher
from .tests.testconditions.testconditions import test_conditions
# Run test cases
test_conditions()

```

Program Flow
The primary function in this program, parse_conditional_statements, parses a sentence into Python code. It uses the matcher object to find sentences that contain numeric assignments or arithmetic expressions. These are respectively matched using pattern1 and pattern2.

Once a match is found, it is handled based on its type:

If a numeric assignment is found ("variable" pattern), the function adds a variable to the context dictionary, setting the assigned number as its value.
If an arithmetic expression is found ("expression" pattern), the function converts it into Python code and assigns the result to the first variable in the expression.
The parse_conditional_statements function also builds a Python conditional structure with proper Python syntax using the if, then, else English keywords.

The test_conditions() function demonstrates the capabilities of the program. It initializes the context dictionary and defines a set of sentences to parse.

Optimization Suggestions
Here are some suggestions for optimizing this program:

Expand the dictionary map: The english_python_map dictionary only includes a few basic English phrases and arithmetic operators. To handle more complex sentences, you could expand this map.

Use more spacy attributes: Spacy's Token class provides various attributes to differentiate elements of a sentence. You could use these attributes to improve the parsing and translation logic.

Add a punctuation stripper: The script currently removes only periods. Adding a feature to remove all irrelevant punctuation could improve the parsing.

Create more Matcher patterns: The script currently only handles a few patterns for detecting numbers and mathematical expressions. Including more patterns could make the code much more robust.

Add error and exception handling: Implementing error handling could make the script more robust and stable, resulting in less unpredictable behavior.

Frequently Asked Questions
How can I add more phrases to the translation map? You can add more key-value pairs to the english_python_map dictionary, with English phrases as keys and equivalent Python code as values.

What types of sentences can this script translate? Currently, the script can handle sentences that assign a number to a variable, perform an addition or subtraction operation, or contain an if-then-else structure.

How can I test my sentences? You can modify the list of sentences inside the test_conditions() function.

What if my sentence contains a phrase that isn't in the english_python_map? If the script encounters a phrase that it can't find in the map, it will use the original phrase from the sentence.



function test_conditions1().


from .translate.translate_conditions2 import test_conditions1
import spacy

# Run test cases
test_conditions1()


Program Flow
The main function parse_conditional_statements handles the parsing of English sentences to Python code. It utilizes the maps defined by english_to_python and context. It iterates through each token (word) in the sentence, looks up appropriate Python code from the maps, and constructs a Python conditional statement.

These conditional statements are formed in the following manner:

The word "if" starts a conditional statement and is followed by the condition, taken from english_to_python.
The word "then" is the separator between condition and consequence action.
The word "else" separates the action for 'if' clause from action when 'if' condition is not met.
The function test_conditions1 initializes the predefined context and loops over sample sentences. It uses parse_conditional_statements to translate them into Python conditional statements.

Optimizing the Program
The script could be optimized in the following ways:

Expand the dictionary mappings: The script currently works with a limited set of hardcoded English phrases and Python code. It could be expanded to accept a wider array of language constructs.

Globalize context: The context dictionary could be used globally rather than being initialized within the testing function.

Use classes and objects: To make better use of memory, we can organize the various components of the program into classes and methods.

Implement exception handling: In the functions that perform NLP operations, we could add try/except blocks to catch and handle exceptions.

Add more types of sentences: The current program mainly handles conditional sentences. By expanding the model to include other types of sentences, we can make it more robust.

Refactor variables initialization in test_cases1 function: Currently, we are repeating the initialization of variables for every sentence, which is not optimal. We could refactor this.

# FAQs
How do I add more phrases to be translated?

You can add more phrases to the map.py or engli2python.py or in contextconditions in engli_to_python dictionary, with the English phrase as the key and the equivalent Python code as the value.
Can I customize the starting context?

Yes, the context dictionary in the test_conditions1 function can be modified to set the initial values of each variable to desired states.
Can I test my own sentences?

Yes, you can modify the sentences list in the test_conditions1 function to include your test sentences.
What other words can be used besides 'if', 'then' and 'else'?

You can add more keywords to the conditional flow within the parse_conditional_statements function. Once added, the mappings need to be handled accordingly.
