from tkinter import * # http://tkinter.fdex.eu/

class Jeu:
    def __init__(self):
        """ définition fenêtre, labels, images et disposition"""
        window = Tk()
        window.title("formes, images et texte")
        # surface de dessin
        self.dessin = Canvas(window, bg="grey")
        self.dessin.configure(width=400, height=300)
        self.dessin.grid ( row=0 , column=0)

        # déclaration d'une image
        self.img_flag = PhotoImage(file = "flag.png") 

        # l'image est affichée au coord (x,y)
        self.dessin.create_image(100, 50, anchor=CENTER,image=self.img_flag)

        # une forme géométrique
        self.dessin.create_rectangle(200, 100, 200+20, 100+30, fill="green", outline='black')

        # du texte
        self.dessin.create_text(300, 100, font=("Sans-Serif", 20),text=254,fill="blue")

        window.mainloop()  

jeu = Jeu()
 

