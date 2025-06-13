from menu import Menu
from logic import Pozycja

def main():
    menu = Menu()
    menu.start()
    while True:
        menu.menu_glowne()
        wybor = input('Wybierz kategorię:')
        if wybor == '1':
            ksiazka = Pozycja('ksiazka')
            obsluz(ksiazka)
        elif wybor == '2':
            gra = Pozycja('gra')
            obsluz(gra)
        elif wybor == '3':
            film = Pozycja('film')
            obsluz(film)
        elif wybor == '4':
            print('Do zobaczenia!')
            break
        else:
            print('Nie ma takiej opcji.')

def obsluz(pozycja):
    while True:
        print(f'---{pozycja.typ.title()}---')
        print('1. Dodaj')
        print('2. Pokaż')
        print('3. Usuń')
        print('4. Powrót')
        wybor = input('Wybierz: ')
        if wybor == '1':
            pozycja.dodaj()
        elif wybor == '2':
            pozycja.pokaz()
        elif wybor == '3':
            pozycja.usun()
        elif wybor == '4':
            break
        else:
            print('Nie ma takiej opcji.')

if __name__ == '__main__':
    main()
