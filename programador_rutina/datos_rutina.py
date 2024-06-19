actions = {

    "estudiar" : 3,
    "ejercicio" : 3,
    "trabajar" : 3

}

pers_cont = 0

def Menu():
    print("1. Actividad realizada")
    print("2. Mostrar Contador")
    print("3. Salir")

def Act_rea():
    global pers_cont
    inp_act = input("Ingresa la actividad que realizaste: ")

    if inp_act in actions:
        pers_cont += actions[inp_act]
        print(f"Puntos acumulados: {pers_cont}")
    else: 
        print("La actividad no se encuentra en el diccionario")    

def Most_cont():
    print(f"Puntos obtenidos: {pers_cont}")

while True:
    Menu()
    opcion = input("Selecciona una opcion: ")    

    if opcion == "1":
        Act_rea()
    elif opcion == "2":
        Most_cont()
    elif opcion == "3":
        print("Cerrando el programa...")
        break        
    else:
        print("Opción no válida, elige una q lo sea.")