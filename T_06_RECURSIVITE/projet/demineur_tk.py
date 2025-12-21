# -*- coding: utf-8 -*-
from tkinter import *
from random import randrange

ECHELLE_PIXEL = 50
LARGEUR,HAUTEUR = 9,9

class demineur:
    def __init__(self):

        self.secondes = 0 #pour afficher le temps écoulé
        self.nbMines = 10

        # objet tkinter pour créer une interface graphique
        window = Tk()
        window.title("démineur")
        # définition des zones de texte
        self.chaine1 = Label ( window ) # zone de texte pour afficher le nombre de mines
        self.chaine2 = Label ( window ) # zone de texte pour affiher le temps
        self.chaine1.grid ( row=0 , column=0)
        self.chaine2.grid ( row=0 , column=1)
        self.chaine1.configure(text = str(self.nbMines),fg="red")
        self.chaine2.configure(text = str(self.secondes),fg="red")
        self.chaine2.after(1000, self.horloge) # appel de la méthode horloge dans 1000ms

        self.dessin = Canvas(window, width=LARGEUR*ECHELLE_PIXEL, height=HAUTEUR*ECHELLE_PIXEL, bg="grey")
        self.dessin.bind ( "<Button-1>" , self.clic_gauche )
        self.dessin.bind ( "<Button-3>" , self.clic_droit )
        self.dessin.grid ( row=1 , column=0, columnspan=2)

        # dessiner le quadrillage
        for i in range(HAUTEUR):
            y = i*ECHELLE_PIXEL
            self.dessin.create_line(0,y,LARGEUR*ECHELLE_PIXEL,y,fill="white")        
        for j in range(LARGEUR):
            x = j*ECHELLE_PIXEL
            self.dessin.create_line(x,0,x,HAUTEUR*ECHELLE_PIXEL,fill="white")        

        window.mainloop()    

    def clic_gauche(self,event):
        """ découvre une cellule"""
        print("clic_gauche",event.x,event.y)
            
    def clic_droit(self,event):
        """méthode dessine un drapeau"""
        #self.dessin.create_text(x, y, text="")
        print("clic_droit",event.x,event.y)

    def horloge(self)->None:
        """méthode appelée chaque seconde pour afficher le temps"""
        self.secondes += 1
        self.chaine2.configure(text=str(self.secondes))
        self.chaine2.after(1000, self.horloge) #appel de la méthode dans 1000ms

jeu = demineur()