import AST
import ply.yacc as yacc
from scanner import tokens


precedence = (
   ("left", 'PLUS', 'MINUS'),
   ("left", 'MULTIPLY', 'DIVIDE'),
   ("left", 'DOTADD', 'DOTSUB'),
   ("left", 'DOTMUL', 'DOTDIV'),
)

def p_program(p):
    '''
    program : lines_opt
    '''
    p[0]=p[1]

def p_lines_opt(p):
    '''
    lines_opt : lines
    '''
    p[0]=AST.LinesOpt(p[1])

def p_lines_opt2(p):
    '''
    lines_opt :
    '''
    p[0] = AST.LinesOpt()
def p_lines(p):
    '''
    lines : lines line
    '''
    p[0] = p[1]
    p[0].append(p[2])
def p_lines2(p):
    '''
    lines : line
    '''
    p[0]=AST.Lines(p[1])
def p_line(p):
    '''
    line : expression SEMICOLON COMMENT
         | var_assign SEMICOLON COMMENT
         | var_op_assign SEMICOLON COMMENT
         | var_tuple SEMICOLON COMMENT
         | for COMMENT
         | if COMMENT
         | while COMMENT
         | else COMMENT
         | print COMMENT
         | return SEMICOLON COMMENT
         | break SEMICOLON COMMENT
         | continue SEMICOLON COMMENT
         | expression SEMICOLON
         | var_assign SEMICOLON
         | var_op_assign SEMICOLON
         | var_tuple SEMICOLON
         | for
         | if
         | while
         | else
         | print
         | return SEMICOLON
         | break SEMICOLON
         | continue SEMICOLON
    '''
    p[0]=(p[1])

def p_return(p):
    '''
    return : RETURN expression
           | RETURN
    '''
    p[0]=[p[1], p[2]]

def p_continue(p):
    '''
    continue : CONTINUE
    '''
    p[0]=p[1]

def p_break(p):
    '''
    break : BREAK
    '''
    p[0]=p[1]


def p_for(p):
    '''
    for : FOR for_helper  EQUALS for_helper TO for_helper OPENING_BRACE program CLOSING_BRACE
        | FOR for_helper  EQUALS for_helper TO for_helper
    '''
    p[0]= [p[1], 'from', p[2] , p[3] ,p[4], 'to', p[6]]

def p_for_helper(p):
    '''
    for_helper : ID
               | INTNUM
    '''
    p[0]=p[1]

def p_if(p):
    '''
    if : IF OPENING_PARANTHESIS condition CLOSING_PARANTHESIS
       | IF OPENING_PARANTHESIS condition CLOSING_PARANTHESIS OPENING_BRACE program CLOSING_BRACE
    '''
    p[0]= [p[1], p[3], 'then']

def p_while(p):
    '''
    while : WHILE OPENING_PARANTHESIS condition CLOSING_PARANTHESIS
          | WHILE OPENING_PARANTHESIS condition CLOSING_PARANTHESIS OPENING_BRACE program CLOSING_BRACE
    '''
    p[0]= [p[1], p[3], 'then']

def p_else(p):
    '''
    else : ELSE
         | OPENING_BRACE program CLOSING_BRACE
    '''
    p[0]= p[1]

def p_condition(p):
    '''
    condition : var_in_cond LESSEQUAL var_in_cond
              | var_in_cond LESS var_in_cond
              | var_in_cond MOREEQUAL var_in_cond
              | var_in_cond MORE var_in_cond
              | var_in_cond COMPARISION var_in_cond
              | var_in_cond NOTEQUAL var_in_cond
    '''
    p[0]= [p[1], p[3], p[2]]

def p_var_in_cond(p):
    '''
    var_in_cond : expression
    '''
    p[0]=p[1]
def p_array(p):
    '''
    expression : OPENING_SQUARE_BRACKET row
    '''
    p[0]=p[2]

def p_row(p):
    '''
    row : expression COMMA row
        | expression SEMICOLON row
        | expression CLOSING_SQUARE_BRACKET
    '''
    p[0]=[p[2]]

def p_var_tuple(p):
    '''
    var_tuple : ID OPENING_SQUARE_BRACKET tuple
    '''
    p[0]=p[1]

def p_tuple(p):
    '''
    tuple : INTNUM COMMA tuple
          | INTNUM CLOSING_SQUARE_BRACKET
    '''
    p[0]=p[1]

def p_var_assign(p):
    '''
    var_assign : ID EQUALS expression
               | var_tuple EQUALS expression
    '''
    p[0]=('=', p[1], p[3])

def p_op_assign(p):
    '''
    var_op_assign : ID MULASSIGN expression
    var_op_assign : ID DIVASSIGN expression
    var_op_assign : ID ADDASSIGN expression
    var_op_assign : ID SUBASSIGN expression
    '''
    p[0]=(p[2], p[1], p[3])

def p_neg_expression(p):
    '''
    expression : MINUS expression
    '''
    p[0]=('unary', p[2])

def p_transpose_expression(p):
    '''
    expression : expression TRANSPOSE
    '''
    p[0]=(p[1], p[2])

def p_expression(p):
    '''
    expression : expression DOTMUL expression
               | expression DOTDIV expression
               | expression DOTADD expression
               | expression DOTSUB expression
               | expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
    '''
    p[0] = (p[2], p[1], p[3])


def p_matrix_function(p):
    '''
    expression : ZEROS OPENING_PARANTHESIS expression CLOSING_PARANTHESIS
                    | ONES OPENING_PARANTHESIS expression CLOSING_PARANTHESIS
                    | EYE OPENING_PARANTHESIS expression CLOSING_PARANTHESIS
    '''
    p[0] = (p[1], p[3])

def p_expression_int_float(p):
    '''
    expression : INTNUM
               | FLOAT
    '''
    p[0]=('num',p[1])

def p_expression_var(p):
    '''
    expression : ID
    '''
    p[0]=('var', p[1])

def p_print(p):
    '''
    print : PRINT print_vars SEMICOLON
          | PRINT STRING SEMICOLON
    '''
    p[0]=[p[1], p[2]]

def p_print_vars(p):
    '''
    print_vars : expression COMMA print_vars
               | expression
    '''
    p[0]=p[1]
def p_empty(p):
    '''
    empty :
    '''
    p[0]=None

def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")



parser = yacc.yacc()