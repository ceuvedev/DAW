#Ponemos un mensaje de introduccion pidiendo los dos equipos
print("Bienvenidos al marcador de basquet IES Jaume el Just \nAntes de comenzar, necesito que me digas los nombres de los dos equipos")
equipoA = input(print("Nombre del equipo A: "))
equipoB = input(print("Nombre del equipo B: "))
#Aqui pongo los variables de scope global para poder acceder desde fuera
puntuacionFinalA = 0
puntuacionFinalB = 0
contador1 = 0
contador2 = 0
contador3 = 0

for i in range(1, 5):
    print(f"Comença el quart {i}")
    #Aqui pongo variables de scope local dentro del loop porque me interesa que vuelvan a cero a cada iteración
    puntuacionParcialA = 0
    puntuacionParcialB = 0
    while True:
        #Pido el valor de la canasta
        canasta = int(input("Puedes indicarme el valor de la canasta? "))
        diferencia = abs(puntuacionParcialA - puntuacionParcialB)
        #Si sale cero, directamente hacemos el break e incrementamos i.
        if canasta == 0:
            print(f"Se acabó el cuarto {i}")
            print("--------------")
            print("Canastas en este cuarto")
            print(f"{equipoA}: {puntuacionParcialA} puntos")
            print(f"{equipoB}: {puntuacionParcialB} puntos")
            print("--------------")
            break
        #En caso de no ser cero, pasamos a la siguiente workflow
        equipo = input("Puedes indicarme el equipo? (A/B) ").upper()    
        if canasta >= 1 and canasta <= 3 and equipo == "A":
            puntuacionParcialA += canasta
            puntuacionFinalA += canasta
            print("--------------")
            print(f"{canasta} puntos para {equipoA}")
            print(f"{equipoA}: {puntuacionFinalA} puntos")
            print(f"{equipoB}: {puntuacionFinalB} puntos")
            print (f"Diferencia actual {diferencia} \nDiferencia máxima ")
            print("--------------")
        elif canasta >= 1 and canasta <= 3 and equipo == "B":
            puntuacionParcialB += canasta
            puntuacionFinalB += canasta
            print("--------------")
            print(f"{canasta} puntos para {equipoB}")
            print(f"{equipoA}: {puntuacionFinalA} puntos")
            print(f"{equipoB}: {puntuacionFinalB} puntos")
            print (f"Diferencia actual {diferencia} \nDiferencia máxima ")
            print("--------------")
        else: canasta < 0 and canasta > 3 and equipo != "A" or equipo != "B"
        print("Datos invalidos, ingrese de nuevo")
        #Esta parte de código es para el contador de tiros y su valor.
        if canasta == 1:
            contador1 = contador1 + 1
        if canasta == 2:
            contador2 = contador2 + 1
        if canasta == 3:
            contador3 = contador3 + 1

#Cuando acaba el bucle de los cuartos, continua con esta parte del codigo, que es el final del partido.
print("Fin del partido")
if puntuacionFinalA > puntuacionFinalB:
    print(f"Ha ganado equipo {equipoA}")
else: 
    print(f"Ha ganado equipo {equipoB}")
print("")

print(f"Tiros libres {contador1}")
print(f"Tiros dobles {contador2}")
print(f"Tiros triples {contador3}")