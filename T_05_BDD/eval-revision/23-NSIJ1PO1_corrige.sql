--1a)
SELECT nom, adresse, telephone FROM Equipe WHERE id_equipe = 5;
--1b)
--domaine text : mixe des nombres et des espaces
--1c)
SELECT nom, adresse, telephone FROM Equipe WHERE id_equipe = 5;
--1d)
SELECT COUNT(*) FROM Equipe;
--1e)
SELECT nom from Equipe ORDER by nom asc;
--1f)
UPDATE Equipe set nom="Tarbes" where id_equipe=4;
--q2a)
--cet attribut fait référence à  l'attribut id_equipe de la table Equipe
--2b)
--car l'attribut id_equipe est référencé dans la table joueuse ( clé étrangère ). Il faudrait d'abord réaffecter les joueuses dans d'autres équipes
--2c)
SELECT Joueuse.nom, prenom from Joueuse
JOIN Equipe on Joueuse.id_equipe=Equipe.id_equipe
where Equipe.nom="Angers"
ORDER by Joueuse.nom;
--3a)
CREATE TABLE "Match" (
	"id_match"	INT,
	"date"	TEXT,
	"id_equipe_dom"	int,
	"id_equipe_dep"	int,
	"score_dom"	int,
	"score_dep"	INT,
	FOREIGN KEY("id_equipe_dep") REFERENCES "Equipe"("id_equipe"),
	PRIMARY KEY("id_match"),
	FOREIGN KEY("id_equipe_dom") REFERENCES "Equipe"("id_equipe")
);
--3b)
INSERT INTO Match values(10, "23/10/2021", 3, 6, 73, 78);
--4a)
CREATE TABLE "Statistiques" (
	"id_joueuse"	int,
	"id_match"	int,
	"points"	int,
	"rebonds"	int,
	"passes_decisives"	int,
	PRIMARY KEY("id_joueuse","id_match"),
	FOREIGN KEY("id_joueuse") REFERENCES "Joueuse"("id_joueuse")
);
--4b)
SELECT Equipe.nom,Joueuse.nom,prenom,points,rebonds,passes_decisives FROM joueuse
JOIN Equipe ON Joueuse.id_equipe=Equipe.id_equipe
JOIN Statistiques ON Statistiques.id_joueuse=joueuse.id_joueuse
WHERE id_match=53;