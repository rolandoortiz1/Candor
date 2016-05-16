# ------------------------------------------------------------
# CandorLex.py
#
# Simple lexical analyzer to identify and tokenize the various
# parts of our language structure.
# ------------------------------------------------------------


# ------------------------------------------------------------
# PLY import that contructs our lexical analyzer with the
# written rules.
# ------------------------------------------------------------
import ply.lex as lex

# ------------------------------------------------------------
# Reserved words that served a specific purpose in the
# programing language
# ------------------------------------------------------------
reserved = {'add': 'ADD', 'subtract': 'SUBTRACT', 'times': 'TIMES',
            'divides': 'DIVIDES', 'while' : 'WHILE','for' : 'FOR',
            'if' : 'IF', 'else' : 'ELSE', 'equals' : 'EQUALS',
            'print' : 'PRINT', 's' : 'ATTRIBUTE', 'greaterThan' : 'GREATERTHAN',
            'lessThan' : 'LESSTHAN', 'sameAs' : 'EXACT', 'end' : 'END',
            'between' : 'BETWEEN', 'endBlock' : 'ENDBLOCK', 'and' : 'AND'}

# ------------------------------------------------------------
# List of token names. This are for general purpose use.
# ------------------------------------------------------------
tokens = [
   'NUMBER',
   'LPAREN',
   'RPAREN',
   'ID',
]  + list(reserved.values())

# ------------------------------------------------------------
# Regular expression rules for simple parenthesis tokens.
# ------------------------------------------------------------

t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# ------------------------------------------------------------
# A regular expression rule for numbers.
# ------------------------------------------------------------
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# ------------------------------------------------------------
# Regular expression rule for word not in the reserved array.
# ------------------------------------------------------------
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID') 
    return t

# ------------------------------------------------------------
# Regular expression rule for tracking line numbers.
# ------------------------------------------------------------
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ------------------------------------------------------------
# A string containing ignored characters (spaces and tabs)
# ------------------------------------------------------------
t_ignore  = ' \t'

# ------------------------------------------------------------
# Code to lower case all reserved words.
# ------------------------------------------------------------
reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

# ------------------------------------------------------------
# Regular expression rule for error handling.
# ------------------------------------------------------------
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# ------------------------------------------------------------
# Build the lexer
# ------------------------------------------------------------
lexer = lex.lex()
