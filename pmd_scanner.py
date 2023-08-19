# h3avren

# imports
from token import Token, TokenType as tt

class Scanner:
    """"
    This class implements the scanner - the part of the code which deals
    with scanning keywords and literals from the raw code.
    """
    def __init__(self,source : str, interpreter):
        self.source = source
        self.tokens = []
        self.interpreter = interpreter

        self.start = 0
        self.current = 0
        self.line = 1
        # keywords are the reserved keywords of the language
        # listed in dictionary for quick match
        self.keywords = { "Pie" : tt.PIE,
                          "Donut" : tt.DONUT,
                          "Line" : tt.LINE,
                          "Bar" : tt.BAR,
                          "Scatter" : tt.SCATTER,
                          "strict" : tt.STRICT,
                          "graph" : tt.GRAPH,
                          "digraph" : tt.DIGRAPH,
                          "edgecolors" : tt.EDGECOLORS,
                          "alpha" : tt.ALPHA,
                          "s" : tt.S,
                          "c" : tt.C,
                          "label" : tt.LABEL,
                          "color" : tt.COLOR,
                          "width" : tt.WIDTH,
                          "edgecolor" : tt.EDGECOLOR,
                          "marker" : tt.MARKER,
                          "linestyle" : tt.LINESTYLE,
                          "explode" : tt.EXPLODE,
                          "x" : tt.X,
                          "colors" : tt.COLORS}

    def scan_tokens(self):
        while(not self.is_at_end()):
            self.start = self.start
            self.scan_token()
        self.tokens.append(Token(tt.EOF, "", None, self.line))
        return self.tokens
    
    def scan_token(self):
        char = self.advance()
        if(char == '('):
            self.addToken(tt.LEFT_PAREN)
        elif(char == ')'):
            self.addToken(tt.RIGHT_PAREN)
        elif(char == ','):
            self.addToken(tt.COMMA)
        elif(char == '.'):
            self.addToken(tt.DOT)
        elif(char == '-'):
            self.addToken(tt.MINUS)
        elif(char == '+'):
            self.addToken(tt.PLUS)
        elif(char == '='):
            self.addToken(tt.EQUAL)
        elif(char == ' ' or char == '\t' or char == '\r'):
            pass
        elif(char == '\n'):
            self.line += 1
        else:
            if(self.isdigit(char)):
                self.number()
            elif(self.isalpha(char)):
                self.identifier()
            else:
                self.interpreter.error(self.line, "Unexpected character.")
        
    def isalpha(self, char):
        return (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char == '_')

    def isdigit(self, char):
        return char >= '0' and char <= '9'
    
    def number(self):
        # consume characters until next characters are digit
        while(self.isdigit(self.peek())):
            self.advance()

        # look for a fractional part
        if(self.peek() == '.' and self.isdigit(self.peek_next())):
            self.advance() # consume the dot '.'
            while(self.isdigit(self.peek())):
                self.advance()
        self.addToken(tt.NUMBER, float(self.source[self.start : self.current]))

    def peek():
        pass