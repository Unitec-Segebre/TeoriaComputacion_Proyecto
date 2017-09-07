from lexer import getNextToken, setInput
from tokens import Token_ENUM
from ast import *

token = None

def parse(text):
    setInput(text)
    global token
    token = getNextToken()
    return E()
    if token.token_id != Token_ENUM.TK_EOF:
        raise ValueError("Input not parsed entirely.")

def E():
    t = T()
    return E_prime(t)

def E_prime(var):
    global token
    if token.token_id == Token_ENUM.OP_OR :
        token = getNextToken()
        t = T()
        or_st = Or(var, t)
        return E_prime(or_st)
    else:
        #epsilon
        return var

def T():
    f = F()
    return T_prime(f)

def T_prime(var):
    global token
    if token.token_id == Token_ENUM.OP_CONCAT :
        token = getNextToken()
        f = F()
        concat_st = Concat(var, f)
        return T_prime(concat_st)
    else:
        #epsilon
        return var


def F():
    global token
    if token.token_id == Token_ENUM.TK_LEFT_PAR :
        token = getNextToken()
        e = E()
        if token.token_id != Token_ENUM.TK_RIGHT_PAR:
            raise ValueError("Expecting right parenthesis ')', but found ", token.lexema)
        token = getNextToken()
        return F_prime(e)
    else:
        r = R()
        return F_prime(r)

def F_prime(var):
    global token
    if token.token_id == Token_ENUM.OP_KLEENE:
        token = getNextToken()
        kleene = Kleene(var)
        return F_prime(kleene)
    else:
        #epsilon
        return var

def R():
    global token
    if token.token_id != Token_ENUM.TK_DIGIT and token.token_id != Token_ENUM.TK_LETTER :
        raise ValueError("Expecting a letter or digit, but found ", token.lexema, token.token_id)
    if token.token_id == Token_ENUM.TK_DIGIT:
        digit = Digit(int(token.lexema))
        token =  getNextToken()
        return digit
    elif token.token_id == Token_ENUM.TK_LETTER:
        letter = Letter(token.lexema)
        token =  getNextToken()
        return letter
