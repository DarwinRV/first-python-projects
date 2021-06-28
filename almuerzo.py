import random


def abrir():

	cena_aleatoria = random.choice(["Sopa de pollo","Sopa de cebada","Sopa de platano","Pechuga con ensalada","Sopa de costilla","Arepas con huevo","Costillas bbq","Sopa de pastas"])


	comida_aleatoria = random.choice(["chuleta con papas","chuleta con papas","ensalada fria","Ensalada con pechuga","Gulash","albondigas","Ensalada con atun","Carne desmechada","Lasagna","Lantejas","Frijoles con carne","Pasta a la boloñesa","Verduras al wok","chuleta con ensalada y papa chorreada"])


	viernes_aleatorio = random.choice(["stroganof de pollo","stroganof de lomo","Bandeja paisa","Pollo a la broster","Porquerias","Arepas con huevo","Croissant de chocolate","Cerdo falso","Domplins","Perros calientes","Hamburguesas"])

	print("Hola bienvenido")


	respuesta = str(input("""
		Ingresa lo que quieres comer hoy: 
			[1] Almuerzo
			[2] Comida
			[3] Almuerzo y comida
			[4] viernes sorpresa

		seleciona :)    >> """))
		

	if respuesta == "1":
		print (comida_aleatoria)
		print("Espero que te guste :)")

	elif respuesta == "2":
		print(cena_aleatoria)
		print("Que duermas bien" )
	
	elif respuesta == "3":
		print(comida_aleatoria)
		print(cena_aleatoria)
		print("Si no te gusto prueba otra vez")
	
	elif respuesta == "4":
		print(viernes_aleatorio)
		print("Espero que lo disfrute")


	else :
		print ("Selecciona una opcion ")


if __name__ == "__main__":
    abrir()



