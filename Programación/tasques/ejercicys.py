# import math

# n1 = int(input("Valor de a"))
# n2 = int(input("Valor de b"))
# n3 = int(input("Valor de c"))

# dinsArrel = (b*b) - (4*a*b)

# if dinsArrel >= 0:
#     x1 = ((-1*b) + math.sqrt(dinsArrel))/(2*a)
#     x2 = ((-1*b) - math.sqrt(dinsArrel))/(2*a)
#     print(f"x1 = {x1}")

# operacion = input(f"Que vols ver (Sumar, Restar, Multiplicació, Divisió)").upper()

# if operacion == "S":
#     print(f"{n1} + {n2} = {n1+n2}")
# elif operacion == "R":
#     print(f"{n1} + {n2} = {n1-n2}")
# elif operacion == "M":
#     print(f"{n1} + {n2} = {n1*n2}")
# elif operacion == "D":
#     if n2 != 0:
#         print(f"{n1} + {n2} = {n1/n2}")
#     else: 
#         print("Divisió zero! No es pot")
# else: 
#     print("Operación no válida")


# Bucle que mostre 4 opcions (1. Demanar temperatura. pujar temp, baixar temp, eixir)

print("Menu\n 1. Demanar temp\n 2. Pujar\n 3. Baixar\n 4. Eixir")

opcion = input("Tria el menu")
temperatura = 0
while opcion != "4":
    
    if opcion == "1":
        temperatura = int(input("Dame temp"))
    elif opcion == "2":
        temperatura += 1
        print(f"{temperatura}")
    elif opcion == "3":
        temperatura -= 1
        print(f"{temperatura}")
    else: 
        print("Operació no válida")
    print("Menu\n 1. Demanar temp\n 2. Pujar\n 3. Baixar\n 4. Eixir")

    opcion = input("Tria el menu")
    
    