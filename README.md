# PCI-PROYECTO
proyecto de la escuela
Healthapp
Este proyecto consiste en no solo una recomendación de comida para una vida saludable, si no que brinda exactamente lo que debes de comer de cada cosa para logarar tu objetivo fitness sea tanto bajar de peso,crear masa muscular o simplemente mantenerte en balance.
Esto será posible mediante la medición aritmética de las calorías de mantenimiento tomando en cuenta las variables de peso,estatura, edad y sexo para que sea más preciso, una vez realizadpo calculará el deficit o superavit calórico dependiendo de la meta fitness, posteriormente brindará un plan alimenticio variado tomando en cuenta todas estas caracteríticas aparte de que ofrece alimentos accesibles a la canasta básica lo que lo hace apropiado para todos los usuarios.
Este proyecto facilita y optimiza la función de un nutriologo que muchas veces las personas no están dispuestas a pagar y aún así podran obtener un cambio fisico garantizado mediante loa medición de datos exactos y uso de fórmulas.

ALGORITMO
entradas: peso,sexo, edad, presupuesto semanal, objetivo fitness y estatura
constantes: “paquete1:Arroz,pollo,frijol,leche,queso,huevo,avena,pasta,lentejas,tortilla,jamón,pan bimbo” 

"paquete2:Arroz,pollo,frijol,leche,queso,yogur,avena,pasta,lentejas,tortilla,jamón,pan bimbo cero, pescado,barra de proteina, rice cakes, huevo,nueces, frutas, hotcakes de avena¨ 

“paquete3:arroz,pollo,frijol,leche de proteína,queso,yogur griego light,avena,pasta,lentejas,tortilla,jamón,pan oroweat, pescado,barra de proteina, rice cakes, huevo,nueces, frutas, hotcakes de avena, salmón,tocino,carne de res, gelatina light, nopales, canre de cerdo, crema de maní, germen de trigo"

salidas: calorías a consumir y alimentos

1Pedir sexo (mujer,hombre)

2Pedir peso edad y estatura

3 SI sexo= mujer

3.1 Calorías mantenimiento=(10_peso)+(6.25_estatura)-(5_edad)-161

4 Si no (sexo=hombre)

    4.1 Calorías mantenimiento= (10_peso)+(6.25_estatura)-(5_edad)+5

5 Preguntar objetivo Fitness (Subir peso, bajar peso, mantenimiento)

6 Si objetivo fitness=“subir peso”
   
    6.1Calorías mantenimientos*.20 + Calorias mantenimiento= Superavit

7Si objetivo fitness= “bajar de peso”

    7.1Calorías de mantenimiento-Calorías de mantenimiento*.20= Déficit

8Si objetivo ftness =“mantenimiento”
    
    8.1Calorías de mantenimiento= Mantenimiento

9Preguntar presupuesto (1000,2000,3000+)

10 Si presupuesto=1000

      10.1 paquete 1 y ajustarlo a “deficit”,“superavit” o “mantenimiento”

11Si presupuest0=2000

      11.1 paquete 2 y ajustarlo a “deficit”,“superavit” o “mantenimiento”

12 Si presupuesto= 3000+

       12.1 paquete3 y ajustarlo a “deficit”,“superavit” o “mantenimiento”

13 mostrar en pantalla “Listo, vamos por una dieta saludable”
