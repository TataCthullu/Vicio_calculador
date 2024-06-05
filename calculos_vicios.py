cantidad_cigarros_al_dia = int(input("Escribe la cantidad de cigarros al dia: "))
print(f"Fumas {cantidad_cigarros_al_dia} cigarros al dia")

def cigarros_al_mes():
    cantidad_cigarros_mes = cantidad_cigarros_al_dia * 30
    return cantidad_cigarros_mes

print(f"Fumas {cigarros_al_mes()} cigarros al mes")
