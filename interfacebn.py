import tkinter as tk
from tkinter import ttk as ttk


Mafenetre = tk.Tk() # on crée une instance
Mafenetre.title("Bataille Navale")

def Clic():
    Label1 = Label(Mafenetre, text = 'BATAILLE NAVALE !', fg = 'red')
    # Positionnement du widget avec la méthode pack()
    Label1.pack()

    

a1 = Button(Mafenetre, text='L1-C1', borderwidth=1).grid(row=1, column=1)
a2 = Button(Mafenetre, text='L1-C2', borderwidth=1).grid(row=1, column=2)


# Lancement du gestionnaire d'événements
Mafenetre.mainloop() 




## http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel
