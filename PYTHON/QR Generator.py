#Aqui se importa Tkened
import pyqrcode
from PIL import Image
link = input ('Ingresa tu URL para tu QR: ')
qr_code= pyqrcode.create(link)
qr_code.png('QRCode.png', scale=5)
Image.open('QRCode.png')