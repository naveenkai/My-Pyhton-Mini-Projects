import pyqrcode
import png
link = "https://github.com/thenameiswin/170-Pyhton-Projects/new/main"
qr_code = pyqrcode.create(link)
qr_code.png("github.png", scale=5)
