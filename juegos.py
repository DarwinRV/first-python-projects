import random



def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    print("tienes 10 vidas")
    vidas = 10
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("busca un numero mas grande")
            vidas -= 1
            print(vidas)

        elif numero_elegido > numero_aleatorio:
           print("busca un numero mas pequeño")
           vidas -= 1
           print(vidas)
        numero_elegido = int(input("Elige otro numero: "))


        if vidas == 1:
            print("tienes "+str(vidas)+" vidas")
            print("GAME OVER")
            print("Era" + numero_aleatorio)
            break
           

        elif numero_elegido == numero_aleatorio:
            print("Ganaste")


if __name__ == "__main__":
    run()
