//ERROR CS1002 = ; manquant

int variable1= 10 ; // atribué variable ne pas oublier d'indiquer le type 
int variable2 = 5 ; 
variable1 += variable2 ;
//Console.WriteLine("variable = "+ variable1) ;

// compter nb voyelle dans un mot
Console.Write("Entrez un nombre : "); //demander a l'utilisateur un mot 
string mot = Console.ReadLine() ; //lire la reponse dans la console
List<char> voyelle = new List<char> {'a', 'e','i','o','u','y'} ; //char 'a' et pas "a"=string  indique une liste de caractére, je peux pas utiliser de type liste ici car je compare dans le for avec mot[i] qui est de type char 
int nb_voyelle = 0 ;

for (int i =0; i<mot.Length ; i++) //i=0; = condition de départ, i<mot.lenght ne pas mettre de = ou de ==, i++ indique comment i change dans ce cas il s'incrémente de 1
{
    if (voyelle.Contains(mot[i])) 
    {
        nb_voyelle ++  ; // = a nb_voyelle += 1 
    }
    
}

 if (nb_voyelle==0)
{
    Console.Write("il n'a aucune voyelle") ; 
}
else 
{
    Console.Write(nb_voyelle) ;
}
//fonction
