import sys
import ply.lex as lex
import re
re.MULTILINE

tokens=[
    'INTNUM',
    'FLOAT',
    'IF',
    'ELSE',
    'FOR',
    'WHILE',
    'BREAK',
    'CONTINUE',
    'RETURN',
    'PRINT',
    'STRING',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    "ZEROS",
    "ONES",
    "EYE",
    "OPENING_PARANTHESIS",
    "CLOSING_PARANTHESIS",
    "OPENING_SQUARE_BRACKET",
    "CLOSING_SQUARE_BRACKET",
    "OPENING_BRACE",
    "CLOSING_BRACE",
    "COMMA",
    "DOTADD",
    'DOTSUB',
    'DOTDIV',
    'DOTMUL',
    'EQUALS',
    'LESS',
    'MORE',
    'LESSEQUAL',
    'MOREEQUAL',
    'NOTEQUAL',
    'COMPARISION',
    'ADDASSIGN',
    'SUBASSIGN',
    'MULASSIGN',
    'DIVASSIGN',
    'SEMICOLON',
    'TRANSPOSE',
    'TO',
    'COMMENT',
    "ENDLINE",
    "ID"


]
t_TO=':'
t_ADDASSIGN='\+\='
t_SUBASSIGN='\-\='
t_MULASSIGN='\*\='
t_DIVASSIGN='\/\='
t_OPENING_PARANTHESIS=r'\('
t_CLOSING_PARANTHESIS=r'\)'
t_OPENING_SQUARE_BRACKET=r'\['
t_CLOSING_SQUARE_BRACKET=r'\]'
t_OPENING_BRACE=r'\{'
t_CLOSING_BRACE=r'\}'
t_PLUS=r'\+'
t_MINUS=r'\-'
t_MULTIPLY=r'\*'
t_DIVIDE=r'\/'
t_LESS=r'<'
t_LESSEQUAL=r'<='
t_MORE=r'>'
t_MOREEQUAL=r'>='
t_NOTEQUAL=r'!='
t_COMPARISION=r'=='
t_TRANSPOSE=r"'"
t_EQUALS=r'\='
t_SEMICOLON=r';'
t_COMMA=r','
t_ignore=r' '

def t_PRINT(t):
    r'print'
    t.type="PRINT"
    return t
def t_STRING(t):
    r'"+(.)+"'
    t.type="STRING"
    return t
def t_IF(t):
    r'if'
    t.type="IF"
    return t

def t_WHILE(t):
    r'while'
    t.type="WHILE"
    return t

def t_FOR(t):
    r'for'
    t.type="FOR"
    return t

def t_ELSE(t):
    r'else'
    t.type="ELSE"
    return t

def t_BREAK(t):
    r'break'
    t.type="BREAK"
    return t

def t_CONTINUE(t):
    r'continue'
    t.type="CONTINUE"
    return t

def t_RETURN(t):
    r'return'
    t.type="RETURN"
    return t

def t_DOTADD(t):
    r'\.+\+'
    t.type="DOTADD"
    return t

def t_DOTSUB(t):
    r'\.+\-'
    t.type="DOTSUB"
    return t

def t_DOTDIV(t):
    r'\.+\/'
    t.type="DOTDIV"
    return t

def t_DOTMUL(t):
    r'\.+\*'
    t.type="DOTMUL"
    return t

def t_FLOAT(t):
    r'(\d)*\.(\d)*E(\d)*|(\d)*\.(\d)*'
    t.value=float(t.value)
    return t

def t_INTNUM(t):
    r'\d+'
    t.value=int(t.value)
    return t

def t_ZEROS(t):
    r'(zeros)'
    t.type='ZEROS'
    return t

def t_ONES(t):
    r'(ones)'
    t.type='ONES'
    return t

def t_EYE(t):
    r'(eye)'
    t.type='EYE'
    return t

def t_ID(t):
    r'[a-zA-Z_0-9]+'
    t.type= 'ID'
    return t

def t_COMMENT(t):
    r'\#+(.)+(\n)|\#+(.)*'
    lexer.lineno+=1
    pass

def t_ENDLINE(t):
    r'\n'
    lexer.lineno += 1
    pass

def t_error(t):
    print(f"Illegal character: {t}")
    t.lexer.skip(1)

lexer=lex.lex()

