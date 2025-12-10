sumaNotes = 50
quantAlumnes = 0

'''
a) No donaria error la divisió per 0 ja que no s'executaria
la part dreta de l'and perquè la part esquerra ja és falsa.
''' 
if (quantAlumnes>0) and (sumaNotes/quantAlumnes >= 5):
    print("Nota mitja aprovada") 
else:
    print("Nota mitja no aprovada")

'''
b) Sí que donaria error la divisió per 0 ja que sí que s'executarà
la part esquerra de l'and (ja que sempre s'avalua d'esquerra a dreta)
''' 
if (sumaNotes/quantAlumnes >= 5) and (quantAlumnes>0):
    print("Nota mitja aprovada") 
else:
    print("Nota mitja no aprovada")'''
2. En el següent programa Python, què valdrà cada 
variable després de cada assignació?
'''

# Nota: la idea de l'exercici és saber el resultat sense fer el programa

a=6
b=3
b=1+b       # a=6       b=4 
print("a=", a, "\tb=", b)
a=a/b       # a=1.5     b=4 
print("a=", a, "\tb=", b)
b=6//b+b    # a=1.5     b=6//4 + 4  --> b =1 + 4 --> b = 5
print("a=", a, "\tb=", b)

'''
3. En el següent programa Python, què valdrà cada 
variable després de cada assignació?
'''

# Nota: la idea de l'exercici és saber el resultat sense fer el programa

a=4
b = 20
b += 23     #a= 4    b= 43
print("a=", a, "\tb=", b)
b //= 2     # a= 4    b= 21
print("a=", a, "\tb=", b)
a -= 2      # a= 2    b= 21
print("a=", a, "\tb=", b)
a *= b + 2  # a= 46   b= 21
print("a=", a, "\tb=", b)
a %= b      # a= 4    b= 21
print("a=", a, "\tb=", b)
a**= b-19   # a= 16   b= 21
print("a=", a, "\tb=", b)
'''
5. Suposem que tenim estes variables en un programa en Python:
a = 12
x = 2.5
y = 0.6
Indica de quin és el valor de cadascuna de les següents expressions:
'''

# Nota: la idea de l'exercici és saber el resultat sense fer el programa

a = 12
x = 2.5
y = 0.6
print("a)",	a + x)
print("b)",	x + y)
print("c)",	int(x) + y)
print("d)",	int(x) + int(y))
print("e)",	int(x + y))
print("f)",	a / 4)
print("g)",	a // 4)
print("h)",	a % 4)
print("i)",	a + x * 2)
print("j)",	a / a - 2)
print("k)",	a ** 2 + 1)
print("l)",	a < x  or  y < x)
print("m)",	not (a < x))
print("n)",	(a >= x) and (y<=a))
'''
6. Fes un programa que pregunte quants anys té algú i que mostre per pantalla 
la quantitat d’anys que falten per a la majoria d’edat i per a jubilar-se.
'''

anys = int(input("Quants anys tens?"))
print("Et falten", 18-anys, "per a la majoria d'edat i", 65-anys, "per a jubilar-te.")

'''
Nota: traurà xifres negatives si ja eres major d'edat o estàs jubilat
però això ja ho controlarem quan veiem les condicions (if)
''''''
7. Programa que pregunte per la base i l’altura d’un triangle 
i mostre per pantalla l’àrea d’eixe triangle.
'''
print("Càlcul de l'àrea d'un triangle.")
base = float(input("Base:"))
altura = float(input("Altura:"))
area = base * altura / 2
print("Àrea:", area)'''
8. Demana per teclat les dades de 2 llibres: títol, autor i preu (permet decimals). 
Després cal mostrar les dades en forma de taula: 30 caràcters per al títol, 
20 per a l'autor i 10 per al preu (incloent 2 decimals). Per exemple:
		Diccionari per a ociosos      Joan Fuster              10.40
		L'home manuscrit              Manuel Baixauli          14.25   
		Un nu                         Josep Palàcios            9.50
'''

# ENTRADA DE DADES
print("Dis-me les dades de 2 llibres:")

titol1 = input("\nTítol:")
autor1 = input("Autor:")
preu1  = float(input("Preu:"))

titol2 = input("\nTítol:")
autor2 = input("Autor:")
preu2  = float(input("Preu:"))

print()

# EIXIDA DE RESULTATS
print(f"{titol1:30} {autor1:20} {preu1:10.2f}")
print(f"{titol2:30} {autor2:20} {preu2:10.2f}")

'''
Nota: si introduírem un títol de més de 30 caràcters o un títol de més de 20
ens desquadraria. Ja veurem com solucionar-ho.
'''
'''
9. Demana per teclat la data de hui (separat amb el caràcter / ). 
Després escriu la data amb el format d'este exemple: "4 del 8 de 2020".
'''
data = input("Escriu la data de hui en format dd/mm/yyyy: ")
dia, mes, any = data.split('/')
print("Hui és", dia, "del", mes, "del", any)

'''
Nota:
dia, mes i any seran de tipus cadena. Per tant, si hem introduït 08/07/1970
eixirà en pantalla:
08 del 07 del 1970
Si volguérem que no eixira el 0 (del mes i de l'any) caldria tractar eixes variables
com a números, no com a text. Per tant, després de la instrucció de l'split, caldria fer:
dia = int(dia)
mes = int(mes)
any = int(any)

Ara eixirà:
8 del 7 del 1970
'''

'''
1. Escriu el resultat de les següents expressions:
'''
# Nota: este exercici està pensat per a resoldre'l sense fer el programa este.
# Ací està fet per a comprovar què valdrà cada expressió.

print("a) ", 5 / 2 + 17 % 3)
print("b) ", 3 * 6 / 2 + 18 / 3 * 2)
print("c) ", 42* 2 / 3 / (5 + 2))
print("d) ", ((5+3)/2*3)/2-int(28.7)//4+29%3*4)
print("e) ", 3 <= 4)
print("f) ", 45 <= 7 or not(5 >= 7))
print("g) ", (8 * 2 < 5 or 7 + 2 > 9) and 8 - 5 < 18)
print("h) ", (2 * 7 > 5 or 7 / 2 == 3) and (7 > 25 or not True) and True)
print("i) ", 35 > 47 and 9 == 9 or 35 != 3 + 2 and 3 >= 3)
print("j) ", 9 == 15 or 8 != 5 and 7 == 4)
print("k) ", 8 > 8 or 7 == 7 and not(5 < 5))
print("l) ", 4 + 2 < 8 and 24 + 1 == 25 or True)'''
2.	Escriu una expressió on s’especifique que una variable numèrica de nom quant 
siga menor o igual que 500 i múltiple de 5 però distinta de 100.
'''
print("Dis-me una quantitat menor o igual que 500 i múltiple de 5 però distinta de 100: ")
quant = int(input())

print(quant<=500 and quant%5==0 and quant!=100)

# Nota: este exercici només demanava l'expressió: quant<=500 and quant%5==0 and quant!=100
# però s'ha fet eixe tros de programa per comprovar que funciona.'''
3.	Troba els errors en el següent programa que calcula l’àrea d’un cercle a partir del radi. 
Després copia'l amb les correccions, compila’l i executa’l.
'''

'''
Solució:
- Cal definir pi abans d'usar-lo (2a instrucció hauria d'anar la 1a)
- El 3,14 ha d'anar amb punt: 3.14
- Tot el text del print hauria d'anar entre cometes. En este cas, dobles, 
ja que dins té un apòstrof (cometa simple) i hi hauria confusió.
- El punt i coma no està mal (Python el permet) però està de més i sobraria.
- El valor arreplegat amb l'input hauria de convertir-se a número (int o float)
ja que després farem operacions matemàtiques amb ell.
- El comentari amb 3 cometes caldria tancar-lo amb altres 3 cometes (o posar # davant)
- La variable radio hauria de dir-se radi, i PI en minúscules (ja que estaven definides així).
- L'últim print hauria d'anar entre cometes dobles (simples no perquè hi ha un apòstrof).
- La variable area hauria de dir-se area.
- Falta el % davant la variable 'area' en el print

'''

# Programa corregit:

pi = 3.14
print("pi=", pi)
print("Programa de càlcul de l’àrea d’un cercle") 
radi = float(input('Dis-me el radi: '))
# Calcular i imprimir l’àrea
area = pi * radi**2
print("\n\nL'àrea del cercle és: %.2f\n" % area)

'''
4. Sense executar el programa, digues què mostrarà per pantalla:
'''

# Nota: L'objectiu d'este exercici era saber què mostraria però sense executar el programa

a=10
b=3
c = a/b             # c = 3.333333...
d = a<b and b<c     # d = False and ... --> d = False
a += a + b          # a = a + (a + b)   --> a = 10 + (10 + 3)   --> a = 23
b = float(a//b)     # b = float(23//3)  --> b = float(7)        --> b = 7.0
print(a, b, c, d)   # 23 7.0 3.3333333333333335 False'''
5. Contesta les següents qüestions tipus test:

a) Els tipus primitius en Python són:
    1. bool, char, short, int, long, float, double
    2. int, float, bool, str   ---> CORRECTE
    3. caràcters, variables i constants
b) Es definix a=5, b=2 i c=0. Quin serà el valor de c després d'esta instrucció: c=a>b
    1. 3
    2. 2
    3. True ---> CORRECTE 
    4. False
    5. Error
c) Quin és el valor d'esta expressió: 10 / int(4.5):
    1. 2
    2. 2.5  ---> CORRECTE (ja que és 10 / 4)
    3. 3
    4. Altra cosa
'''

