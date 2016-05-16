# ------------------------------------------------------------
# CandorParser.py
#
# Simple syntax analyzer to identify expressions and output 
# the intermediate code to an output python file.
# ------------------------------------------------------------

# ------------------------------------------------------------
# PLY import that creates our syntax analyzer, including the
# rule tables using the rules we specify.
# ------------------------------------------------------------
import ply.yacc as yacc

# ------------------------------------------------------------
# Import to enable to closing of the syntax analyzer's
# function.
# ------------------------------------------------------------
import sys

# ------------------------------------------------------------
# Import that gives us the tokens produced with each line of
# code.
# ------------------------------------------------------------
from CandorLex import tokens

# ------------------------------------------------------------
# Dictionary to hold tuples to simplify our computation of
# the output file.
# ------------------------------------------------------------
names = {}
# ------------------------------------------------------------
# Integer that would keep track of how many tabs are need
# in the file before the intermediate code is produced.
# ------------------------------------------------------------
indents = 0

# ------------------------------------------------------------
# File where our intermediate code will be produced.
# ------------------------------------------------------------
f = open('C:\\Users\\Victor\\Documents\\test.py','w')

# ------------------------------------------------------------
# Mathematical Operations of the programming language
# produced into intermediate code.
# ------------------------------------------------------------
def p_expression_add(p):
            'expression : expression ADD term'
            indent()
            f.write(str(p[1]) + " + " + str(p[3]) + "\n")
            print ("p_expression_add")

def p_expression_subtract(p):
            'expression : expression SUBTRACT term'
            indent()
            f.write(str(p[1]) + " - " + str(p[3]) + "\n")
            print ("p_expression_subtract")

def p_expression_times(p):
            'expression : expression TIMES term'
            indent()
            f.write(str(p[1]) + " * " + str(p[3]) + "\n")
            print ("p_expression_times")

def p_expression_divide(p):
            'expression : expression DIVIDES term'
            indent()
            f.write(str(p[1]) + " / " + str(p[3]) + "\n")
            print ("p_expression_divide")

def p_expression_equals(p):
        'expression : ID EQUALS expression'
        indent()
        f.write(str(p[1]) + " = " + str(p[3]) + "\n")
        print ("p_expression_equals")

# ------------------------------------------------------------
# Expression rule to output intermediate code of attributes.
# ------------------------------------------------------------
def p_expression_attributes(p):
            'expression : ID ATTRIBUTE ID EQUALS term'
            f.write(str(p[1]) + "." + str(p[3]) +" = "+ str(p[5]) + "\n")

# ------------------------------------------------------------
# Expression rule to output intermediate code of prints.
# ------------------------------------------------------------
def p_expression_print(p):
            'expression : PRINT factor'
            f.write(str(p[1]) +" "+ str(p[2]) + "\n")
# ------------------------------------------------------------
# Expression rules that convert the input of other rules.
# ------------------------------------------------------------
def p_term_ID(p):
            'term : ID'
        #    p[0] = variable_check(p[1])
            p[0] = p[1]
            print ("p_expression_ID")
        #    print (variable_check(p[1]))

def p_expression_term(p):
            'expression : term'
            p[0] = p[1]
            print ("p_expression_term")

def p_term_factor(p):
            'term : factor'
            p[0] = p[1]
            print ("p_term_factor")

def p_factor_num(p):
            'factor : NUMBER'
            p[0] = p[1]
            print ("p_term_num")

def p_factor_expr(p):
            'factor : LPAREN expression RPAREN'
            p[0] = p[2]
            print ("p_factor_expr")

# ------------------------------------------------------------
# Expression to output intermediate code of if/else
# statements.
# ------------------------------------------------------------
def p_condition_if(p):
            'condition : IF'
            p[0] = p[1]

def p_condition_else(p):
            'condition : ELSE'
            p[0] = p[1]

# ------------------------------------------------------------
# Expression to output intermediate code of while loops.
# ------------------------------------------------------------
def p_condition_while(p):
            'condition : WHILE'
            p[0] = p[1]

# ------------------------------------------------------------
# Expressions to output intermediate code of mathematical
# comparisons.
# ------------------------------------------------------------
def p_condition_gt(p):
            'expression : condition term GREATERTHAN term'
            indent()
            f.write(str(p[1])+" "+str(p[2])+" >= "+str(p[4])+" :"+ "\n")
            global indents
            indents= indents + 1

def p_condition_lt(p):
            'expression : condition term LESSTHAN term'
            indent()
            f.write(str(p[1])+" "+str(p[2])+" <= "+str(p[4])+" :"+ "\n")
            global indents
            indents = indents +1

def p_condition_sa(p):
            'expression : condition term EXACT term'
            indent()
            f.write(str(p[1])+" "+str(p[2])+" == "+str(p[4])+" :"+ "\n")
            global indents
            indents = indents + 1
            
# ------------------------------------------------------------
# Expression to output intermediate code of for loops.
# ------------------------------------------------------------
def p_for(p):
            'expression : FOR ID BETWEEN term AND term'
            indent()
            global indents
            indents = indents + 1
            f.write("for "+str(p[2])+" in range("+str(p[4])+","+str(p[6])+") :" + "\n")

# ------------------------------------------------------------
# Expression to change the number of indents of the next line
# of code.
# ------------------------------------------------------------
def p_endblock(p):
            'expression : ENDBLOCK'
            p[0] = p[1]
            global indents
            indents = indents - 1

# ------------------------------------------------------------
# Expression to end the operations of the syntax analyzer.
# ------------------------------------------------------------
def p_expression_end(p):
            'expression : END'
            f.close()
            sys.exit()

# ------------------------------------------------------------
# Helper methods to output intermediate code.
# ------------------------------------------------------------
def indent ():
    global indents
    for i in range(0, indents):
        f.write("\t")
            
def variable_check (id):
            if names[id]:
                return names[id]
            print ("Variable " + id + " does not exist.")
            
# ------------------------------------------------------------
# Expression for error handling.
# ------------------------------------------------------------
def p_error(p):
            print("Syntax error in input!")

# ------------------------------------------------------------
# Build the parser.
# ------------------------------------------------------------
parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)



