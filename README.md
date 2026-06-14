# Interpreter 


## Instalacja

```bash
pip install ply
```

## Uruchomienie
### Przykładowe programy

```bash
./run.sh program_wszystko.txt
```
```bash
./run.sh program_blad1.txt
```
```bash
./run.sh program_blad2.txt
```
```bash
./run.sh program_blad3.txt
```
### lub przy wykorzystaniu pythona
```bash
python3 main.py program_wszystko.txt
```

## Składnia języka

### Zmienne
```
zmienna x;          
zmienna x = 5;      
x = 10;             
```

### Operatory arytmetyczne
```
zmienna wynik = 2 + 3;
zmienna wynik = 2 - 3;
zmienna wynik = 2 * 3;
zmienna wynik = 10 / 2;
```

### Operatory porównania
```
x == y    # równe
x != y    # różne
x < y     # mniejsze
x > y     # większe
x <= y    # mniejsze lub równe
x >= y    # większe lub równe
```

### Operatory logiczne
```
x i y     # AND
x lub y   # OR
nie x     # NOT
prawda    # true
fałsz     # false
```

### Instrukcja warunkowa
```
jeżli (warunek) {
    # instrukcje
}

jeżli (warunek) {
    # instrukcje
} inaczej {
    # instrukcje
}
```

### Pętla while
```
dopóki (warunek) {
    # instrukcje
}
```

### Wyświetlanie i pobieranie
```
wyświetl(x);       
pobierz(x);     
```

### Komentarze
```
# komentarz jednoliniowy

### komentarz
    wieloliniowy ###
```

### zerwezerwowane keywords 
```
zmienna, wyświetl, pobierz, jeżli, inaczej, dopóki, prawda, fałsz, i, lub, nie
```
