productos = [
    ['coca', 1, 20.00]
     ['hot dog', 1, 40.00]
]

ticket_str= ''

encabezado = 'TICKET DE COMPRA'
for elemento in productos:
    ticket_str += f'{elemento[0]:<20}{elemento[1]:^}

#Crear el encabezado del ticket 
print(f'{encabezado:42\\b})
'''TICKET DE COMPRA

PRODUCTO        CANTIDAD        TOTAL
