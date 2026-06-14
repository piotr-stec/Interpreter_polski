
class Program:
    def __init__(self, instrukcje):
        self.instrukcje = instrukcje  


class Liczba:
    def __init__(self, wartosc):
        self.wartosc = wartosc  


class ZmiennaReferencja:
    def __init__(self, nazwa, linia):
        self.nazwa = nazwa  
        self.linia = linia  


class OperacjaBinarna:
    def __init__(self, operator, lewy, prawy, linia):
        self.operator = operator  
        self.lewy = lewy           
        self.prawy = prawy          
        self.linia = linia

class Operacja:
    def __init__(self, operator, operacja, linia):
        self.operator = operator  
        self.operacja = operacja           
        self.linia = linia

class Jezeli:
    def __init__(self, warunek, wtedy, inaczej, linia):
        self.warunek = warunek  
        self.wtedy = wtedy           
        self.inaczej = inaczej
        self.linia = linia

class Dopoki:
    def __init__(self, warunek, instrukcje, linia):
        self.warunek = warunek  
        self.instrukcje = instrukcje           
        self.linia = linia

class Deklaracja:
    def __init__(self, nazwa, wartosc, linia):
        self.nazwa = nazwa      
        self.wartosc = wartosc 
        self.linia = linia

class Przypisanie:
    def __init__(self, nazwa, wartosc, linia):
        self.nazwa = nazwa
        self.wartosc = wartosc
        self.linia = linia

class Wyswietl:
    def __init__(self, wyrazenie, linia):
        self.wyrazenie = wyrazenie  
        self.linia = linia

class Pobierz:
    def __init__(self, nazwa, linia):
        self.nazwa = nazwa  
        self.linia = linia