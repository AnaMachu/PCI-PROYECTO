sexofemenino="Mujer"
paquete1=("arroz,pollo,frijol,leche,queso,huevo,avena,pasta,lentejas,tortilla,jamón,pan bimbo")
paquete2=("arroz,pollo,frijol,leche,queso,yogur,avena,pasta,lentejas,tortilla,jamón,pan bimbo cero, pescado,barra de proteina, rice cakes, huevo,nueces, frutas, hotcakes de avena")
paquete3=("arroz,pollo,frijol,leche de proteína,queso,yogur griego light,avena,pasta,lentejas,tortilla,jamón,pan oroweat, pescado,barra de proteina, rice cakes, huevo,nueces, frutas, hotcakes de avena, salmón,tocino,carne de res, gelatina light, nopales, canre de cerdo, crema de maní, germen de trigo")
sexo=str(input("¿Cuál es tu sexo? (Hombre/Mujer): "))
peso=float(input("¿Cuántos pesas? (en kilos)"))
edad=int(input("¿Cuál es tu edad?"))
estatura=float(input("¿Cuál es tu estatura?(en metros)"))

if sexo==sexofemenino:
    Calorías_de_mantenimiento=(((10*peso)+(6.25*estatura)-(5*edad)-161)*10)
    print(f"Calorías de mantenimiento {Calorías_de_mantenimiento} calorias")
else:
    Calorías_de_mantenimiento= (((10*peso)+(6.25*estatura)-(5*edad)+5)*10)
    print(f"Calorías de mantenimiento= {Calorías_de_mantenimiento} calorias")

objetivo_fitness=str(input("¿Cuál es tu objetivo fitnes? (Subir de peso,Bajar de peso,Mantenimiento)"))
if objetivo_fitness=="Subir de peso":
    superavit=((Calorías_de_mantenimiento*0.20) + (Calorías_de_mantenimiento))
    print(f"Debes hacer un superavit de: {superavit} calorias")
elif objetivo_fitness=="Bajar de peso":
    Déficit=((Calorías_de_mantenimiento)-(Calorías_de_mantenimiento*.20))
    print(f"Debes hacer un déficit de: {Déficit} calorías")
else:
    Mantenimiento=Calorías_de_mantenimiento
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

print("Lsistos para una vida saludable")

 

















 

 

