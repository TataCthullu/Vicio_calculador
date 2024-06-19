actions = {

    "estudiar" : 3,
    "ejercicio" : 3,
    "trabajar" : 3

}

pers_cont = 0
inp_act = input("Ingresa la actividad que realizaste: ")

if inp_act in actions:
    pers_cont += actions[inp_act]
    print(pers_cont)
else: 
    print("La actividad no se encuentra en el diccionario")    


