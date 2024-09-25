sexofemenino="Mujer"
paquete1=("arroz","pollo","frijol","leche","queso","huevo","avena") #700g
paquete1cals= 165+120+60+100+70+150
paquete2=("arroz","pollo","frijol","leche","queso","huevo","avena","pasta","lentejas")#900
paquete2cals=165+120+60+100+70+150+200+120
paquete3=("arroz","pollo","frijol","leche","queso","huevo","avena","pasta","lentejas","tortilla","jamón",
          "pan bimbo")#1200
paquete3cals=165+120+60+100+70+150+200+120+50+150+70
sexo=str(input("¿Cuál es tu sexo? (Hombre/Mujer): "))
peso=float(input("¿Cuántos pesas? (en kilos)"))
edad=int(input("¿Cuál es tu edad?"))
estatura=float(input("¿Cuál es tu estatura?(en metros)"))

def calorias_de_mantenimientof(peso,estatura,edad):
   cantidad_de_calorías=(((10*peso)+(6.25*estatura)-(5*edad)-161)*10)
   return cantidad_de_calorías
if sexo==sexofemenino:
    cals=calorias_de_mantenimientof(peso,estatura,edad)
    print(f"Calorías de mantenimiento {cals} calorias")
else:
 def calorias_de_mantenimientom(peso,estatura,edad):
  cantidad_de_calorías= (((10*peso)+(6.25*estatura)-(5*edad)+5)*10)
  return cantidad_de_calorías
 cals=calorias_de_mantenimientom(peso,estatura,edad)
 print(f"Calorías de mantenimiento {cals} calorías")
 
def calcular_superavit(cals):
  superavit=((cals*0.20)+cals)
  return superavit
def calcular_deficit(cals):
  déficit=((cals)-(cals*.20))
  return déficit

objetivo_fitness=str(input("¿Cuál es tu objetivo fitnes? (Subir de peso,Bajar de peso,Mantenimiento)"))
if objetivo_fitness=="Subir de peso":
   Superavit=calcular_superavit(cals)
   print(f"Debes hacer un superavit de: {Superavit} calorias")
elif objetivo_fitness=="Bajar de peso":
    Déficit=calcular_deficit(cals)
    print(f"Debes hacer un déficit de: {Déficit} calorías")
else:
    Mantenimiento=cals
    print("Debes consumir tus calorías de mantenimiento")

presupuesto=str(input("¿Cuál es tu presupuesto semanal? (1000,2000,3000+)"))
if presupuesto=="1000":
 comida_recomendada=paquete1
 print(f"Opciones saludables de comida para ti:{paquete1}")
elif presupuesto=="2000":
 comida_recomendada=paquete2
 print(f"Opciones saludables de comida para ti:{paquete2}")
else:
 comida_recomendada=paquete3
print(f"Opciones saludables de comida para ti:{paquete3}")

def gramaje_alimento(cantidad_de_calorías,comida_recomendada):
  while paquete1: True
  gramaje1=700
  gramaje=0
  while gramaje<=Déficit or Superavit or cals:
   creciente=Déficit or Superavit or cals/gramaje1
   gramaje+=gramaje1+creciente
   print(f"necesitas comer {gramaje}")

while paquete2: True
gramaje2=800
gramaje=0
while gramaje<=Déficit or Superavit or cals:
   creciente=Déficit or Superavit or cals/gramaje2
   gramaje+=gramaje2+creciente
   print(f"necesitas comer {gramaje}")

while paquete3: True
gramaje3=1100
gramaje=0
while gramaje<=Déficit or Superavit or cals:
   creciente=Déficit or Superavit or cals/gramaje3
   gramaje+=gramaje3+creciente
   print(f"necesitas comer {gramaje}")

print("Listos para una vida saludable")