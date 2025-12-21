import turtle as t
from random import randrange

####################################
# MODULE TURTLE A LIRE
# https://docs.python.org/3/library/turtle.html
t.bgcolor('black') #change la couleur du background
t.pencolor('green') #change la couleur du crayon
t.colormode(255) # mode rgb
t.pensize(1) #taille du crayon
t.hideturtle() # chache le crayon
t.speed("fast") # vitesse du tracé
t.screensize(20000,20000)

# au lancement le stylo se trouve au centre du dessin coords (0,0)
# /!\ par défaut le stylo pointe vers la droite
# t.forward(l) le fait donc avancer de l vers la droite
# t.backward(l) le fait reculer de l vers la gauche sans changer son orientation
# t.left(90) le fait tourner de 90 vers la gauche ( sens trigo )


def gotoxy(x,y):
    """ déplace la tortue sans tracer au point (x,y)"""
    t.up() # soulève le stylo
    t.goto(x,y) # déplace au coords (x,y)
    t.down() # pose le stylo
    
def carre(cote):
    """ trace un carre en faisant des rotations trigo """
    for i in range(4) :
        t.forward(cote)
        t.left(90)

def carre_rec(n,cote):
    if n!=0 :
        carre(cote)
        carre_rec(n-1, cote/2)
    

gotoxy(-200,200)
carre_rec(1,50)

   
def carre_it(n,cote):
    for i in range (n) :
        carre(cote)
        cote = cote/2
        
gotoxy(-100,200)
carre_it(3,50)

# ####################################

def spirale_rec(n):
    long=5*n
    while n!=0 :
        t.right(90)
        t.forward(long)
        spirale_rec(n-1)


gotoxy(+200,100)
spirale_rec(10)

        
# ####################################
# # marches

def marche(l, h):
    for i in range (2):
        t.forward(l)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.forward(l)


def escalier1(n):
    l=10
    h=5*n
    if n!=0 :
        marche(l,h)
        escalier1(n-1)
    


gotoxy(+150,0)
escalier1(10)


def escalier2(n):
    l=10
    h=5*n
    if n!=0 :
        marche(-l,h)
        escalier2(n-1)

gotoxy(+140,0)
escalier2(10)

t.exitonclick()



