import tkinter as tk
from importlib.metadata import entry_points
from tkinter import messagebox

def o_ksiazki():
    tytul = entry_tytul.get()
    autor = entry_autor.get()
    status = var_status.get()
    messagebox.showinfo("Dodano",f"Tytuł:{tytul}\nAutor:{autor}\nStatus:{status}")

#Główne onko
okno = tk.Tk()
okno.title('Organizer')
#Pole tekstowe
tk.Label(okno, text="Tytuł").pack()
entry_tytul = tk.Entry(okno)
entry_tytul.pack()
tk.Label(okno, text="Autor").pack()
entry_autor = tk.Entry(okno)
entry_autor.pack()
tk.Label(okno, text="Status").pack()
var_status = tk.Stringvar(value="Ukończone")
tk.OptionMenu(okno, var_status, "Ukończone","W trakcie","Planowane").pack()
tk.Button(okno, text="Dodaj książkę", command=dodaj_ksiazke).pack(pady=10)
root.mainloop()
