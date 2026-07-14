import tkinter as tk
from tkinter import messagebox #hapandeh ny ambany 
root = tk.Tk()
root.title("Salutation")
root.geometry("720x420")
root.resizable(False,False) #TSY AFAK MODIFIENA NY TAILLE 
nom = tk.StringVar() # @zay mifandray @champs saise
frame_haut = tk.Frame(root)
frame_haut.pack(pady=10) 
label_titre =tk.Label(frame_haut,text="Bonjour et bienvenue,veillez entrez votre nom ") 
label_titre.pack() #hampiseo anzy @zay 

frame_milieu = tk.Frame(root)
frame_milieu.pack(pady=0)
label_nom =tk.Label(frame_milieu,text="Entrez votre nom")
label_nom.grid(row=0,column=0,padx=5,pady=5)
entrer_nom =tk.Entry(frame_milieu,textvariable=nom,width=20)
entrer_nom.grid(row=0,column=1,padx=5,pady=5)

#================= boutton ============
def afficher_salutation():
    prenom = nom.get().strip()
    if prenom == "":
        messagebox.showwarning("Manorata teny key zafady !!")
    else:
        messagebox.showinfo(f"Salut {prenom}; comment ça va aujourd'hui !?")
bouton_valider = tk.Button(frame_milieu,text=" Valider ",command=afficher_salutation)
bouton_valider.grid(row=0,column=2,pady=5)

root.mainloop()