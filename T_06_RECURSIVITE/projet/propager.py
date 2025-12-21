def propager(M:list, i:int, j:int, val:int)->None:
    # cas de base
    
    # si l'élément en haut fait partie de la composante on propage

    # l'élément en bas fait partie de la composante

    # l'élément à gauche fait partie de la composante

    # l'élément à droite fait partie de la composante


def afficher(M:list)->None:
	for ligne in M:
		print("|",end="")
		for j in range(len(ligne)):
			if j+1==len(ligne) or ligne[j+1]!=ligne[j]:
				print(ligne[j],end="|")
			else:
				print(ligne[j],end=" ")
		print()


#Exemple :
M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]
propager(M,2,1,3)
assert M==[[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]], "erreur !"
afficher(M)



