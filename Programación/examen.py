# piedra papel o tijera
import random #se usara para los aleatorios
print("Juego de piedra papel o tijera!")

tirada = ['Piedra', 'Papel', 'Tijera'] 
tirada_aleatoria = random.choice(tirada)
print(tirada_aleatoria)

while True:
    num_jugadas=int(input(print("Cuantas jugadas quieres que sean? (Nota: numero positivo y número impar)")))
    
    if num_jugadas < 0 or num_jugadas%2==0:
        num_jugadas=int(input(print("Recuerdo: núm. positivo y núm impar! ")))
        continue
    else: 
        break
        
jugador1=input(print("Nombre del jugador1 "))
jugador2=input(print("Nombre del jugador2 "))
rondaGanadaJugador1= 0
rondaGanadaJugador2= 0

print("Que comience el juego!")
for i in range(0, num_jugadas):
    tiradaJugador1 = random.choice(tirada)
    tiradaJugador2 = random.choice(tirada)
    if tiradaJugador1 == tiradaJugador2:
        print(f"{jugador1} juega {tiradaJugador1} y {jugador2} juega {tiradaJugador2}")
        print("Empate!")
    if tiradaJugador1 == "Piedra" and tiradaJugador2 == "Tijera":
        print(f"{jugador1} juega {tiradaJugador1} y {jugador2} juega {tiradaJugador2}")
        print(f"{jugador1} gana la ronda {i+1}")   
        rondaGanadaJugador1 += 1
    if tiradaJugador1 == "Tijera" and tiradaJugador2 == "Papel":
        print(f"{jugador1} juega {tiradaJugador1} y {jugador2} juega {tiradaJugador2}")
        print(f"{jugador1} gana la ronda {i+1}")
        rondaGanadaJugador1 += 1 
    if tiradaJugador1 == "Papel" and tiradaJugador2 == "Piedra":
        print(f"{jugador1} juega {tiradaJugador1} y {jugador2} juega {tiradaJugador2}")
        print(f"{jugador2} gana la ronda {i+1}")
        rondaGanadaJugador1 += 1 
#2 jugador
    if tiradaJugador2 == "Piedra" and tiradaJugador1 == "Tijera":
        print(f"{jugador1} juega {tiradaJugador1} y {jugador2} juega {tiradaJugador2}")
        print(f"{jugador2} gana la ronda {i+1}")   
        rondaGanadaJugador2 += 1
    if tiradaJugador2 == "Tijera" and tiradaJugador1 == "Papel":
        print(f"{jugador1} juega {tiradaJugador1} y {jugador2} juega {tiradaJugador2}")
        print(f"{jugador1} gana la ronda {i+1}")
        rondaGanadaJugador2 += 1 
    if tiradaJugador2 == "Papel" and tiradaJugador1 == "Piedra":
        print(f"{jugador1} juega {tiradaJugador1} y {jugador2} juega {tiradaJugador2}")
        print(f"{jugador2} gana la ronda {i+1}")
        rondaGanadaJugador2 += 1 
        #esto no funciona pero lo dejo para despues
        

    
print(f"rondas ganadas por el {jugador1}: {rondaGanadaJugador1} y rondas ganadas por el jugador {jugador2}: {rondaGanadaJugador2}")
if rondaGanadaJugador1 > rondaGanadaJugador2:
    print(f"gana el {jugador1}")
else: print (f"gana {jugador2}")
    




