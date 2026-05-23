

import webbrowser
def open():
    webbrowser.open_new("url") 


#fenetre hisy anaz * ensemble des elelmnt 
from tkinter import *
# creer un premier fenetre racine manao variable
window = Tk()

#personalisation du f
# TITRE 
window.title("RICOST")
# par defaut xy
window.geometry("720x420")
window.minsize(480, 360)
# atao ico ny sary datao @ ambony 
window.iconbitmap("")
window.config(background='#b8b79b89')
frame = Frame(window, bg='#b8b79b89', bd=1, relief= SUNKEN)

#ajouter un text manao varible ndraik enplacement sy soratr ,bg hampitov n couleur font ,fg nenazy 
Label_title = Label(boite, text="BONJOUR",font=("courrier", 40),bg='#b8b79b89',fg="white")
# afficher 
# side left a gauche 
# ATAO EXPAND YES @zay centre avao izy 
Label_title.pack()
# centrer le txt au milieut 

# sous titre 
Label_subtitle = Label(boite, text="Bienvenue dans le game ",font=("courrier", 25),bg='#b8b79b89',fg="white")
Label_subtitle.pack()

yt_button =Button(frame,text="ouvrir", font=("courier",25), bg='while', fg='#b8b79b89',command=open)
# MAKA LAGEUR DISPO @ X 
yt_button.pack(pady=25, fill=X)

# atao anaty boite indreo  ign no crntrena ambony 
# pactena 
frame.pack(expand= YES)

# afficher  principal caree 
window.mainloop()