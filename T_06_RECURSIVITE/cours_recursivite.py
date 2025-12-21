import time,sys
from math import sqrt

#############################
# compte à rebours

# def compte_a_rebours(n:int):
#     if n <= 0:
#         print('Décollage !')
#     else:
#         print(n,end=" ")
#         compte_a_rebours(n-1)
        
# compte_a_rebours(5)

# #version itérative
# def compte_a_rebours_iter(n:int):
#     while n>0:
#         print(n,end=" ")
#         n = n-1
#     print('Décollage !')

# compte_a_rebours_iter(5)

##############################
# palindrome
# def palindrome(texte:str):
#     if len(texte) <=1 : #cas de base 
#         return True 
#     if texte[0] != texte[-1] :
#         return False 
#     else :
#        return palindrome(texte[1:-1])           
# print(palindrome("kayak"))
# print(palindrome("kaya"))
# print(palindrome("engagelejeuquejelegagne"))
# print(palindrome("sibenetetualaustaxatsualautetenebis")) #latin
# print(palindrome("anastas mum satsana")) #turc
# https://fr.wikipedia.org/wiki/Palindrome

#############################
##puissance
def puissance_iter(x:int, n:int):
    puiss =1
    for i in range(n):
        puiss=puiss*x
    return puiss

def puissance_a(x:int, n:int ):
    if n==  0 : #cas de base 
        return 1
    else :
        return x*puissance_a(x, n-1)

def puissance_b(x, n):
    if n==0 : #cas de base 
        return 1
    elif n==1 : #cas de base 2
        return x
    else :
        return x*puissance_b(x, n-1)

def puissance_rapide(x:int, n:int):
    if n == 0 :
        return 1
    if n%2 == 0 :          
        return puissance_rapide(x*x, n/2)
    else :
        return x*((puissance_rapide(x*x, (n-1)/2)))




# for fonction in (puissance_iter,puissance_a, puissance_b, puissance_rapide):
#     for n in (0,1,8,10):
#         print(fonction(2,n),end=" ")
# print()

# print("recursion limit",sys.getrecursionlimit())
# sys.setrecursionlimit(5000)
# # test vitesse avec 5**270 !!!!
# for fonction in (puissance_iter, puissance_b, puissance_rapide):
#     start = time.time()
#     r = fonction(5,270)
#     stop = time.time() 
#     print(r)    
#     print(fonction.__name__,(stop-start)*1000,"ms")


# #############################
# # approcher le nombre pi

def u(n):
    if n==0 :
        return sqrt(2)
    else :
        return sqrt(2+u(n-1))


def v(n):
    if n==0 :
        return 2
    else :
        return 2*(v(n-1)/u(n-1))

    
print("pi=",v(5))
print("pi=",v(500))


# ##############################
# # syracuse
def syracuse(u_n):
    while u_n > 1 :
        if u_n%2 == 0 :
            return 2*syracuse(u_n-1)
        else : 
            return 3*syracuse(u_n-1)-1
    return 1


print("syracuse : ",syracuse(731))




