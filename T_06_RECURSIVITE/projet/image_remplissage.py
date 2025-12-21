#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(100000) # il y a beaucoup d'appel récursifs sur une image

from PIL import Image

def propager(M:object, l:int, h:int, x:int, y:int, lastcolor:tuple,newcolor:tuple)->None:
    if M[x,y] != lastcolor:
        return

    M[x,y]=newcolor

    # l'élément en haut fait partie de la composante

    # l'élément en bas fait partie de la composante

    # l'élément à gauche fait partie de la composante

    # l'élément à droite fait partie de la composante

def outil_remplissage(im:object, x:int, y:int, newcolor:tuple)->None:
	pix = im.load() #tableau de pixels accessible par [x,y]
	l,h= im.width,im.height #dimension image
	lastcolor = pix[x,y] #couleur actuelle (r,g,b,a)
	print("taille image",im.size)
	propager(pix,l,h,x,y,lastcolor,newcolor)


img = Image.open("coeur.png")  

img.show()


outil_remplissage(img,160,50,(255,0,255,255)) #la zone bleue
img.show()

outil_remplissage(img,0,0,(255,255,255,0)) #rendre transparent le tour
img.show()

img.close()




