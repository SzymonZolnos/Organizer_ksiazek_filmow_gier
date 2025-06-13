import tkinter as tk
from tkinter import messagebox
from DataBase import z_baza, p_kolekcje, u_opcje
class OrganizerGUI:
    def __init__(self,master):
        self.master = master
        master.title("Organizer")
        self.var_type = tk.StringVar(value="ksiazka")
        self.var_type = tk.StringVar(value="gra")
        self.var_type = tk.StringVar(value="film")
        self.var_status = tk.StringVar(value="Ukończone")
    #-------------------------------Tytuł-------------------------------------------------
        tk.Label(master, text="Tytuł:").pack()
        self.entry_tytul = tk.Entry(master)
        self.entry_tytul.pack()
#-----------------------------------Autor--------------------------------------------------
        tk.Label(master, text="Autor:").pack()
        self.entry_autor = tk.Entry(master)
        self.entry_autor.pack()
# -----------------------------------Typ--------------------------------------------------
        tk.Label(master, text="Typ (książka/Film/Gra:").pack()
        tk.OptionMenu(master, self.var_type,"ksiazka","gra","film").pack()
# ------------------------------------Staus-------------------------------------------------
        tk.Label(master, text="Status (Ukończone/W trakcie/Planowane:").pack()
        tk.OptionMenu(master, self.var_type,"Ukończone","W trakcie","Planowane").pack()
# -----------------------------------Ocena--------------------------------------------------
        tk.Label(master, text="Ocena (1-5):").pack()
        self.entry_ocena = tk.Entry(master)
        self.entry_ocena.pack()
# -----------------------------------Przyciski--------------------------------------------------
        tk.Button(master, text = "Dodaj do kolekcji", command=self.dodaj_element).pack(pady=5)
        tk.Button(master, text="Zobacz całą kolekcję", command=self.zobacz_kolekcje).pack(pady=5)
        tk.Button(master, text="Usuń element", command=self.usun_element).pack(pady=5)
        tk.Button(master, text="Zobacz książki", command=lambda: self.zobacz_typ("ksiazka")).pack()
        tk.Button(master, text="Zobacz_gry", command=lambda: self.zobacz_typ("gra")).pack()
        tk.Button(master, text="Zobacz_filmy", command=lambda: self.zobacz_typ("film")).pack()
# -----------------------------------Wyświetl wynik--------------------------------------------------
        self.text_output = tk.Text(master, height=15, width=60)
        self.text_output.pack(pady=10)

    def dodaj_element(self):
        tytul = self.entry_tytul.get()
        autor = self.entry_autor.get()
        status = self.var_status.get()
        typ = self.var_type.get()
        pelny_tytul = f"{tytul} {autor}"

        if status.lower() == "Ukończone":
            try:
                ocena = int(self.entry_ocena.get())
                if not ocena (1 <= ocena <= 5):
                    raise ValueError
            except ValueError:
                messagebox.showerror("Błędna ocena!","Ocena musi być od 1 do 5.")
                return
            else:
                ocena = None

            z_baza(pelny_tytul, typ, status, ocena)
            messagebox.showinfo("Sukces!",f"Dodano element do kolekcji.")
            self.wyczysc_pola()
#
    def zobacz_kolekcje(self):
        self.text_output.delete('1.0', tk.END)
        wynik = p_kolekcje
        if not wynik:
            self.text_output.insert(tk.END,"Brak pozycji w kolekcji.\n")
        for i,(id, tytul, typ, status, ocena) in enumerate(wynik, 1):
            ocena_txt = f"|ocena: {ocena}/5"if ocena is not None else ""
            self.text_output.insert(tk.END, f"{i}.{tytul}|Typ:{typ}|Status:{status}{ocena_txt}\n")

    def zobacz_typ(self, typ):
        self.text_output.delete('1.0', tk.END)
        wynik = p_kolekcje()
        filtrowanie = [w for w in wynik if [2]==typ]

        if not filtrowanie:
            self.text_output.insert(tk.END,"Brak pozycji w kolekcji.\n")
            return
        for i, (id, tytul, typ, status, ocena) in enumerate(filtrowanie, 1):
            ocena_txt = f"|ocena: {ocena}/5" if ocena is not None else ""
            self.text_output.insert(tk.END)
            f"{i}.{tytul}|Typ:{typ}|Status:{status}{ocena_txt}\n"

    def usun_element(self):
            try:
                id_do_usuniecia = int(self.entry_tytul.get())
            except ValueError:
                messagebox.showerror("Błąd!","Wprowadzono zły numer id do usunięcia.")
                return
            u_opcje(id_do_usuniecia)
            messagebox.showinfo("Usunięto!",f"Usunięto pozycje o ID: {id_do_usuniecia}")
            self.zobacz_kolekcje()

            def wyczysc_pola(self):
                self.entry_tytul.delete(0, tk.END)
                self.entry_autor.delete(0, tk.END)
                self.entry_ocena.delete(0, tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    app = OrganizerGUI(root)
    root.mainloop()
