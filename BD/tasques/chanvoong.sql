1. Per a familiaritzar-te amb el que té cada taula, fes una select de cadascuna.

SELECT * FROM articles;
SELECT * FROM families;
SELECT * FROM pobles;
SELECT * FROM proveidors;
SELECT * FROM proveir;

2.Mostra els articles da la família ‘VER’ amb un preu entre 2 i 3 euros.

SELECT * FROM articles WHERE familia = "VER" AND preu >2 AND preu <3; 

3. Mostra els articles que no s’hagen mostrat a l’exercici anterior. Nota: fes-ho sense
usar l’operador not.    



4. Codi i nom d’articles que el nom comence per ‘Pera’ i que el codi comence per P i
tinga 4 lletres.

SELECT codi, nom FROM articles WHERE (codi LIKE "P___") AND (nom LIKE "pera%");

5. De cada article mostra el nom en majúscules, el codi de la família, el preu (que està
en euros) i el preu en pessetes, que no haurà de tindre decimals. Els articles apareixeran
ordenats per famílies i, dins de cada família, els articles estaran ordenats pel preu (de major
a menor).
1 euro són 166.386 pessetes.

SELECT UPPER(nom) AS nom, familia, preu, ROUND(preu*166.386) AS preu_pessetes FROM articles ORDER BY familia, preu DESC; 

6.Mostra els codis d’articles proveïts pel proveïdor 2 o pel 4, amb un preu inferior a
70 cèntims. Mostra també el codi del proveïdor i el preu.

SELECT * FROM proveir WHERE pro = 2 OR pro = 4 AND preu < 0.7;

7. Mostra els articles que no tenen posat el preu de venda.

SELECT * FROM articles WHERE preu IS NULL;

8. Mostra quants proveïdors no tenen posat el poble.
        
SELECT COUNT(*) AS q_proveidors_sense_poble FROM proveidors WHERE poble IS NULL;

9. Mostra el preu mig de compra dels articles, el mínim, el màxim i la diferència entre
el màxim i el mínim.

SELECT AVG(preu) AS preu_mig, MIN(preu) AS preu_min, MAX(preu) AS preu_max, (MAX(preu)-MIN(preu)) AS diff_preu FROM articles;

10. Mostra quants articles hi ha, quants tenen preu i quants no tenen preu.

SELECT
  COUNT(*) AS articles, COUNT(preu) AS articles_amb_preu FROM articles;