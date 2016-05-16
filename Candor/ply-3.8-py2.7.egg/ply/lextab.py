# lextab.py. This file automatically created by PLY (version 3.8). Don't edit!
_tabversion   = '3.8'
_lextokens    = set(['ADD', 'RPAREN', 'FOR', 'NUMBER', 'ATTRIBUTE', 'EQUALS', 'ELSE', 'WHILE', 'DIVIDES', 'LPAREN', 'PRINT', 'TIMES', 'SUBTRACT', 'ID', 'IF'])
_lexreflags   = 0
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_NUMBER>\\d+)|(?P<t_ID>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<t_newline>\\n+)|(?P<t_LPAREN>\\()|(?P<t_RPAREN>\\))', [None, ('t_NUMBER', 'NUMBER'), ('t_ID', 'ID'), ('t_newline', 'newline'), (None, 'LPAREN'), (None, 'RPAREN')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
