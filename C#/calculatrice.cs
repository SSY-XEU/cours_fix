using System.Diagnostics;



double nombre1 = Console.ReadLine();
char ope = Console.ReadLine();
double nombre2 = Console.ReadLine();
List<char> operateur = new List<char> ['*','+','-','/'] ;

if (ope == '*')
{
    return nombre1*nombre2 ;
}
else if  (ope== '+')
{
    return nombre1+nombre2  ;
}
else if (ope == '-')
{
    return nombre1-nombre2 ;
}
else 
{
    return nombre1/nombre2 ;
    Debug.Assert (nombre2 !=0); 
    return " zero division " ;
}
Debug.Assert (operateur.Contains(ope)==false) ;
return "entry error" ;

