'''
1. Fes un programa que calcule les solucions reals de l’equació de 2n grau 
ax2 + bx + c = 0
'''

'''
Nota: és important controlar possibles errors que facen avortar el programa, com:
- Arrel quadrada d'un número negatiu
- Divisions per 0 --> Ho controlarem en altra versió del programa (v2)

Per això s'han fet els controls del programa:
'''

import math
# ENTRADA DE DADES
print("Resolució equació 2n grau: ax2 + bx + c = 0")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

# CÀLCULS I MOSTRAR RESULTATS

dinsArrel = b**2-4*a*c  # Ho posem en una variable per no repetir el càlcul 3 voltes

if dinsArrel < 0 :
    print("No té solució")
else: 
    x1 = (-b + math.sqrt(dinsArrel)) /  ( 2 * a)
    x2 = (-b - math.sqrt(dinsArrel)) /  ( 2 * a)
    if (x1==x2):
        print("Només té 1 solució:", x1)
    else:
        print("Té 2 solucions:")
        print(x1)
        print(x2)
    
'''
Nota:
A més, sempre s'ha de tindre en compte que no hi haja divisions per 0
ja que farien avortar el programa.
En altre fitxer hi ha una versió ampliada que contempla este cas i 
com seria la solució (requerix un poc de coneixement matemàtic).
''''''
1. Fes un programa que calcule les solucions reals de l’equació de 2n grau 
ax2 + bx + c = 0
'''

'''
Nota: és important controlar possibles errors que facen avortar el programa, com:
- Arrel quadrada d'un número negatiu
- Divisions per 0 --> En esta versió controlem també eixa part

Per això s'han fet els controls del programa:
'''

import math
# ENTRADA DE DADES
print("Resolució equació 2n grau: ax2 + bx + c = 0")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

# CÀLCULS I MOSTRAR RESULTATS
if (a == 0):
    print("No és de 2n grau, ja que en eixe cas és del tipus: bx + c = 0")
    if (b == 0):
        if (c == 0):
            print("Infinites solucions. L'equació es compleix per a qualsevol valor de la x")
        else:
            print("No té solució ja que per a cap valor de x es compleix que", c, "= 0")
    else:
        print("Solució:", -c/b)
else:
    dinsArrel = b**2-4*a*c  # Ho posem en una variable per no repetir el càlcul 3 voltes
    if dinsArrel < 0 :
        print("No té solució")
    else: 
        x1 = (-b + math.sqrt(dinsArrel)) /  ( 2 * a)
        x2 = (-b - math.sqrt(dinsArrel)) /  ( 2 * a)
        if (x1==x2):
            print("Només té 1 solució:", x1)
        else:
            print("Té 2 solucions:")
            print(x1)
            print(x2)'''
2. Demana una nota amb decimals i mostra el text corresponent: 
“ins”, “suf”, “bé”, “not” o “exc”. O bé "error" si la nota no està entre 0 i 10.
'''

nota = float(input("Nota:"))

if nota<0 or nota>10:
    print("error")
elif nota<5:
    print("ins")
elif nota<6:
    print("suf")
elif nota<7:
    print("bé")
elif nota<9:
    print("not")
else:
    print("exc")'''
3. Calculadora. Fes un programa que llija de teclat 2 números 
i una operació aritmètica (S/R/P/D). 
El programa farà el càlcul i imprimirà el resultat.
'''
print("Calculadora a partir de 2 números i una operació.")
a = float(input("Número:"))
b = float(input("Altre número:"))
op = input("Operació (s, r, p, d):")

ok = True
if op=='s':
    print("El resultat de l'operació és", a+b)
elif op=='r':
    print("El resultat de l'operació és", a-b)
elif op=='p':
    print("El resultat de l'operació és", a*b)
elif op=='d':
    if (b==0):
        print("No podem dividir per 0")
    else:
        print("El resultat de l'operació és", a/b)
else:  
    print("Error en el codi d'operació")

'''
Nota: 
No convé repetir tantes voltes el mateix missatge (El resultat de l'operació és...)
Millor guardar el resultat en una variable i mostrar al final el missatge amb eixa variable.
Està resolt en la versió v2.
''''''
3. Calculadora. Fes un programa que llija de teclat 2 números 
i una operació aritmètica (S/R/P/D). 
El programa farà el càlcul i imprimirà el resultat.
'''
print("Calculadora a partir de 2 números i una operació.")
a = float(input("Número:"))
b = float(input("Altre número:"))
op = input("Operació (s, r, p, d):")

if op=='s':
    res = a+b
elif op=='r':
    res = a-b
elif op=='p':
    res = a*b
elif op=='d':
    if (b==0):
        res = "error"
        print("No podem dividir per 0")
    else:
        res = a/b
else:  
    res = "error"   
    print("Error en el codi d'operació")

if res != "error":
    print("El resultat és", res)

'''
Hem agafat la variable 'res' tant per a guardar un número (el resultat de l'operació)
com per a guardar un text ("error").

Això ho podem fer en Python perquè el tipificat és dinàmic: una mateixa variable pot
ser entera en un moment del programa i de tipus cadena en altre moment.

Però no es podria fer en llenguatges com Java, de tipificat estàtic,
on una variable es declara d'un tipus determinat i ja no pot canviar de tipus 
al llarg del programa.

En la versió v3 està resolt usant:
- una variable entera per al resultat: num
- una altra variable (booleana) per a indicar si ha anat bé l'operació: ok
'''
'''
3. Calculadora. Fes un programa que llija de teclat 2 números 
i una operació aritmètica (S/R/P/D). 
El programa farà el càlcul i imprimirà el resultat.
'''
print("Calculadora a partir de 2 números i una operació.")
a = float(input("Número:"))
b = float(input("Altre número:"))
op = input("Operació (s, r, p, d):")

ok = True   # De moment, tot OK. És a dir: no hi ha cap error

if op=='s':
    res = a+b
elif op=='r':
    res = a-b
elif op=='p':
    res = a*b
elif op=='d':
    if (b==0):
        ok = False  # Si passem per ací ja no està tot OK. No haurem de mostrar el resultat
        print("No podem dividir per 0")
    else:
        res = a/b
else:  
    ok = False  # Si passem per ací ja no està tot OK. No haurem de mostrar el resultat
    print("Error en el codi d'operació")

if ok:      # És el mateix que fer   if ok==True:
    print("El resultat és", res)

'''
5. Fes un programa que mostre el màxim de 3 números introduïts per teclat.
'''
print("Dis-me 3 números i et diré el major")
a = int(input("Número: "))
b = int(input("Número: "))
c = int(input("Número: "))

if (a>b and a>c):
    major = a
elif (b>c):
    major = b
else:
    major = c

print("El major és el", major)'''
6. Demana una nota sense decimals i mostra el text corresponent: 
“ins”, “suf”, “be”, “not” o “exc”. O bé "error" si la nota no està entre 0 i 10.
'''

nota = int(input("Nota: "))

if nota<0 or nota>10:
    print("error")
elif nota <= 4:
    print("ins")
elif nota == 5:
    print("suf")
elif nota == 6:
    print("bé")
elif nota == 7 or nota == 8:
    print("not")
else:
    print("exc")

'''
7. Demana per teclat el pes d'una persona, en quilos. 
Tant si el pes és menor de 10 kg, com si és > 200 kg, ha de mostrar error. 
En cas contrari mostrarà el pes en grams i també un missatge: 
"flac" si és menor de 50 kg, "normal" si està entre 50 i 100 kg, o "sobrepés" en altre cas.
'''

pes = float(input("Quants kg peses? "))
if pes<10 or pes>200:
    print("Error. Pes incorrecte")
else:
    print("Peses", pes * 1000, "grams")

    if pes < 50:
        estat = "Flac"
    elif pes <= 100:
        estat = "Normal"
    else:
        estat = "Sobrepés"

    print("Estat:", estat)

'''
8. Programa que, repetidament, mostre un menú amb 4 opcions 
(Demanar temperatura / Pujar 1 grau / Baixar 1 grau / Eixir), 
que demane per teclat una opció i l'execute. 
Cada vegada que s'augmente o disminuïsca, també es mostrarà la nova temperatura. 
Després del bucle es mostrarà quantes vegades s'ha canviat la temperatura.
'''
qMod = 0    # Quantitat de Modificacions de la temperatura

exisTempInicial = False # Per a no modificar la temperatura si encara no se n'havia posat cap

opcio = -1  # Truquet per a entrar al bucle la 1a vegada

while (opcio != 4):

    print("MENÚ D'OPCIONS")
    print("1. Introduir temperatura nova")
    print("2. Pujar temperatura")
    print("3. Baixar temperatura")
    print("4. Eixir")

    opcio = int(input("Opció: "))

    if opcio==1:
        temp=int(input("Quants graus vols? "))
        qMod += 1
        exisTempInicial = True

    elif opcio==2 or opcio==3:
        if not exisTempInicial:
            print("Primer has de posar una temperatura. ")
        else:
            if opcio==2:
                temp += 1
            else:
                temp -= 1
            qMod += 1
            print("Ara fa", temp, "graus.")
    
    elif opcio==4:
        pass 
        # Es posa el 'pass' en els llocs on Python ens obliga a posar una acció
        # però no en volem posar cap (El 'pass' no fa absolutament res).
    else:
        print("Opció incorrecta.")

if qMod > 0:
    print("Han hagut", qMod, "canvis en la temperatura.")
else:
    print("No han hagut canvis en la temperatura.")'''
9. Mostra els números del 0 al 10.
'''
for i in range(11):
    print(i, end=" ")   # L'"end" és per a que no faça salt de línia en cada número

print() # Per a fer un salt de línia al final de tot
'''
10.Mostra la taula de multiplicar del 3.
'''
for i in range(1, 11): 
    print("3 x", i, "=", 3*i)
'''
11.Mostra els números parells del 40 fins al 0 (inclòs).
'''
for i in range(40, -1, -2):  # -1 (i no 0) perquè el range mai arriba al valor final
    print(i, end=" ")

print()'''
12. Programa que demane una taula de multiplicar i la mostre.
'''
taula = int(input("Número de taula de multiplicar: "))
for i in range(1, 11): 
    print(taula, "x", i, "=", taula*i)'''
14.	Programa que calcule el màxim, mínim i mitjana de 10 números entrats per teclat.
'''

print("Dis-me 10 números i et diré quin és el màxim.")

# Necessitem un número màxim inicial per a poder comparar després.
# No podem dir que siga el 0 ja que tots els números introduïts podrien ser negatius.
max = int(input("Número: ")) 

# Demanem 9 números perquè un ja l'hem demanat abans.
for i in range(9):           
    num = int(input("Número: "))
    if num > max:
        max = num

# Mostrem el resultat:
print("El màxim és el", max)
'''
14.	Programa que calcule el màxim, mínim i mitjana de 10 números entrats per teclat.
'''

print("Dis-me 10 números i et diré quin és el màxim, el mínim i la mitjana.")

# Necessitem un número màxim inicial per a poder comparar després.
# No podem dir que siga el 0 ja que tots els números introduïts podrien ser negatius.
max = int(input("Número: ")) 

# Iniciem també el mínim. El primer valor que ens donen de moment és el màxim i el mínim.
min = max  

# Iniciem l'acumulador de sumes per a calcular la mijana:
sum = 0

# Demanem 9 números perquè un ja l'hem demanat abans.
for i in range(9):           
    num = int(input("Número: "))
    if num > max:
        max = num
    elif num < min:
        min = num
    sum += num
    

# Mostrem el resultat:
print("\nRESULTATS:")
print("Màxim:", max)
print("Mínim:", min)
print("Mitjana:", sum/10)
'''
15.	Programa que mostre les taules de multiplicar del 2 al 9.
'''
for taula in range(2, 10):
    print("\n- TAULA DEL", taula, "-")
    for i in range(1, 11): 
        print(taula, "x", i, "=", taula*i)'''
16.	Programa que calcule el factorial d’un número introduït per teclat ( n! ) 
tenint en compte que:
		0! = 1
    	n! = n * (n-1) * (n-2) * ... * 2 * 1     (sent n > 1)
	Feu-ho amb diferents solucions: 
a) Amb un for recorrent els números des de l'1 fins n
b) Amb un for recorrent els números des d'n fins a 1
c) Amb un while recorrent els números des de l'1 fins n
d) Amb un while recorrent els números des d'n fins a 1
'''

num = int(input("Dis-me un número i et calcularé el seu factorial: "))

print("\na) Amb un for recorrent els números des de l'1 fins n: ", end="")
fac = 1
for i in range(1, num+1):
    fac *= i
print(fac)

print("\nb) Amb un for recorrent els números des d'n fins a 1: ", end="")
fac = 1
for i in range(num, 1, -1):
    fac *= i
print(fac)

print("\nc) Amb un while recorrent els números des de l'1 fins n: ", end="")
fac = 1
i = 1
while i<= num:
    fac *= i
    i += 1
print(fac)

print("\nd) Amb un while recorrent els números des d'n fins a 1: ", end="")
fac = 1
i = num
while i >=1 :
    fac *= i
    i -= 1
print(fac)'''
17.	Programa en Python que demane les notes dels alumnes 
(números enters i positius entre 0 i 10) 
i que després mostre quantes notes s'han introduït i la nota mitjana. 
Per a parar d'introduir notes caldrà posar la nota 11, 
que no es tindrà en compte per als càlculs.
'''

'''
Nota: El programa es podria fer sense break ni continue, 
però ho farem així per a vore el seu funcionament.
'''

# Inicialització de comptador i acumulador
notes = 0
suma = 0

# Demanar dades i fer càlculs
while True:
    # Introducció de la nota per teclat
    nota = input("Dis-me una nota (11 per a eixir):")

    # Comprovacions de nota OK
    if not nota.isnumeric():
        print("Han de ser números enters positius. Torna a provar.")
        continue   # No executa la part "que queda" del bucle i torna "dalt" (al while)

    nota = int(nota) 
    if nota > 11:
        print("La nota màxima és 10. Torna a provar.")
        continue   # No executa la part "que queda" del bucle i torna "dalt" (al while)

    # Si volem acabar 
    if nota == 11:
        print("Ja no et demane més notes. Vaig a eixir del bucle.")
        break      # Se n'ix del bucle (va a la següent instrucció del final del bucle)

    # Si tot ha anat bé, farem els càlculs 
    print("Nota introduïda ok:", nota)
    notes += 1
    suma += nota
## Fi del bucle

# Mostrem els resultats
print(notes, "notes introduïdes.")
print("Nota mitja:", suma/notes)
'''
18.	Programa que demane 10 números (positius i/o negatius) 
i mostre la mitjana només dels positius. 
Fes-ho a l'estil de l'exercici resolt anterior, per a fer ús del continue.
'''

print("Dis-me 10 números (positius i/o negatius) i et diré la mitjana dels positius.")
sumaPos = 0
comptPos = 0
for i in range(10):
    num = float(input("Número: "))

    if (num<0):
        continue   
        # Si és menor que 0 no s'executen les instruccions de baix 
        # i tornarà a "pujar al for", on la 'i' agafarà el següent valor.

    sumaPos += num
    comptPos += 1 

# Recordem que sempre cal evitar divisions per 0 per a que el programa no avorte.
if (comptPos == 0):
    print("No puc calcular la mitjana dels positius perquè no hi ha cap número positiu.")
else:
    print("Mitjana dels positius:", sumaPos / comptPos)

'''
Nota: s'haguera pogut resoldre sense el "continue", usant este if en compte de l'altre:

for i in range(10):
    num = float(input("Número: "))

    if (num>=0):
        sumaPos += num
        comptPos += 1 
''''''
20.	Fes un programa en Python que simule un caixer automàtic. 
Es demana per teclat la clau contínuament mentre no siga correcta (1234). 
Però com a molt són 5 intents. 
Després del bucle caldrà indicar si s'han superat els intents o si s'ha encertat la clau. 
a) Fes el programa usant un while amb break i l'else del while.
b) Fes el programa usant un for
c) Fes el programa usant un while sense break (ni l'else del while, clar).
'''

# a) Fes el programa usant un while amb break i l'else del while.
i = 0  # La 'i' compta els intents d'encertar la clau
while i<5:
    comb = input("Clau secreta: ")
    i += 1
    if comb == "1234":
        print("Exacte! Ho has encertat en", i, "intents.")
        break  # Com ja s'ha encertat, eixim del bucle (sense esperar els 5 intents)

else:   # Este "else" és del "for", no de l'"if"
    print("No ho has encertat.")
    
print("Adéu")'''
20.	Fes un programa en Python que simule un caixer automàtic. 
Es demana per teclat la clau contínuament mentre no siga correcta (1234). 
Però com a molt són 5 intents. 
Després del bucle caldrà indicar si s'han superat els intents o si s'ha encertat la clau. 
a) Fes el programa usant un while amb break i l'else del bucle.
b) Fes el programa usant un for amb break i l'else del bucle.
c) Fes el programa usant un while sense break ni l'else del bucle.
'''

# b) Fes el programa usant un for

for i in range(1, 6):
    comb = input("Clau secreta: ")
    if comb == "1234":
        print("Exacte! Ho has encertat en", i, "intents.")
        break  # Com ja s'ha encertat, eixim del bucle (sense esperar els 5 intents)

else:   # Este "else" és del "for", no de l'"if"
    print("No ho has encertat.")
    
print("Adéu")
'''
20.	Fes un programa en Python que simule un caixer automàtic. 
Es demana per teclat la clau contínuament mentre no siga correcta (1234). 
Però com a molt són 5 intents. 
Després del bucle caldrà indicar si s'han superat els intents o si s'ha encertat la clau. 
a) Fes el programa usant un while amb break i l'else del while.
b) Fes el programa usant un for
c) Fes el programa usant un while sense break (ni l'else del while, clar).
'''

# c) Fes el programa usant un while sense break (ni l'else del while, clar).

i = 0       # La 'i' compta els intents d'encertar la clau.
comb = ""   # Li posem un valor inicial per a que entre al bucle.

# Bucle demanant la clau mentre no se superen els intents i no s'encerte la clau.
while i < 5 and comb != "1234":
    comb = input("Clau secreta: ")
    i += 1

# Quan eixim del bucle mostrem un missatge o altre depenent del motiu d'haver eixit del bucle.
# Compte en no posar la condició de i==5, ja que potser s'ha encertat en l'últim intent.
if comb == "1234":
    print("Exacte! Ho has encertat en", i, "intents.")
else:   # Este "else" és del "for", no de l'"if"
    print("No ho has encertat.")
    
print("Adéu")