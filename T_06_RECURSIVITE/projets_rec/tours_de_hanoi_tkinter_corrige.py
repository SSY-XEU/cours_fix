# -*- coding: utf-8 -*-
# doc tkinter dans ressources
from tkinter import *
import time

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
        self.canvas.grid ( row=0 , column=0, columnspan=5)
        
        self.texteCoups = Label(self.window,text="coups:0", foreground="blue")
        self.texteCoups.grid(row=1 , column=0)
        
        cadre = LabelFrame(self.window, text="disques")
        cadre.grid(row=1, column=1)
        listeOptions = (3,4,5,6,7)
        self.v = IntVar()
        self.v.set(listeOptions[0])
        optionMenu1 = OptionMenu(cadre, self.v, *listeOptions)
        optionMenu1.pack()
        
        self.button1 = Button(self.window, text="Jouer", padx=5, justify="center", command=self.start)
        self.button1.grid(row=1, column=2)

        button2 = Button(self.window, text="Résoudre", padx=5, justify="center", command=self.hanoi_ia)
        button2.grid(row=1, column=3)

        self.textePosition = Label (self.window, text="position:", foreground="blue")
        self.textePosition.grid (row=1 , column=4)

        self.canvas.bind ( "<Motion>" , self.motion ) # le déplacement souris est lié à la méthode motion

        #dessiner le jeu
        for x in range(self.X0,4*self.X0,self.X0):
            self.canvas.create_line(x,30,x,self.Y0,x-40,self.Y0,x+40,self.Y0,fill='white')

        #création des 3 piles
        self.piles = [Pile(),Pile(),Pile()]
        self.window.mainloop()

    def motion(self,event):
        """ évènement souris """
        self.textePosition.configure(text="position:"+str(event.x)+","+str(event.y))

    def start(self, restart=False):
        """ dessine le jeu : les tours, création des disques, empilage """
        if restart or self.button1.cget("text")=="Rejouer": #rejoue
            self.coups = 0
            self.texteCoups.configure(text="coups:"+str(self.coups))
            for pile in self.piles:
                while len(pile)>0:
                    self.canvas.delete(pile.depiler())
            self.canvas.delete("texteFin")
        #dessiner les disques
        largeur = self.L//5 # largeur du grand disque
        x, y = self.X0 - largeur//2, self.Y0-1 # placement
        color = ('violet', 'indigo', 'blue','green', 'yellow', 'orange', 'red')
        self.nb_disques = self.v.get()
        for i in range(self.nb_disques):
            disque = self.canvas.create_rectangle( x , y, x+largeur, y-self.H_disque, fill=color[i], tags="rect")
            self.piles[0].empiler(disque)
            largeur *= 0.75
            x = self.X0 - largeur//2
            y -= self.H_disque
        self.unblock(self.piles[0].top()) #la tour du haut de la pile peut bouger
        self.button1.configure(text="Rejouer")

        
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
            self.texteCoups.configure(text="coups:"+str(self.coups))
        else:
            # on le ramène à sa position initiale
            y = self.Y0 - self.H_disque*(len(self.piles[prov])-1) -1
            x = self.X0*(prov+1) - largeur//2

        self.canvas.coords(disque, x, y, x+largeur, y-self.H_disque)
        self.gagne()

    def gagne(self): 
        if len(self.piles[2]) == self.nb_disques:
            if self.coups== 2**(self.nb_disques) -1:
                texte = f"Bravo, vos {self.coups} déplacements ont été optimaux !"
            else:
                texte = "Pas mal, mais vous pouvez mieux faire !"
            self.canvas.create_text(self.L//2,self.H//2, text=texte, fill="yellow", tags="texteFin")
            self.block(self.piles[2].top())

    def hanoi_ia(self):
        def hanoi(n, tour_depart, tour_arrivee , tour_intermediaire):
            if n>=1:
                hanoi(n-1, tour_depart, tour_intermediaire, tour_arrivee)

                disque = self.piles[tour_depart].depiler()
                self.piles[tour_arrivee].empiler(disque)
                x0, _, x1, _ = self.canvas.coords(disque) #calcul coords pour déplacement
                largeur = x1-x0
                x = self.X0*(tour_arrivee+1) - largeur//2
                y = self.Y0 - self.H_disque * (len(self.piles[tour_arrivee])-1) -1
                self.canvas.coords(disque, x, y, x+largeur, y-self.H_disque)
                self.canvas.update()
                self.coups +=1
                self.texteCoups.configure(text="coups:"+str(self.coups))
                time.sleep(8 / (2**self.nb_disques))

                hanoi(n-1, tour_intermediaire, tour_arrivee, tour_depart)

        
        self.start(restart=True)
        self.canvas.update()
        time.sleep(1)

        hanoi(self.nb_disques, 0, 2, 1)

        self.gagne()

           
        

jeu = Jeu()