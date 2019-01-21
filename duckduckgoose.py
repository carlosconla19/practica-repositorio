
jugadores = ["carlos", "cesar", "maribel", "carol"]

def duck(juego):
    numero = input(int("Inroduce un numero entero: "))

    for i in jugadores:

        if jugadores[i] == numero:
            print(jugadores[i])
    return
