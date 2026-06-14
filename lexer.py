import ply.lex as lex
import sys


keywords = {
    'zmienna': 'ZMIENNA',
    'wyświetl': 'WYSWIETL',
    'prawda': 'PRAWDA',
    'fałsz': 'FALSZ',       
    'i': 'I',
    'lub': 'LUB',
    'nie': 'NIE',
    'jeżeli': 'JEZELI',
    'inaczej': 'INACZEJ',
    'dopóki': 'DOPOKI',
    'pobierz': 'POBIERZ',
}

tokens = [
    'ID',
    'LICZBA',
    'PLUS',
    'MINUS',
    'RAZY',
    'PODZIEL',
    'ROWNA_SIE',
    'SREDNIK',
    'LNAWIAS',
    'PNAWIAS',
    'LKLAMRA',
    'PKLAMRA',
    'MNIEJSZE',
    'WIEKSZE',
    'MNIEJSZE_ROWNE',
    'WIEKSZE_ROWNE',
    'ROWNE',
    'NIEROWNE',
] + list(keywords.values())


def t_KOMENTARZ_WIELOLINIOWY(t):
    r'\#\#\#(.|\n)*?\#\#\#'
    t.lexer.lineno += t.value.count('\n')

def t_KOMENTARZ_JEDNOLINIOWY(t):
    r'\#[^\n]*'

def t_MNIEJSZE_ROWNE(t):
    r'<='
    return t

def t_WIEKSZE_ROWNE(t):
    r'>='
    return t

def t_ROWNE(t):
    r'=='
    return t

def t_NIEROWNE(t):
    r'!='
    return t


t_PLUS = r'\+'
t_MINUS = r'-'
t_RAZY = r'\*'
t_PODZIEL = r'\/'
t_ROWNA_SIE = r'='
t_SREDNIK = r';'
t_LNAWIAS= r'\('
t_PNAWIAS = r'\)'
t_LKLAMRA = r'\{'
t_PKLAMRA = r'\}'
t_MNIEJSZE = r'<'
t_WIEKSZE = r'>'

def t_LICZBA(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ_][a-zA-Z0-9ąćęłńóśźżĄĆĘŁŃÓŚŹŻ_]*'
    t.type = keywords.get(t.value, 'ID')
    return t


t_ignore = ' \t'

def t_nowalinia(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Błąd leksykalny: nieznany znak '{t.value[0]}' w linii {t.lexer.lineno}")
    sys.exit(1)


lexer = lex.lex()