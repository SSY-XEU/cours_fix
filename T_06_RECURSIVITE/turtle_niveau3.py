import turtle as t
from random import randrange
from math import sqrt

####################################
# MODULE t A LIRE
t.bgcolor('black') #change la couleur du background
t.pencolor('green') #change la couleur du crayon
t.colormode(255) # mode rgb
t.pensize(1) #taille du crayon
# t.hidet() # cache le crayon
t.speed("slow") # vitesse du tracé
#t.speed("slowest")
# t.tracer(0,0) # rapide+++

def gotoxy(x,y):
    #déplace la tortue sans trace
    t.up()
    t.goto(x,y)
    t.down()
   

####################################
# LE FLOCON DE KOCH

# t.forward(seg_dec)
# t.left(45)
# t.forward(seg_dec)
# t.left(-90)
# t.forward(seg_dec)
# t.left(90)



def koch(n, long):
    if n == 0:
        t.forward(long)
    else:
        koch(n-1, long/3)
        t.left(60)
        koch(n-1, long/3)
        t.right(120)
        koch(n-1, long/3)
        t.left(60)
        koch(n-1, long/3)




    
#tests        
# gotoxy(0,0)     
# koch(1,150) #étape 1
# gotoxy(80,0)     
# koch(2,150) #étape 2
# gotoxy(160,0)     
# koch(3,150) #étape 3

# le flocon , c'est 3 koch à 120°
# gotoxy(100,200)     
# for i in range (3) :
#     koch(3,150)
#     t.left(-120)

####################################
# L'ARBRE DE PYTHAGORE

def carre(cote):
    for i in range(4) :
        t.forward(cote)
        t.left(90)

def arbre_pythagore(n, cote):
    if n == 0:
        return
    else :
        
        #partie gauche 
        carre(cote)
        t.left(90)
        t.forward(cote)
        t.right(45)
        arbre_pythagore(n-1,cote/sqrt(2))
        #partie droite
        carre(cote)
        t.forward(cote)
        t.left(45)
        t.forward(cote)
        t.left(45)
        arbre_pythagore(n-1,cote/sqrt(2))
        


arbre_pythagore(5, 100)


####################################
# LE TRIANGLE DE SIERPINSKI

def triangle(cote):
    t.down()
    for _ in range(3):
        t.forward(cote)
        t.left(120)
    t.up()
        
def triangle_blanc(cote):
    t.left(60)
    t.begin_fill()
    triangle(cote)
    t.end_fill()
    t.right(60)

def triangle_sierpinski(n,cote):
    if n==0 :
        return
    else :
        triangle(cote)
        t.forward(cote/2)
        triangle_blanc(cote/2)
        triangle_sierpinski(n-1, cote/2)   
# gotoxy(0,-200)     
# t.setheading(0)
# # le triangle plein
# t.fillcolor("black") # couleur de remplissage
# t.begin_fill()
# triangle(100)
# t.end_fill()
# # sierpinski
# # t.pencolor('green') #change la couleur du crayon
# # t.fillcolor("green") # couleur de remplissage
# triangle_sierpinski(1,100)

####################################
# LE TAPIS DE SIERPINSKI

def carre_plein(cote):
    t.begin_fill()
    for _ in range(4):
        t.forward(cote)
        t.left(90)
    t.end_fill()
    

def tapis_sierpinski(n,cote):
    if n==0 :
        return
    else :
        t.forward(cote/4)
        t.left(90)
        t.forward(cote/4)
        t.right(90)
        carre_plein(cote/4)
        tapis_sierpinski(n-1,cote)

# gotoxy(-250,-110) 
# t.setheading(0)    
# # le tapis de départ
# t.pencolor('white')
# t.fillcolor("white")
# carre_plein(200)
# # sierpinski
# t.pencolor('green') #change la couleur du crayon
# t.fillcolor("green") # couleur de remplissage
# tapis_sierpinski(4,200)



t.update() # dessine...
t.exitonclick()
