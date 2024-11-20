import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
# Créer la fenêtre
window = tk.Tk()
# Titre de la fenêtre
window.title("Ma première fenêtre Tkinter")
# Taille de la fenêtre
window.geometry("400x300") 

# Créer un bouton
button = tk.Button(window, text="Cliquez ici") 
# Afficher le bouton
button.pack()

# Créer une étiquette
label = tk.Label(window, text="Bienvenue sur mon programme Tkinter")

#Créer un champ de texte
entry = tk.Entry(window)
entry.pack()

# Fonction pour afficher une boîte de dialogue
def show_dialog():
    messagebox.showinfo("Titre de la boîte de dialogue", "Ceci est un message.") 
# Créer un bouton pour afficher la boîte de dialogue
button = tk.Button(window, text="Afficher la boîte de dialogue", command=show_dialog)
button.pack()

# Créer un Treeview
treeview = ttk.Treeview(window) 
# Ajouter des éléments à l'arbre
treeview.insert("", "0", "node1", text="Node 1")
treeview.insert("node1", "0", "subnode1", text="Subnode 1")
# Afficher l'arbre
treeview.pack()

# Créer un Canvas
canvas = tk.Canvas(window, width=200, height=200)
# Dessiner une ligne
line = canvas.create_line(0, 0, 200, 200) 
# Dessiner un rectangle
rectangle = canvas.create_rectangle(50, 50, 150, 150, fill="red") 
# Afficher le Canvas
canvas.pack()


# Créer un Notebook
notebook = ttk.Notebook(window) 
# Créer le premier onglet
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Onglet 1")

# Créer le deuxième onglet
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Onglet 2") 
# Afficher le Notebook
notebook.pack()


# Afficher l'étiquette
label.pack() # Afficher la fenêtre
window.mainloop()