from ast_tree import (
    Dopoki,
    Jezeli,
    Pobierz,
    Program,
    Liczba,
    Przypisanie,
    ZmiennaReferencja,
    OperacjaBinarna,
    Operacja,
    Deklaracja,
    Wyswietl,
)


class BladWykonania(Exception):
    def __init__(self, komunikat, linia):
        super().__init__(f"Błąd w linii {linia}: {komunikat}")


def oblicz_wyrazenie(node, zmienne_programu):

    if isinstance(node, Liczba):
        return node.wartosc

    if isinstance(node, ZmiennaReferencja):
        if node.nazwa not in zmienne_programu:
            raise BladWykonania(
                f"użycie niezadeklarowanej zmiennej '{node.nazwa}'", node.linia
            )
        return zmienne_programu[node.nazwa]


    if isinstance(node, OperacjaBinarna):
        lewa_strona_operacji = oblicz_wyrazenie(node.lewy, zmienne_programu)
        prawa_strona_operacji = oblicz_wyrazenie(node.prawy, zmienne_programu)

        if node.operator == '+':
            return lewa_strona_operacji + prawa_strona_operacji
        elif node.operator == '-':
            return lewa_strona_operacji - prawa_strona_operacji
        elif node.operator == '*':
            return lewa_strona_operacji * prawa_strona_operacji
        elif node.operator == '/':
            if prawa_strona_operacji == 0:
                raise BladWykonania("dzielenie przez zero", node.linia)
            return lewa_strona_operacji // prawa_strona_operacji
        elif node.operator == '<':
            if lewa_strona_operacji < prawa_strona_operacji:
                return 1
            else:
                return 0
        elif node.operator == '>':
            if lewa_strona_operacji > prawa_strona_operacji:
                return 1
            else:
                return 0
        elif node.operator == '<=':
            if lewa_strona_operacji <= prawa_strona_operacji:
                return 1
            else:
                return 0
        elif node.operator == '>=':
            if lewa_strona_operacji >= prawa_strona_operacji:
                return 1
            else:
                return 0
        elif node.operator == '==':
            if lewa_strona_operacji == prawa_strona_operacji:
                return 1
            else:
                return 0
        elif node.operator == '!=':
            if lewa_strona_operacji != prawa_strona_operacji:
                return 1
            else:
                return 0
        elif node.operator == 'i':
            if lewa_strona_operacji and prawa_strona_operacji:
                return 1
            else:
                return 0
        elif node.operator == 'lub':
            if lewa_strona_operacji or prawa_strona_operacji:
                return 1
            else:
                return 0

    if isinstance(node, Operacja):
        operacja = oblicz_wyrazenie(node.operacja, zmienne_programu)
        if node.operator == 'nie':
            if not operacja:
                return 1
            else:
                return 0
        elif node.operator == '-':
            return -operacja
            
        raise BladWykonania(f"nieznany operator '{node.operator}'", node.linia)

    raise BladWykonania(f"nieznany typ wyrażenia: {type(node)}", 0)


def wykonaj_instrukcje(node, zmienne_programu):

    if isinstance(node, Deklaracja):
        if node.nazwa in zmienne_programu:
            raise BladWykonania(
                f"zmienna '{node.nazwa}' została już zadeklarowana", node.linia
            )
        if node.wartosc is not None:
            zmienne_programu[node.nazwa] = oblicz_wyrazenie(node.wartosc, zmienne_programu)
        else:
            zmienne_programu[node.nazwa] = 0  
        return

    if isinstance(node, Przypisanie):
        if node.nazwa not in zmienne_programu:
            raise BladWykonania(
                f"przypisanie do niezadeklarowanej zmiennej '{node.nazwa}'", node.linia
            )
        zmienne_programu[node.nazwa] = oblicz_wyrazenie(node.wartosc, zmienne_programu)
        return

    if isinstance(node, Wyswietl):
        wartosc = oblicz_wyrazenie(node.wyrazenie, zmienne_programu)
        print(wartosc)
        return
    
    if isinstance(node, Pobierz):
        if node.nazwa not in zmienne_programu:
            raise BladWykonania(
                f"próba pobrania do niezadeklarowanej zmiennej '{node.nazwa}'", node.linia
            )
        try:
            wartosc = int(input())
        except ValueError:
            raise BladWykonania("nie można przekonwertować wejścia na liczbę", node.linia)
        zmienne_programu[node.nazwa] = wartosc
        return
    
    if isinstance(node, Jezeli):
        warunek = oblicz_wyrazenie(node.warunek, zmienne_programu)
        if warunek:
            for instrukcja in node.wtedy:
                wykonaj_instrukcje(instrukcja, zmienne_programu)
        elif node.inaczej is not None:
            for instrukcja in node.inaczej:
                wykonaj_instrukcje(instrukcja, zmienne_programu)
        return

    if isinstance(node, Dopoki):
        while oblicz_wyrazenie(node.warunek, zmienne_programu):
            for instrukcja in node.instrukcje:
                wykonaj_instrukcje(instrukcja, zmienne_programu)
        return
    raise BladWykonania(f"nieznany typ instrukcji: {type(node)}", 0)


def uruchom(program: Program):
    zmienne_programu = {}  
    for instrukcja in program.instrukcje:
        wykonaj_instrukcje(instrukcja, zmienne_programu)
    return zmienne_programu