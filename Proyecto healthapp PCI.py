'''
Se reciben las variables peso,estatura y edad y devuelve calorías
de mantenimiento según el sexo del usuario
'''
def calorias_de_mantenimientof(peso, estatura, edad):#define calorías para mantenerse para mujer
    cantidad_de_calorias = (((10 * peso) + (6.25 * estatura) - (5 * edad) - 161) * 10)
    return cantidad_de_calorias

def calorias_de_mantenimientom(peso, estatura, edad):#define calorías para mantenerse para hombre
    cantidad_de_calorias = (((10 * peso) + (6.25 * estatura) - (5 * edad) + 5) * 10)
    return cantidad_de_calorias

'''
Recibe calorías de mantenimiento y se multiplican 
por un factor para calcular un superavit del 20%
'''
def calcular_superavit(cals):
    return cals * 1.2

'''
Recibe calorías de mantenimiento y se multiplican
por un factor para calcular un deficit del 20%
'''
def calcular_deficit(cals):
    return cals * 0.8


sexofemenino = "Mujer"
# Matriz con alimentos, gramajes y calorías por paquete
paquetes = [
    [["arroz", 100, 165], ["pollo", 100, 120], ["frijol", 100, 60], ["leche", 100, 100],\
     ["queso", 100, 70], ["huevo", 100, 150], ["avena", 100, 50]], 
    # Paquete 1 (700g)
    
    [["arroz", 100, 165], ["pollo", 100, 120], ["frijol", 100, 60], ["leche", 100, 100],\
     ["queso", 100, 70], ["huevo", 100, 150], ["avena", 100, 50], ["pasta", 100, 200],\
     ["lentejas", 100, 120]], 
    # Paquete 2 (900g)
    
    [["arroz", 100, 165], ["pollo", 100, 120], ["frijol", 100, 60], ["leche", 100, 100],\
    ["queso", 100, 70], ["huevo", 100, 150], ["avena", 100, 50], ["pasta", 100, 200],\
     ["lentejas", 100, 120], ["tortilla", 100, 50], ["jamón", 100, 150], ["pan bimbo", 100, 70]] 
    # Paquete 3 (1200g)
    ]

sexo = str(input("¿Cuál es tu sexo? (Hombre/Mujer): "))
peso = float(input("¿Cuántos pesas? (en kilos) "))
edad = int(input("¿Cuál es tu edad? "))
estatura = float(input("¿Cuál es tu estatura? (en metros) "))

if sexo == sexofemenino:
    cals = calorias_de_mantenimientof(peso, estatura, edad)
else:
    cals = calorias_de_mantenimientom(peso, estatura, edad)

print(f"Calorías de mantenimiento: {cals} calorías")

objetivo_fitness = str(input("¿Cuál es tu objetivo fitness? (Subir de peso, Bajar de peso, Mantenimiento) "))

if objetivo_fitness == "Subir de peso":
   superavit = calcular_superavit(cals)
   print(f"Debes hacer un superávit de: {superavit} calorías")
elif objetivo_fitness == "Bajar de peso":
    deficit = calcular_deficit(cals)
    print(f"Debes hacer un déficit de: {deficit} calorías")
else:
    mantenimiento = cals
    print(f"Debes consumir tus calorías de mantenimiento: {mantenimiento}")

presupuesto = str(input("¿Cuál es tu presupuesto semanal? (1000, 2000, 3000+) "))

# Seleccionando el paquete de alimentos según el presupuesto
if presupuesto == "1000":
    paquete_recomendado = paquetes[0]
elif presupuesto == "2000":
    paquete_recomendado = paquetes[1]
else:
    paquete_recomendado = paquetes[2]

# Mostrar la lista de alimentos recomendados
print(f"Opciones saludables de comida para ti:")
for alimento in paquete_recomendado:
    print(f"{alimento[0]} - {alimento[1]}g - {alimento[2]} calorías")

# Ciclo while para continuar o no con el gramaje
continuar = "s"
while continuar == "s":
    gr = str(input("¿Quieres continuar para brindarte gramaje de comida? (s/n): "))
    
    if gr == "s":
        if objetivo_fitness == "Subir de peso":
            objetivo_cals = superavit
        elif objetivo_fitness == "Bajar de peso":
            objetivo_cals = deficit
        else:
            objetivo_cals = cals
        
        calorias_paquete = sum(alimento[2] for alimento in paquete_recomendado)
        
        # Calcular el gramaje total necesario
        gramaje_necesario = (objetivo_cals/calorias_paquete) * sum(alimento[1] for alimento in paquete_recomendado)
        print(f"Necesitas comer aproximadamente {gramaje_necesario}g de este paquete de comida.")
    
    # Preguntar si quiere continuar calculando
    continuar = str(input("¿Quieres hacer otro cálculo? (s/n): "))

print("Listos para una vida saludable.")
