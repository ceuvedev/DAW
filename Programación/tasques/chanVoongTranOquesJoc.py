import random

print("Welcome to joc de la Oca")
casillasTotales = int(input("Cuántas casillas quieres que tenga el juego? ")) 
print(casillasTotales)
posicionActual = 0
ultimaTirada = 0
#hay que hacer un bucle para que el juego no acabe hasta que se cumpla la condicion de que se llegue a las casillas totales. de momento la logica ha aplicar, es que se termine el bucle pasado las casillasTotales

while posicionActual < casillasTotales:
    tirada = random.randint(1, 6)    
    posicionActual = posicionActual + tirada    
    print(f"He sacado {tirada}, Estoy en la posición {posicionActual}")
    #damos por el juego finalizado cuando la posicion actual coincide con la ultima casilla
    if posicionActual == casillasTotales:
        print(f"Has ganado la OCA")
        break
    #con esta condicion, si cae en multiplo de 5, es una oca, sumo 5 casillas
    if posicionActual % 5 == 0:        
        posicionActual = posicionActual + 5
        print(f"Estoy en una oca voy a saltar 5 casillas estoy en {posicionActual}")
    if posicionActual > casillasTotales:
        rebote = (posicionActual - casillasTotales) * 2
        posicionActual = posicionActual - rebote
        print(f"Me he pasado {casillasTotales - posicionActual} casillas, vuelvo a la casilla {posicionActual}")
    if tirada == 6 & ultimaTirada == 6:
        posicionActual = 0
        print(f"Arrancada de Marquez, parada de Casillas. Dos 6, comienza de nuevo")
    ultimaTirada = tirada
    
