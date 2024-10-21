# Definiciones de listas y sus calorías
list1 = ["arroz", "pollo", "frijol", "leche", "queso", "huevo", "avena"]
list1cals = [165, 120, 60, 0, 70, 150]
list2 = ["arroz", "pollo", "frijol", "leche", "queso", "huevo", "avena", "pasta", "lentejas"]
list2cals = [165, 120, 60, 100, 70, 150, 200, 120]
list3 = ["arroz", "pollo", "frijol", "leche", "queso", "huevo", "avena", "pasta", "lentejas", "tortilla", "jamón", "pan bimbo"]
list3cals = [65, 120, 60, 100, 70, 150, 200, 120, 50, 150, 70]

sexo_femenino = "Mujer"
sexo = input("¿Cuál es tu sexo? (Hombre/Mujer): ")
peso = float(input("¿Cuántos pesas? (en kilos): "))
edad = int(input("¿Cuál es tu edad?: "))
estatura = float(input("¿Cuál es tu estatura? (en metros): "))

# Función para calcular calorías de mantenimiento
def calorias_de_mantenimiento(peso, estatura, edad, sexo):
    if sexo == sexo_femenino:
        return (10 * peso) + (6.25 * estatura * 100) - (5 * edad) - 161
    else:
        return (10 * peso) + (6.25 * estatura * 100) - (5 * edad) + 5

cals = calorias_de_mantenimiento(peso, estatura, edad, sexo)
print(f"Calorías de mantenimiento: {cals:.2f} calorías")

# Determinar el objetivo de calorías
objetivo_fitness = input("¿Cuál es tu objetivo fitness? (Subir de peso/Bajar de peso/Mantenimiento): ")

if objetivo_fitness == "Subir de peso":
    objetivo_calorias = cals * 1.20
    print(f"Debes hacer un superávit de: {objetivo_calorias:.2f} calorías")
elif objetivo_fitness == "Bajar de peso":
    objetivo_calorias = cals * 0.80
    print(f"Debes hacer un déficit de: {objetivo_calorias:.2f} calorías")
else:
    objetivo_calorias = cals
    print("Debes consumir tus calorías de mantenimiento.")

presupuesto = input("¿Cuál es tu presupuesto semanal? (1000, 2000, 3000+): ")

if presupuesto == "1000":
    comida_recomendada = list1
    lista_calorias = list1cals
elif presupuesto == "2000":
    comida_recomendada = list2
    lista_calorias = list2cals
else:
    comida_recomendada = list3
    lista_calorias = list3cals

print(f"Opciones saludables de comida para ti: {comida_recomendada}")

# Cálculo del gramaje necesario
def calcular_gramaje(objetivo_calorias, lista_calorias):
    gramaje_total = []
    for calorias in lista_calorias:
        # Calcula el gramaje proporcional a la cantidad total de calorías
        gramaje = (objetivo_calorias / sum(lista_calorias)) * 1000  # Proporción de 1000g
        gramaje_total.append(gramaje)
    return gramaje_total

gr = input("¿Quieres continuar para brindarte gramaje de comida? (s/n): ")

while gr.lower() == "s":
    gramajes_necesarios = calcular_gramaje(objetivo_calorias, lista_calorias)
    for alimento, gramaje in zip(comida_recomendada, gramajes_necesarios):
        print(f"Necesitas consumir aproximadamente {gramaje:.2f} gramos de {alimento}.")
gr = input("¿Quieres continuar para brindarte gramaje de comida? (s/n): ")

print("Listos para una vida saludable")