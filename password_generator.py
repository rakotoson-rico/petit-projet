from tkinter import *
# fenetre 
window = Tk()
window.title("mots de passe")
window.geometry("720x430")
window.minsize(420,360)
window.iconbitmap("#")
window.config(background='#ffffff')
#frame priciipam 
frame = Frame(window, bg='#ffffff')
label_title = Label(frame,text="MOTS DE PASSE " ,font=("helvedica",20) , bg='')
# creation image
Width = 300 #largeur 
height = 300
# haka ny source                   haleben 
image = PhotoImage(file=".png").zoom(35).subsample(32)

#dssiner des composant graphique 
Canvas = Canvas(window,width=width, height=height,bg='#ffffff', bd=0,)
Canvas.create_image(width/2, height/2, image= image)

Canvas.pack()
frame.pack(expand=YES)
# fenetre  
window.mainloop()
