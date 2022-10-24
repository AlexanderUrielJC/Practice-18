precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
for price in precios:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min))
print("El máximo es " + str(max))