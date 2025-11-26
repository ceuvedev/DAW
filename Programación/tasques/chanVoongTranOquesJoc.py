import random

def dados():
    dados = random.randrange(1, 6)
    print(f"Soy un dado de valor: {dados}")
    return int(dados)
print("Welcome to joc de la Oca")
casillasTotales = int(input("Cuántas casillas quieres que tenga el juego? ")) 
print(casillasTotales)
posicionActual = 0

#hay que hacer un bucle para que el juego no acabe hasta que se cumpla la condicion de que se llegue a las casillas totales. de momento la logica ha aplicar, es que se termine el bucle pasado las casillasTotales

while posicionActual < casillasTotales:
    posicionActual = posicionActual + dados()
    print(f"Estoy en la posición {posicionActual}")
        if posicionActual