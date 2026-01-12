# -*- coding: utf-8 -*-
# doc tkinter dans ressources
from tkinter import *
from random import *

class Pile(list):
    """ héritage de la classe list de python
    une classe pour gérer les piles"""
    def __init__(self):
        list.__init__(self)
    
    def empiler(self,valeur):
        self.append(valeur)
    
    def depiler(self):
        return self.pop()
        
    def top(self):
        return self[-1]

class Jeu:
    def __init__(self):
        self.nb_disques = 3
        self.H_disque = 25 #hauteur disque
        self.L=600 #largeur fenêtre
        self.H=60*(self.nb_disques+1) #hauteur fenêtre
        self.Y0 = self.H - self.H_disque # position basse tour
        self.X0 = self.L//4 #position tour gauche
        self.coups = 0 # compteur de coups
        self.window = Tk() 
        self.window.title("Les tours de Hanoï")
        self.canvas = Canvas(self.window, width=self.L, height=self.H, bg="black")
        self.canvas.grid ( row=0 , column=0, columnspan=4)
        
        texteCoups = Label(self.window)
        texteCoups.grid(row=1 , column=0)
        self.textCoups = StringVar()
        self.textCoups.set("coups:0")
        texteCoups.configure(textvariable=self.textCoups,fg="blue")
        
        cadre = LabelFrame(self.window, text="disques")
        cadre.grid(row=1, column=1)
        listeOptions = ('3','4','5','6','7')
        self.v = StringVar()
        self.v.set(listeOptions[0])
        optionMenu1 = OptionMenu(cadre, self.v, *listeOptions)
        optionMenu1.pack()
        
        button1 = Button(self.window)
        self.buttonText = StringVar()
        self.buttonText.set("Jouer")
        button1.configure(textvariable=self.buttonText, padx=10, justify="center", command=self.start)
        button1.grid(row=1, column=2)
        
        textePosition = Label (self.window)
        self.textePosition = StringVar()
        self.textePosition.set("position:")
        textePosition.grid (row=1 , column=3)
        textePosition.configure(textvariable=self.textePosition,fg="blue")
        self.canvas.bind ( "<Motion>" , self.motion ) # le déplacement souris est lié à la méthode motion

        #dessiner le jeu
        for x in range(self.X0,4*self.X0,self.X0):
            self.canvas.create_line(x,30,x,self.Y0,x-40,self.Y0,x+40,self.Y0,fill='white')


        #création des 3 piles
        self.piles = [Pile(),Pile(),Pile()]
        self.window.mainloop()

    def motion(self,event):
        """ évènement souris """
        self.textePosition.set("position:"+str(event.x)+","+str(event.y))

    def start(self, restart=False):
        """ dessine le jeu : les 3 tours, création des disques, empilage """
        if self.buttonText.get()=="Rejouer": #rejoue
            self.coups = 0
            self.textCoups.set("coups:"+str(self.coups))
            for pile in self.piles:
                while len(pile)>0:
                    self.canvas.delete(pile.depiler())
            self.canvas.delete("texteFin")
        #dessiner les disques
        largeur = self.L//5 # largeur du grand disque
        x, y = self.X0 - largeur//2, self.Y0-1 # placement
        color = ('blue','orange','green', 'magenta', 'yellow', 'red', 'pink')
        self.nb_disques = int(self.v.get())
        print(self.nb_disques)
        for i in range(self.nb_disques):
            disque = self.canvas.create_rectangle( x , y, x+largeur, y-self.H_disque, fill=color[i], tags="rect")
            self.piles[0].empiler(disque)
            largeur *= 0.75
            x = self.X0 - largeur//2
            y -= self.H_disque
        self.unblock(self.piles[0].top()) #la tour du haut de la pile peut bouger
        self.buttonText.set("Rejouer")
        
    def unblock(self,disque):
        self.canvas.tag_bind(disque, '<Button1-Motion>', self.move_tour)
        self.canvas.tag_bind(disque, '<ButtonRelease-1>', self.mouse_release)

    def block(self,disque):
        self.canvas.tag_unbind(disque, '<Button1-Motion>')
        self.canvas.tag_unbind(disque, '<ButtonRelease-1>')
        
    def move_tour(self, event):
        disque = event.widget.find_withtag("current")[0]
        x0, y0, x1, y1 = self.canvas.coords(disque)
        self.canvas.move(disque,event.x-x0, event.y-y0)

    def mouse_release(self, event):
        """si on peut, placer le disque au bon endroit
        sinon le ramener à sa place initiale"""
        # de quelle pile provient le disque ?
        disque = event.widget.find_withtag("current")[0]
        prov = 0
        while len(self.piles[prov])==0 or self.piles[prov].top()!=disque:
            prov += 1 
        # vers quelle destination ?
        if event.x > self.L*2/3: # pile droite
            dest = 2
        elif event.x > self.L*1/3: # pile milieu
            dest = 1
        else: # pile gauche
            dest = 0

        x,_,x1,_ = self.canvas.coords(disque)
        largeur = x1-x

        if len(self.piles[dest])!=0:
            x,_,x1,_ = self.canvas.coords(self.piles[dest].top())
        # placement correct ? une plus petite au dessus
        if  len(self.piles[dest])==0 or largeur < x1-x  :
            if len(self.piles[dest])>0:
                self.block(self.piles[dest].top())
            self.piles[dest].empiler(self.piles[prov].depiler())
            if len(self.piles[prov])>0:
                self.unblock(self.piles[prov].top())
            x = self.X0*(dest+1) - largeur//2
            y = self.Y0 - self.H_disque*(len(self.piles[dest])-1) -1 
            self.coups +=1
            self.textCoups.set("coups:"+str(self.coups))
        else:
            # on le ramène à sa position initiale
            y = self.Y0 - self.H_disque*(len(self.piles[prov])-1) -1
            x = self.X0*(prov+1) - largeur//2

        self.canvas.coords(disque, x, y, x+largeur, y-self.H_disque)
        self.gagne()

    def gagne(self):
        
        if len(self.piles[2]) == self.nb_disques:
            coupsMin = 2**(self.nb_disques) -1
            if self.coups== coupsMin:
                texte = "Bravo, vos déplacements ont été optimaux !"
            else:
                texte = "Pas mal, mais vous pouvez mieux faire !"
            self.canvas.create_text(self.L//2,self.H//2, text=texte, fill="yellow", tags="texteFin")
            self.block(self.piles[2].top())



jeu = Jeu()