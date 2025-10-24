Guia de desenvolupament de l’esquema E-R
En el punt anterior hem vist els diferents elements de l’esquema E-R. Ara vorem com
confeccionar este esquema. És a dir, vorem una guia per a desenvolupar l’esquema E-R a
partir dels requeriments (que hem obtingut entrevistant-nos amb el futur usuari de la BD, etc).
Els passos a seguir per a confeccionar l’esquema E-R són:
1. Construir l’esquema E-R pròpiament dit.
1.1. Identificar entitats i atributs
1.2. Identificar les especialitzacions
1.3. Identificar les relacions
1.4. Identificar agregacions
2. Anotar “Altres Restriccions d’Integritat”
3. Anotar “Suposicions”

En un juego de rol hay personajes controlados por personas.

- Las personas son entidades reales y únicas. Tienen nombre, fecha de nacimiento, etc.
- Los personajes son entidades ficticias y repetibles. Tienen nombre, atributos, raza, etc.
    - Estos personajes pueden tener caracteristicas diferentes y particularidades
- La relación de estas dos entidades es que las personas pueden controlar personajes y estos personajes interactuar entre ellos