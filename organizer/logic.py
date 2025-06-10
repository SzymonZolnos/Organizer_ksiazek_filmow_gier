#---------------Książka----------------------
def l_ksiazki():
    while True:
        print('---Książki---\n')
        print('1.Dodaj książkę\n')
        print('2.Pokaż książki\n')
        print('3.Usuń książkę\n')
        print('4.Powrót do Menu\n')

        wybor = input('Wybierz opcje:')

        if wybor == '1':
            m_ksiazki()
        elif wybor == '2':
            p_ksiazki()
        elif wybor == '3':
            uelement("ksiazka")
        elif wybor == '4':
            break
        else:
            print('Nie ma takiej opcji! Wybierz inną.\n')

#--------------menu po dodaniu ksiazki----------------------
from organizer.DataBase import z_baza
def m_ksiazki():
    tytul = input("Podaj tytuł książki:")
    autor = input("Podaj autora:")
    status = input("Czy przeczytałeś (Ukończone/W trakcie/Planowane):")
    if status == ("Ukończone"):
        while True:
            try:
                ocena = int(input("Podaj ocene od 1 do 5:"))
                if 1<=ocena<=5:
                    break
                else:
                    print('Wpisz ocene między 1-5!\n')
            except ValueError:
                print('To nie liczba spróbuj ponowanie!\n')
    elif status in ["W trakcie", "Planowane"]:
        ocena = None
    else:
        print("Nieprawidłowy status. Wpisz dokładnie jak podano.")
        return

    pelny_tytul = f"{tytul} ({autor})"
    z_baza(pelny_tytul, "ksiazka", status, ocena)
    print("Dodano książkę!\n")

#----------------Pokazywanie książek------------------------------
import sqlite3
import os
def p_ksiazki():
    if not os.path.exists("kolekcja.db"):
        print("Nie masz dodanych książek.\n")
        return
    try:
        conn = sqlite3.connect('kolekcja.db')
        cursor = conn.cursor()
        cursor.execute("SELECT tytul, status ,ocena FROM kolekcja WHERE typ = 'ksiazka'")
        ksiazki = cursor.fetchall()
        conn.close()
        if not ksiazki:
            print("Nie masz żadnych książek.\n")
        else:
            print('Lista książek:')
            for i, (tytul, status, ocena) in enumerate(ksiazki, 1):
              print(f"{i}.{tytul} | Status: {status} |Ocena: {ocena}/5")
              print()
    except sqlite3.OperationalError:
        print("Nie masz jeszcze żadnych książek.\n")
#------------------------------usuwanie elementu---------------------------------------------
import sqlite3
import os

def uelement(typ):
    if not os.path.exists("kolekcja.db"):
        print("Nie masz jeszcze bazy.\n")
        return

    conn = sqlite3.connect("kolekcja.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT id, tytul, status, ocena FROM kolekcja WHERE typ = ?",
            (typ,),
        )
        dane = cursor.fetchall()
        if not dane:
            print(f"Nie masz żadnych elementów do usunięcia.\n")
            return

        print(f"\nLista ({typ}):")
        for i, (id, tytul, status, ocena) in enumerate(dane, 1):
            print(f"{i}. {tytul} | Status: {status} | Ocena: {ocena or 'None'}")

        wybor = input("Podaj numer elementu do usunięcia (Enter = anuluj): ")
        if not wybor:
            print("Anulowano usuwanie.\n")
            return

        try:
            idx = int(wybor) - 1
            id_do_usuniecia = dane[idx][0]
        except (ValueError, IndexError):
            print("Nieprawidłowy wybór.\n")
            return

        cursor.execute(
            "DELETE FROM kolekcja WHERE id = ?",
            (id_do_usuniecia,),
        )
        conn.commit()
        print("Element został usunięty.\n")

    except sqlite3.OperationalError:
        print("Brak danych do usunięcia.\n")

    finally:
        conn.close()

#------------------------------------Gra----------------------------------------------------
def l_gry():
    while True:
        print('---Gry---\n')
        print('1.Dodaj grę\n')
        print('2.Pokaż gry\n')
        print('3.Usuń grę\n')
        print('4.Powrót do Menu\n')

        wybor = input('Wybierz opcje:')

        if wybor == '1':
                m_gry()
        elif wybor == '2':
                p_gry()
        elif wybor == '3':
                uelement("gra")
        elif wybor == '4':
             break
        else:
            print('Nie ma takiej opcji! Wybierz inną.\n')
#--------------menu po dodaniu Gry----------------------
from organizer.DataBase import z_baza
def m_gry():
    tytul = input("Podaj tytuł gry:")
    autor = input("Podaj producenta:")
    status = input("Czy grałeś (Ukończone/W trakcie/Planowane):")
    if status == ("Ukończone"):
        while True:
            try:
                ocena = int(input("Podaj ocene od 1 do 5:"))
                if 1<=ocena<=5:
                    break
                else:
                    print('Wpisz ocene między 1-5!\n')
            except ValueError:
                print('To nie liczba spróbuj ponowanie!\n')
    elif status in ["W trakcie", "Planowane"]:
        ocena = None
    else:
        print("Nieprawidłowy status. Wpisz dokładnie jak podano.")
        return

    pelny_tytul = f"{tytul} ({autor})"
    z_baza(pelny_tytul, "gra", status, ocena)
    print("Dodano grę!\n")
#----------------Pokazywanie gier------------------------------
import sqlite3
import os
def p_gry():
    if not os.path.exists("kolekcja.db"):
        print("Nie masz dodanych gier.\n")
        return
    try:
        conn = sqlite3.connect('kolekcja.db')
        cursor = conn.cursor()
        cursor.execute("SELECT tytul, status ,ocena FROM kolekcja WHERE typ = 'gra'")
        gry = cursor.fetchall()
        conn.close()
        if not gry:
            print("Nie masz żadnych gier.\n")
        else:
            print('Lista gier:')
            for i, (tytul, status, ocena) in enumerate(gry, 1):
              print(f"{i}.{tytul} | Status: {status} |Ocena: {ocena}/5")
              print()
    except sqlite3.OperationalError:
        print("Nie masz jeszcze żadnych gier.\n")

#---------------Filmy----------------------
def l_filmy():
    while True:
        print('---Filmy---\n')
        print('1.Dodaj film\n')
        print('2.Pokaż filmy\n')
        print('3.Usuń film\n')
        print('4.Powrót do Menu\n')

        wybor = input('Wybierz opcje:')

        if wybor == '1':
            m_filmy()
        elif wybor == '2':
            p_filmy()
        elif wybor == '3':
            uelement("film")
        elif wybor == '4':
            break
        else:
            print('Nie ma takiej opcji! Wybierz inną.\n')

#--------------menu po dodaniu filmu----------------------
from organizer.DataBase import z_baza
def m_filmy():
    tytul = input("Podaj tytuł filmu:")
    autor = input("Podaj reżysera:")
    status = input("Czy obejrzałeś (Ukończone/W trakcie/Planowane):")
    if status == ("Ukończone"):
        while True:
            try:
                ocena = int(input("Podaj ocene od 1 do 5:"))
                if 1<=ocena<=5:
                    break
                else:
                    print('Wpisz ocene między 1-5!\n')
            except ValueError:
                print('To nie liczba spróbuj ponowanie!\n')
    elif status in ["W trakcie", "Planowane"]:
        ocena = None
    else:
        print("Nieprawidłowy status. Wpisz dokładnie jak podano.")
        return

    pelny_tytul = f"{tytul} ({autor})"
    z_baza(pelny_tytul, "film", status, ocena)
    print("Dodano film!\n")

#----------------Pokazywanie filmów------------------------------
import sqlite3
import os
def p_filmy():
    if not os.path.exists("kolekcja.db"):
        print("Nie masz dodanych filmów.\n")
        return
    try:
        conn = sqlite3.connect('kolekcja.db')
        cursor = conn.cursor()
        cursor.execute("SELECT tytul, status ,ocena FROM kolekcja WHERE typ = 'film'")
        filmy = cursor.fetchall()
        conn.close()
        if not filmy:
            print("Nie masz żadnych filmów.\n")
        else:
            print('Lista filmów:')
            for i, (tytul, status, ocena) in enumerate(filmy, 1):
              print(f"{i}.{tytul} | Status: {status} |Ocena: {ocena}/5")
              print()
    except sqlite3.OperationalError:
        print("Nie masz jeszcze żadnych filmów.\n")