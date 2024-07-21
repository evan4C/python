import pyqrcode
from PIL import Image
link = input("enter a link to generate QR: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCode.png")
