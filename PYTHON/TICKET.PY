Productos= [
    ['Coca', 1, 20.00],
    ['HOT DOG', 1, 40.00]
]

ticket_str = ''
total = 0

Encabezado = 'TICKET DE COMPRA'
for elemento in Productos:
    ticket_str += f'{elemento[0]:<20}{elemento[1]}
