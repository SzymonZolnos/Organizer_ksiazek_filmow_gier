import sqlite3
def z_baza(tytul, typ, status, ocena,):
    conn = sqlite3.connect('kolekcja.db')
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
    cursor.execute("INSERT INTO kolekcja (tytul, typ, status, ocena) VALUES (?,?,?,?)",
                (tytul, typ , status ,ocena))
    conn.commit()
    conn.close()