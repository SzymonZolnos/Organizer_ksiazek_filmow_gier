import sqlite3

class BazaDanych:
    def __init__(self, nazwa_bazy='kolekcja.db'):
        self.nazwa_bazy = nazwa_bazy
        self._utworz_tabele()

    def _utworz_tabele(self):
        with sqlite3.connect(self.nazwa_bazy) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS kolekcja (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tytul TEXT NOT NULL,
                typ TEXT CHECK(typ IN ('ksiazka','film','gra')) NOT NULL,
                status TEXT CHECK (status IN ('Ukończone','W trakcie', 'Planowane')) NOT NULL,
                ocena INTEGER CHECK(ocena BETWEEN 1 AND 5 OR ocena IS NULL)
            )
            ''')

    def dodaj_pozycje(self, tytul, typ, status, ocena):
        with sqlite3.connect(self.nazwa_bazy) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO kolekcja (tytul, typ, status, ocena) VALUES (?, ?, ?, ?)",
                           (tytul, typ, status, ocena))
            conn.commit()

    def pobierz_pozycje(self, typ):
        with sqlite3.connect(self.nazwa_bazy) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT tytul, status, ocena FROM kolekcja WHERE typ = ?", (typ,))
            return cursor.fetchall()

    def pobierz_do_usuniecia(self, typ):
        with sqlite3.connect(self.nazwa_bazy) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, tytul, status, ocena FROM kolekcja WHERE typ = ?", (typ,))
            return cursor.fetchall()

    def usun_pozycje(self, id):
        with sqlite3.connect(self.nazwa_bazy) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM kolekcja WHERE id = ?", (id,))
            conn.commit()

