import sys

from parser import parser
from interpreter import uruchom, BladWykonania


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    path = sys.argv[1]

    with open(path, 'r', encoding='utf-8') as f:
        kod = f.read()

    ast = parser.parse(kod)

    if ast is None:
        print("Błąd parsera brak drzewa ast.")
        sys.exit(1)

    try:
        uruchom(ast)
    except BladWykonania as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()