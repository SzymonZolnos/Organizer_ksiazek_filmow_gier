#---------------Książka----------------------
import os
from DataBase import BazaDanych

db = BazaDanych()

class Pozycja:
    def __init__(self, typ):
        self.typ = typ

    def dodaj(self):
        tytul = input("Podaj tytuł:")
        autor = input("Podaj autora/producenta/reżysera:")
        status = input("Status (Ukończone/W trakcie/Planowane):")

        if status == "Ukończone":
            while True:
                try:
                    ocena = int(input("Ocena 1-5: "))
                    if 1 <= ocena <= 5:
                        break
                    print("Ocena musi być od 1 do 5!")
                except ValueError:
                    print("To nie liczba!")
        elif status in ["W trakcie", "Planowane"]:
            ocena = None
        else:
            print("Nieprawidłowy status.")
            return

        pelny_tytul = f"{tytul} ({autor})"
        db.dodaj_pozycje(pelny_tytul, self.typ, status, ocena)
        print("Dodano pozycję!")

    def pokaz(self):
        if not os.path.exists(db.nazwa_bazy):
            print("Brak bazy danych.")
            return

        pozycje = db.pobierz_pozycje(self.typ)
        if not pozycje:
            print("Brak danych.")
            return

        for i, (tytul, status, ocena) in enumerate(pozycje, 1):
            print(f"{i}. {tytul} | Status: {status} | Ocena: {ocena or 'None'}/5")

    def usun(self):
        if not os.path.exists(db.nazwa_bazy):
            print("Brak bazy danych.")
            return

        pozycje = db.pobierz_do_usuniecia(self.typ)
        if not pozycje:
            print("Brak pozycji do usunięcia.")
            return

        for i, (id, tytul, status, ocena) in enumerate(pozycje, 1):
            print(f"{i}. {tytul} | Status: {status} | Ocena: {ocena or 'None'}")

        wybor = input("Podaj numer do usunięcia (Enter = anuluj): ")
        if not wybor:
            return

        try:
            idx = int(wybor) - 1
            db.usun_pozycje(pozycje[idx][0])
            print("Usuń to.")
        except (ValueError, IndexError):
            print("Błędny wybór.")