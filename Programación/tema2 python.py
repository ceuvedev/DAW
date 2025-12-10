# Exercici 1 - UD2 - PRG - 1DAMsp

numero1 = int(input("Dona'm el primer número: "))
numero2 = int(input("Dona'm el segon número: "))
print("SUMA: ", numero1 + numero2)
print("RESTA: ", numero1 - numero2)
print("MULTIPLICACIÓ: ", numero1 * numero2)
print("DIVISIÓ: ", numero1 / numero2)

# UD2 - Exercici 5

numero = int(input("Dis-me un número: "))
if numero % 2 == 0:
    print("El número", numero, "és parell!")
    
# UD2 - Exercici 6

numero = int(input("Dis-me un número: "))
if numero % 2 == 0:
    print("El número", numero, "és parell!")
else:
    print("El número", numero, "és imparell!")
    
    
# UD2 - Exercici 7

numero1 = int(input("Dis-me un número: "))
numero2 = int(input("Dis-me altre número: "))

if numero1 >= numero2:
    print (numero1, "és el més gran!")
else:
    print (numero2, "és el més gran!")
    
# UD2 - Exercici 8

n1 = int(input("Introdueix un número enter: "))
n2 = int(input("Introdueix un altre número enter: "))
n3 = int(input("Introdueix un altre número enter: "))

if n1 >= n2 and n1 >= n3: maxim = n1
else:
    if n2 >= n3: maxim = n2
    else: maxim = n3

print("El número més gran és", maxim)

# UD2 - Exercici 9

n1 = int(input("Introdueix un número enter: "))
n2 = int(input("Introdueix un altre número enter: "))
n3 = int(input("Introdueix un altre número enter: "))

# TROBEM EL MÀXIM
if n1 >= n2 and n1 >= n3: maxim = n1
else:
    if n2 >= n3: maxim = n2
    else: maxim = n3

# TROBEM EL MÍNIM
if n1 <= n2 and n1 <= n3: minim = n1
else:
    if n2 <= n3: minim = n2
    else: minim = n3

print("El número més gran és", maxim)
print("El número més petit és", minim)

# UD2 - Exercici 10

n1 = int(input("Introdueix un número enter: "))
n2 = int(input("Introdueix un altre número enter: "))
n3 = int(input("Introdueix un altre número enter: "))

if n1 >= n2 and n1 >= n3:
    minim1 = n2
    minim2 = n3
else:
    if n2 >=3:
        minim1 = n1
        minim2 = n3
    else:
        minim1 = n1
        minim2 = n2

print("Els dos números més petits són", minim1, "i", minim2)

# UD2 - Exercici 11
# Llegir els valors
c1 = int(input("Dona'm un costat del triangle: "))
c2 = int(input("Dona'm un altre costat del triangle: "))
c3 = int(input("Dona'm un altre costat del triangle: "))

# Trobar els valors màxims (hipotenusa) i mínims (catets)
if c1 >= c2 and c1 >= c3:
    hipotenusa = c1
    catet1 = c2
    catet2 = c3
else:
    if c2 >= c3:
        hipotenusa = c2
        catet1 = c1
        catet2 = c3
    else:
        hipotenusa = c3
        catet1 = c1
        catet2 = c2

# Comprovar si els valors formen un triangle
if catet1 + catet2 > hipotenusa:
    print("Els costats", catet1, catet2, hipotenusa, "formen un triangle.")
else:
    print("Els costats", catet1, catet2, hipotenusa, "no formen un triangle.")
    
# UD2 - Exercici 12

nota = int(input("Introdueix la nota: "))

if nota < 0 or nota > 10: print("Error. Nota incorrecta.")
else:
    if nota < 3: print ("Molt deficient")
    else:
        if nota < 5: print ("Insuficient")
        else:
            if nota < 6: print ("Suficient")
            else:
                if nota < 7: print ("Be")
                else:
                    if nota < 9: print ("Notable")
                    else: print ("Excel·lent")
                    
# UD2 - Exercici 13

n1 = int(input("Introdueix un número: "))
operacio = input("Introdueix l'operació a realitzar (S)uma, (R)esta, (M)ultiplicació, (D)ivisió): ")
n2 = int(input("Introdueix un altre número: "))
error = False

# CÀLCULS
if operacio == "S" or operacio == "s": resultat = n1 + n2
else:
    if operacio == "R" or operacio == "r": resultat = n1 - n2
    else:
        if operacio == "M" or operacio == "m": resultat = n1 * n2
        else:
            if operacio == "D" or operacio == "d": resultat = n1 / n2
            else: error = True

# MOSTRAR ELS RESULTATS
if error: print("Error. Operació incorrecta.")
else: print("El resultat de la operació és", resultat)

# UD2 - Exercici 14

numDia = int(input("Introdueix un número de dia de la setmana (1-7): "))

if numDia == 1: print("Dilluns")
elif numDia == 2: print("Dimarts")
elif numDia == 3: print("Dimecres")
elif numDia == 4: print("Dijous")
elif numDia == 5: print("Divendres")
elif numDia == 6: print("Dissabte")
elif numDia == 7: print("Diumenge")
else: print("Error. Número de dia incorrecte.")

# UD2 - Exercici 15

radi = float(input("Introdueix el radi:"))

while radi < 0:
    print("El radi no pot ser negatiu")
    radi = float(input("Introdueix el radi:"))

print("L'area del cercle és:", 3.1416 * radi ** 2)

# UD2 - Exercici 16

anyNaixement = int(input("Any de naixement: "))
anyDefuncio = int(input("Any de defuncio: "))

while anyDefuncio < anyNaixement:
    print("L'any de defuncio no pot ser anterior a l'any de naixement")
    anyDefuncio = int(input("Any de defuncio: "))

# exer 17

n = int(input("Quants nombres vols mostrar? "))

for i in range(n, 0, -1):
    print(i)

print("Ha viscut", anyDefuncio - anyNaixement, "anys")

#exer 18
valor_inicial = int(input("Introdueix un valor inicial: "))
valor_final = int(input("Introdueix un valor final: "))

if valor_inicial < valor_final:
    pas = 3
else:
    pas = -3

for i in range(valor_inicial, valor_final, pas):
    print(i)
    
#exer 19

i = 1
while i <= 10:
    print("9 x", i, "=", 9 * i)
    i = i + 1
    
# exer 21

numero = int(input("Dona'm un número: "))

cDiv = 0

for i in range(numero):
    if numero % (i + 1) == 0:
        cDiv = cDiv + 1
print("El número", numero, "té", cDiv, "divisor(s)")

#exer 22

resposta = int(input("Arrel de 225: "))

intents = 1

while (resposta != 15 and resposta != -15):
    resposta = int(input("Error! Arrel de 225: "))
    intents = intents + 1

print("Ok.", intents, "intents")

# exer 23

multi2 = 0
multi3 = 0
multi2i3 = 0

for i in range(1, 101):
    if (i % 2 == 0):
        multi2 = multi2 + 1
    if (i % 3 == 0):
        multi3 = multi3 + 1
    if (i % 2 == 0 and i % 3 == 0):
        multi2i3 = multi2i3 + 1

print("Entre 1 i 100 hi ha:")
print("\t", multi2, "múltiples de 2")
print("\t", multi3, "múltiples de 3")
print("\t", multi2i3, "múltiples de 2 i de 3")

#exer 24

nombrePositius = 0
nombreNegatius = 0
acabatsZero = 0

num = int(input("Dona'm un número: "))

while (num != 0):
    if (num !=0):
        if (num > 0):
            nombrePositius = nombrePositius + 1
        else:
            nombreNegatius = nombreNegatius + 1
        if (num % 10 == 0):
            acabatsZero = acabatsZero + 1
    num = int(input("Dona'm un número: "))

print(nombrePositius, "nombres positius")
print(nombreNegatius, "nombres negatius")
print(acabatsZero, "nombres acabats en zero")

#exer26

total = 0

while True:
    q = int(input("Dona'm un número: "))
    total = total + q
    if (q == 0):
        break
print("La suma dels números és", total)

#exer 27

alumnes = 23
acumulaNotes = 0

for i in range(alumnes):
    nota = float(input("Dona'm la nota de l'alumne " + str(i+1) + ": "))
    if nota < 0 or nota > 10:
        print("Nota incorrecta")
        while nota < 0 or nota > 10:
            nota = float(input("Dona'm la nota de l'alumne " + str(i+1) + ": "))
    acumulaNotes = acumulaNotes + nota

print("La mitjana de la classe és: ", acumulaNotes/alumnes)

# exer 28

numInicial = int(input("Número inicial: "))
numFinal = int(input("Número final: "))

acumulaParells = 0
acumulaSenars = 0

for i in range(numInicial, numFinal+1):
    print(i)
    if i % 2 == 0:
        acumulaParells = acumulaParells + i
    else:
        acumulaSenars = acumulaSenars + i

print("La suma dels parells és: ", acumulaParells)
print("La suma dels senars és: ", acumulaSenars)

#exer 29

a = int(input("Número inicial: "))
b = int(input("Número final: "))

while a < b:
    print("a =", a, "\tb =", b)
    a = a + 2
    b = b - 3

print("a =", a, "\tb =", b)

#exer 30

print ("Multiplicar sumant...")
a = int(input("Primer número: "))
b = int(input("Segon número: "))

acumulador = 0

for i in range(1, a+1):
    acumulador = acumulador + b

print("El resultat de multiplicar", a, "per", b, "és", acumulador)  

#exer 32

producte = 1

for i in range(1, 41, 2):
    producte = producte * i

print("El producte dels 40 primers nombres senars és", producte)

#exer 33

suma = 0
producte = 1

for i in range (1, 101):
    suma = suma + i
    producte = producte * i

mitjana = suma / 100

print("La suma dels 100 primers nombres és", suma)
print("El producte dels 100 primers nombres és", producte)
print("La mitjana dels 100 primers nombres és", mitjana)

#exer 34

numero = int(input("Introdueix un número: "))

factorial = 1

for i in range(1, numero + 1):
    factorial = factorial * i

print(numero, "!", "=", factorial)

#exer 25

num = int(input("Introdueix un número: "))

trobat = False
i = 2

while (not trobat) and (i < num):
    print (i)
    if num % i == 0:
        trobat = True
    i = i + 1

if trobat == True:
    print("El número", num, "no és primer")
else:
    print("El número", num, "és primer")
