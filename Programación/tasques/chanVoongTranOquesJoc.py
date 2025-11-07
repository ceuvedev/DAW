import random

def dados():
    dados = random.randrange(1, 6)
    print(f"Soy un dado de valor: {dados}")
print("Welcome to joc de la Oca")
casillasTotales = int(input("Cuántas casillas quieres que tenga el juego? ")) 
casillasTotales += 1 
print(casillasTotales)
posicionActual = 0

#hay que hacer un bucle para que haga el algoritmo de las sumas en el rango de las casillas del juego
for i in range (0, casillasTotales):
    dados()