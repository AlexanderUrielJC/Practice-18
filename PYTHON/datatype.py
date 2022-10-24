from cProfile import label
from tokenize import PlainToken
from turtle import color
import matplotlib as pit

x1 = (3, 4, 5, 6)
y1 = (5, 6, 3, 4)
x2 = (2, 5, 8)
y2 = (3, 4, 3)

pit.plot (x1, y1, label = 'line 1', linewidth = 4, color = 'yellow')
pit.plot (x2, y2, label = 'line 2', linewidth = 4, color = 'blue')

pit.title('Diagrama de lineas')
pit.ylabel('Eje Y')
pit.xlabel('Eje X')

pit.legend()
pit.grid()
pit.show()