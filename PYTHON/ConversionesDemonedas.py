print('.......................................ENTRANDO EN EL APARTADO US$/MXN...................................................')
ValorDelDolar=19.9590
#Este apartado es para la moneda de libras esterlinas a pesos y viceversa
Cantidad_de_pesos = float(input("Ingresa la cantidad de pesos a convertir: "))
Resultado = Cantidad_de_pesos/ValorDelDolar
print('la cantidad de pesos a dolares es:', Resultado)

Cant_dolares = float(input("Ingresa la cantidad de dólares: "))
ResultadoAPesos = Cant_dolares * ValorDelDolar
print('La converscion de dolares a pesos es la siguiente', ResultadoAPesos)
print('.......................................ENTRANDO EN EL APARTADO £/MXN...................................................')

ValorLibrasEsterlinas= 23.10
#Este apartado es para la moneda de libras esterlinas a pesos y viceversa
Cantidad_de_pesos = float(input("Ingresa la cantidad de pesos a convertir: "))
Resultado = Cantidad_de_pesos/ValorLibrasEsterlinas
print('la cantidad de pesos a dolares es:', Resultado)

CantLibras = float(input("Ingresa la cantidad de libras a pesos: "))
ResultadoAPesos = ValorLibrasEsterlinas*CantLibras
print('La converscion de dolares a pesos es la siguiente', ResultadoAPesos)
print('......................................................................................................................')
