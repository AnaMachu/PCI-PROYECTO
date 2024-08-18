# PCI-PROYECTO
Healthapp
Este proyecto consiste en no solo una recomendación de comida para una vida saludable, si no que brinda exactamente lo que debes de comer de cada cosa para logarar tu objetivo fitness sea tanto bajar de peso,crear masa muscular o simplemente mantenerte en balance.
Esto será posible mediante la medición aritmética de las calorías de mantenimiento tomando en cuenta las variables de peso,estatura, edad y sexo para que sea más preciso, una vez realizadpo calculará el deficit o superavit calórico dependiendo de la meta fitness, posteriormente brindará un plan alimenticio variado tomando en cuenta todas estas caracteríticas aparte de que ofrece alimentos accesibles a la canasta básica lo que lo hace apropiado para todos los usuarios.
Este proyecto facilita y optimiza la función de un nutriologo que muchas veces las personas no están dispuestas a pagar y aún así podran obtener un cambio fisico garantizado mediante loa medición de datos exactos y uso de fórmulas.

ALGORITMO
entradas: peso,sexo, edad y estatura
salidas: calorías a consumir y alimentos

1Pedir sexo (mujer,hombre)
2Pedir peso edad y estatura
3 SI sexo= mujer
 3.1 Calorías mantenimiento=(10*peso)+(6.25*estatura)-(5*edad)-161
4 Si no (sexo=hombre)
 4.1 Calorías mantenimiento= (10*peso)+(6.25*estatura)-(5*edad)+5
5 Preguntar objetivo Fitness (Subir peso, bajar peso, mantenimiento)
6 Si objetivo fitness="subir peso"
 6.1
