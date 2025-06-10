from menu import menu1
from logic import l_ksiazki
from logic import l_gry
from logic import l_filmy

def main():
    while True:
        menu1()
        wybor = input('Wybierz kategorie:')
        if wybor == '1':
            l_ksiazki()
        elif wybor == '2':
            l_gry()
        elif wybor == '3':
            l_filmy()
        elif wybor == '4':
            print('Program zamknięty. Do zobaczenia!')
            break
        else:
            print('Nie ma takiej opcji! Wybierz inną.')
if __name__=='__main__':
    main()