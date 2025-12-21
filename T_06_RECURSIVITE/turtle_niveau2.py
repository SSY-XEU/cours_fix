import turtle as t
from random import randrange

####################################
# MODULE TURTLE A LIRE
# https://docs.python.org/3/library/turtle.html
t.bgcolor('black') #change la couleur du background
t.pencolor('green') #change la couleur du crayon
t.colormode(255) # mode rgb
t.pensize(1) #taille du crayon
#t.hideturtle() # chache le crayon
t.speed("slow") # vitesse du tracé

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

####################################
# petits carres 
    
def carre(cote):
    """ trace un carre en faisant des rotations trigo """
    for i in range(4) :
        t.forward(cote)
        t.left(90)

def petits_carres(n,cote):
    if n==1 :
        carre(cote)
    else:
        for i in range (4) :
            t.forward(cote)
            petits_carres(n-1, cote//2)
            t.left(90)
        

# gotoxy(-300,150)
# petits_carres(1,50)
# gotoxy(-200,150)
# petits_carres(2,50)
# gotoxy(-50,150)
# petits_carres(3,50)
# gotoxy(150,150)
# petits_carres(4,50)


####################################
# bulles 
def cercle(x,y,r):
    gotoxy(x,y-r)
    t.circle(r)

def bulles(n,x,y,r):
    if n==1 :
        cercle(x,y,r)
    else :
        cercle(x,y,r)
        xd=x+(r+(r/2))
        yd= y-(r+(r/2))
        cercle(xd,y,r/2)
        cercle(x,yd,r/2)
        bulles(n-1, xd, y, r/2 )
        bulles(n-1, x, yd, r/2 )


                
# t.setheading(0)
# bulles(1,-250,0,40)
# t.setheading(0)
# bulles(2,-100,0,40)
# t.setheading(0)
# bulles(3,50,0,40)
# t.setheading(0)
# bulles(4,200,0,40)

t.exitonclick()
