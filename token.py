# h3avren

# imports
from enum import Enum

class TokenType(Enum):
    # single character token
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    COMMA = 3
    DOT = 4
    MINUS = 5
    PLUS = 6
    EQUAL = 7

    # Shape keywords
    PIE = 8
    DONUT = 9
    LINE = 10
    BAR = 11
    SCATTER = 13
    STRICT = 14
    GRAPH = 15
    DIGRAPH = 16

    # attribute names
    EDGECOLORS =17
    EDGECOLOR = 18
    C = 19
    COLOR = 20
    COLORS = 21
    S = 22
    X = 23
    ALPHA = 24
    LABEL = 25
    WIDTH = 26
    MARKER = 27
    LINESTYLE = 28
    EXPLODE = 29

    # Literals
    IDENTIFIER = 30
    NUMBER = 31

    EOF = 32
    

class Token:
    def __init__(self, type : TokenType, lexeme : str, literal, line : int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return "%s %s %s" % (self.type, self. lexeme, self.literal)

    def __repr__(self):
        args = f'{self.type}, {self.lexeme}, {self.literal}, {self.line}'
        return f'{self.__class__.__name__}({args})'