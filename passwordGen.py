import random 

def generar_password ():
    MAYUS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    MINUS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    NUM = ["1","2","3","4","5","6","7","8","9","0"]
    SIMBO = ["!","@","#","$","%","^^","&","*","(","_","+"]

    caracteres = MAYUS + MINUS + NUM + SIMBO


    password = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password)
    return password


def run ():
    password = generar_password()
    print ("Tu nueva contrasena es :" + password)


if __name__ == "__main__":
    run()