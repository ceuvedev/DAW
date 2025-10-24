#Ponemos un mensaje de introduccion pidiendo los dos equipos
print("Bienvenidos al marcador de basquet IES Jaume el Just \nAntes de comenzar, necesito que me digas los nombres de los dos equipos")
equipoA = input(print("Nombre del equipo A: "))
equipoB = input(print("Nombre del equipo B: "))
#Aqui pongo los variables de scope global para poder acceder desde fuera
puntuacionFinalA = 0
puntuacionFinalB = 0


#Bucle para generar los cuartos no funciona como se espera
for i in range(1, 5):
    print(f"Comença el quart {i}")
    #Aqui pongo variables de scope local dentro del loop porque me interesa que vuelvan a cero a cada iteración
    puntuacionParcialA = 0
    puntuacionParcialB = 0
    # Aquí me he encotnrado un problema, una vez declarado las dos variables, no se como hacer para que pase a break en la primera declaración de la variable.
    # Todavía no se como refactorizar en python, pero la logica de elif ha sido un poco a matar moscas a cañonazos.
    while True:
        canasta = int(input("Puedes indicarme el valor de la canasta? "))
        equipo = input("Puedes indicarme el equipo? (A/B) ").upper()
        if canasta == 0:
            print(f"Se acabó el cuarto {i}")
            print("--------------")
            print("Canastas en este cuarto")
            print(f"{equipoA}: {puntuacionParcialA} puntos")
            print(f"{equipoB}: {puntuacionParcialB} puntos")
            print("--------------")
            break
        elif canasta > 1 and canasta <= 3 and equipo == "A":
            puntuacionParcialA += canasta
            puntuacionFinalA += canasta
            print("--------------")
            print(f"{canasta} puntos para {equipoA}")
            print(f"{equipoA}: {puntuacionFinalA} puntos")
            print(f"{equipoB}: {puntuacionFinalB} puntos")
            print("--------------")
        elif canasta > 1 and canasta <= 3 and equipo == "B":
            puntuacionParcialB += canasta
            puntuacionFinalB += canasta
            print("--------------")
            print(f"{canasta} puntos para {equipoB}")
            print(f"{equipoA}: {puntuacionFinalA} puntos")
            print(f"{equipoB}: {puntuacionFinalB} puntos")
            print("--------------")
        elif canasta < 0 and canasta > 3 and equipo != "A" or equipo != "B":
            print("Datos invalidos, ingrese de nuevo")




print("Fin del partido")
print("Puntuacion total blablablab")