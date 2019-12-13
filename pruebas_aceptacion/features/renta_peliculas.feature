Característica: Renta Películas
    Como usuario del sistema Renta_Películas
    Quiero seleccionar películas disponobles
    Para rentarlas
    
    Escenario: Renta de una película
        Dado Que ingreso logueado a la vista películas
        Y selecciono una de las películas disponibles
        Cuando presiono el botón rentar
        Entonces puedo ver que el stock de la pelicula seleccionada disminuye 

   #Escenario: Presionar el boton rentar sin selecionar ninguna película
   #    Dado Que ingreso logueado a la vista películas
   #    Y no selecciono ningua de las películas disponibles 
   #    Cuando presiono el botón rentar
   #    Entonces puedo ver el mensaje "No se ha seleccionado ninguna película"
