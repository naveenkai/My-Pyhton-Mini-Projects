from PIL import Image
image = Image.open('win.png')

from numpy import asarray
data = asarray(image)
print(data)
