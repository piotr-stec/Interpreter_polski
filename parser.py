import ply.yacc as yacc
import sys

from lexer import tokens  
from ast_tree import (
    Dopoki,
    Program,
    Liczba,
    Przypisanie,
    ZmiennaReferencja,
    OperacjaBinarna,
    Operacja,
    Deklaracja,
    Wyswietl,
    Jezeli,
    Pobierz,
)


precedence = (
    ('left', 'LUB'),
    ('left', 'I'),
    ('right', 'NIE'),
    ('left', 'ROWNE', 'NIEROWNE'),
    ('left', 'MNIEJSZE', 'WIEKSZE', 'MNIEJSZE_ROWNE', 'WIEKSZE_ROWNE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'RAZY', 'PODZIEL'),
    ('right', 'UJEMNE')
)


def p_program(p):
    'program : instrukcje'
    p[0] = Program(p[1])

def p_wiele_instrukcji(p):
    'instrukcje : instrukcje instrukcja'
    p[0] = p[1] + [p[2]]

def p_jedna_instrukcja(p):
    'instrukcje : instrukcja'
    p[0] = [p[1]]

def p_instrukcja_deklaracja(p):
    'instrukcja : deklaracja'
    p[0] = p[1]

def p_instrukcja_wyswietlenie(p):
    'instrukcja : wyswietlenie'
    p[0] = p[1]

def p_instrukcja_pobierz(p):
    'instrukcja : pobierz'
    p[0] = p[1]

def p_instrukcja_jezeli(p):
    'instrukcja : JEZELI LNAWIAS wyrazenie PNAWIAS LKLAMRA instrukcje PKLAMRA INACZEJ LKLAMRA instrukcje PKLAMRA'
    p[0] = Jezeli(warunek=p[3], wtedy=p[6], inaczej=p[10], linia=p.lineno(1))

def p_instrukcja_jezeli_bez_inaczej(p):
    'instrukcja : JEZELI LNAWIAS wyrazenie PNAWIAS LKLAMRA instrukcje PKLAMRA'
    p[0] = Jezeli(warunek=p[3], wtedy=p[6], inaczej=None, linia=p.lineno(1))


def p_instrukcja_dopoki(p):
    'instrukcja : DOPOKI LNAWIAS wyrazenie PNAWIAS LKLAMRA instrukcje PKLAMRA'
    p[0] = Dopoki(warunek=p[3], instrukcje=p[6], linia=p.lineno(1))

def p_przypisanie_wyrazenia(p):
    'instrukcja : ID ROWNA_SIE wyrazenie SREDNIK'
    p[0] = Przypisanie(nazwa=p[1], wartosc=p[3], linia=p.lineno(1))


# Deklaracja
def p_deklaracja_z_inicjalizacja(p):
    'deklaracja : ZMIENNA ID ROWNA_SIE wyrazenie SREDNIK'
    p[0] = Deklaracja(nazwa=p[2], wartosc=p[4], linia=p.lineno(1))


def p_deklaracja_bez_inicjalizacji(p):
    'deklaracja : ZMIENNA ID SREDNIK'
    p[0] = Deklaracja(nazwa=p[2], wartosc=None, linia=p.lineno(1))


# Wyświetlanie/wczytywanie
def p_wyswietlenie_wyrazenia(p):
    'wyswietlenie : WYSWIETL LNAWIAS wyrazenie PNAWIAS SREDNIK'
    p[0] = Wyswietl(wyrazenie=p[3], linia=p.lineno(1))

def p_pobierz(p):
    'pobierz : POBIERZ LNAWIAS ID PNAWIAS SREDNIK'
    p[0] = Pobierz(nazwa=p[3], linia=p.lineno(1))


# Wyrażenia
def p_wyrazenie_arytmetyczne(p):
    '''wyrazenie : wyrazenie PLUS wyrazenie
                 | wyrazenie MINUS wyrazenie
                 | wyrazenie RAZY wyrazenie
                 | wyrazenie PODZIEL wyrazenie'''
    p[0] = OperacjaBinarna(operator=p[2], lewy=p[1], prawy=p[3], linia=p.lineno(2))

def p_wyrazenie_porownanie(p):
    '''wyrazenie : wyrazenie MNIEJSZE wyrazenie
                 | wyrazenie WIEKSZE wyrazenie
                 | wyrazenie MNIEJSZE_ROWNE wyrazenie
                 | wyrazenie WIEKSZE_ROWNE wyrazenie
                 | wyrazenie ROWNE wyrazenie
                 | wyrazenie NIEROWNE wyrazenie'''
    p[0] = OperacjaBinarna(operator=p[2], lewy=p[1], prawy=p[3], linia=p.lineno(2))

def p_wyrazenie_prawda(p):
    'wyrazenie : PRAWDA'
    p[0] = Liczba(1)

def p_wyrazenie_falsz(p):
    'wyrazenie : FALSZ'
    p[0] = Liczba(0)

def p_wyrazenie_logiczne(p):
    '''wyrazenie : wyrazenie I wyrazenie
                 | wyrazenie LUB wyrazenie'''
    p[0] = OperacjaBinarna(operator=p[2], lewy=p[1], prawy=p[3], linia=p.lineno(2))

def p_wyrazenie_nie(p):
    'wyrazenie : NIE wyrazenie'
    p[0] = Operacja(operator=p[1], operacja=p[2], linia=p.lineno(1))

def p_wyrazenie_ujemne(p):
    'wyrazenie : MINUS wyrazenie %prec UJEMNE'
    p[0] = Operacja(operator=p[1], operacja=p[2], linia=p.lineno(1))


def p_wyrazenie_liczba(p):
    'wyrazenie : LICZBA'
    p[0] = Liczba(wartosc=p[1])


def p_wyrazenie_zmienna(p):
    'wyrazenie : ID'
    p[0] = ZmiennaReferencja(nazwa=p[1], linia=p.lineno(1))


def p_wyrazenie_nawiasy(p):
    'wyrazenie : LNAWIAS wyrazenie PNAWIAS'
    p[0] = p[2]


def p_error(p):
    if p:
        print(f"Błąd składniowy w linii {p.lineno}: nieoczekiwany token '{p.value}'")
    else:
        print("Błąd składniowy: nieoczekiwany koniec pliku")
    sys.exit(1)

parser = yacc.yacc()