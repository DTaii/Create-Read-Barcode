from pyzbar.pyzbar import decode
from PIL import Image

# Open barcode image
image = Image.open('barcode.png') #path to your image

#Solve and print 
decoded_objects = decode(image)
for obj in decoded_objects:
    print(f'Type: {obj.type}, Data: {obj.data.decode("utf-8")}')