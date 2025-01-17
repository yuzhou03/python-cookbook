# example.py
#
# Example of a tokenizer

import re
from collections import namedtuple

NAME = r"(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)"
NUM = r"(?P<NUM>\d+)"
PLUS = r"(?P<PLUS>\+)"
TIMES = r"(?P<TIMES>\*)"
EQ = r"(?P<EQ>=)"
WS = r"(?P<WS>\s+)"

master_pat = re.compile("|".join([NAME, NUM, PLUS, TIMES, EQ, WS]))

Token = namedtuple("Token", ["type", "value"])


def generate_tokens(pat, text):
    """
    Generate tokens from the given text using the provided regular expression pattern.
    :param pat: The compiled regular expression pattern.
    :param text: The input text to tokenize.
    :return: A generator that yields Token namedtuples.
    """
    # Create a scanner object using the compiled pattern and the input text
    scanner = pat.scanner(text)
    # Iterate over matches found by the scanner until no more matches are found (scanner.match returns None)
    for m in iter(scanner.match, None):
        # Yield a Token namedtuple with the type (lastgroup) and value (group()) of the match
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, "foo = 42"):
    print(tok)
