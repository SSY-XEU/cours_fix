// Permet d’utiliser les fonctionnalités de base de C# (Console, types primitifs comme int, double, string, etc.)
using System;

// Permet d’utiliser les collections génériques comme List<T>
using System.Collections.Generic;

// Fournit des outils de debug 
using System.Diagnostics;

// Permet de gérer les formats culturels (ex: 3.14 vs 3,14)
// en gros c# se base sur en systeme culturel en fonction de ton pc donc si tu est en francais de base pour ecrire un nb  decimal il faudra l'ecrire avec une virgule 
using System.Globalization; // force la culture internationale 

// Déclaration de la classe principale du programme
class Program
{
    // Point d’entrée du programme Le programme commence TOUJOURS par Main
    static void Main()
    {
        // Demande à l’utilisateur de saisir le premier nombre
        Console.Write("Nombre 1 : ");

        // Lit ce que l’utilisateur tape dans la console (string)
        // et le convertit en double
        // InvariantCulture permet d’utiliser le point comme séparateur décimal
        double nombre1 = double.Parse(
            Console.ReadLine(),
            CultureInfo.InvariantCulture
        );

        // Demande à l’utilisateur l’opérateur
        Console.Write("Opérateur (+ - * /) : ");

        // Lecture de l’opérateur sous forme de chaîne
        string ope = Console.ReadLine();

        // Demande le second nombre
        Console.Write("Nombre 2 : ");

        // Conversion du deuxième nombre
        double nombre2 = double.Parse(
            Console.ReadLine(),
            CultureInfo.InvariantCulture
        );

        // Liste des opérateurs autorisés
        List<string> operateurs = new List<string> { "*", "+", "-", "/" };

        // Vérifie si l’opérateur entré existe dans la liste
        if (!operateurs.Contains(ope))
        {
            // Message d’erreur si l’opérateur est invalide
            Console.WriteLine("Opérateur invalide");
            return; // Stoppe le programme
        }

        // Vérification de la division par zéro
        if (ope == "/" && nombre2 == 0)
        {
            Console.WriteLine("Division par zéro interdite");
            return;
        }

        // Variable qui contiendra le résultat final
        double resultat = 0;

        // Effectue le calcul selon l’opérateur choisi
        if (ope == "*")
            resultat = nombre1 * nombre2;
        else if (ope == "+")
            resultat = nombre1 + nombre2;
        else if (ope == "-")
            resultat = nombre1 - nombre2;
        else if (ope == "/")
            resultat = nombre1 / nombre2;

        // Affiche le résultat à l’écran
        Console.WriteLine("Résultat : " + resultat);
    }
}
