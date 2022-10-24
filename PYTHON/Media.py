def puntuacion (clase):
    return sum(clase) / len(clase)

clase= [80, 50, 70, 80]
media = puntuacion(clase)
print ('Esta es la media: ', media)

clase = [60, 70, 60, 50, 58]
media = puntuacion(clase)
print ('Segunda media de la clase 2:', media)