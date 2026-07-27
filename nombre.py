import tkinter as tk 
from tkinter import ttk
root = tk.Tk()
root.geometry("720x420")
root.title(" Deux nombre ")
nombre1 = tk.IntVar()
nombre2 = tk.IntVar()
frame = ttk.Frame(root) #ahafana mampisa ny weight 
frame.grid()
ttk.Label(frame,text="Première nombre :").grid(column=2,row=1)
ttk.Label(frame,text="Deuxième nombre :").grid(column=6,row=1)

#tk.Label(frame_milieu,text="Première nombre ").grid(column=10,row=0)
#nombre_1 = tk.Label(frame_milieu,textvariable=nombre1).grid(column=10,row =0)
entrer_nombre_1 =ttk.Entry(frame,textvariable=nombre1).grid(column=2,row=3)
entrer_nombre_2 =ttk.Entry(frame,textvariable=nombre2).grid(column=6,row=3)
ttk.Label(frame,text="Résultat").grid(column=3,row=7)

# resultat = ttk.Entry(frame).grid(column=3,row=8) / lasa none ny resultat affochene rah soratana miaraky 
resultat = ttk.Entry(frame)
resultat.grid(column=3,row=8)

def addition():
    nbr1 = nombre1.get()
    nbr2 = nombre2.get()
     #mamafa ny teo aloha  
    return resultat.insert(0,nbr1 + nbr2 ) #argument ftsn ny 0

def soustraction():
    nbr1 = nombre1.get()
    nbr2 = nombre2.get()
    return resultat.insert(0,nbr1 - nbr2 ) #argument ftsn ny 0
    
def multiplication():
    nbr1 = nombre1.get()
    nbr2 = nombre2.get()
    return resultat.insert(0,nbr1 * nbr2 ) 

def division():
    nbr1 = nombre1.get()
    nbr2 = nombre2.get()
    return resultat.insert(0,nbr1 / nbr2 ) #argument ftsn ny 0

bouton =ttk.Button(frame,text="+",command=addition).grid(column=1,row=20)
bouton =ttk.Button(frame,text="-",command=soustraction).grid(column=2,row=20)
bouton =ttk.Button(frame,text="*",command=multiplication).grid(column=3,row=20)
bouton =ttk.Button(frame,text="/",command=division).grid(column=5,row=20)


root.mainloop()