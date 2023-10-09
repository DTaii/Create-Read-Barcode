import barcode
from barcode import generate
from barcode.writer import ImageWriter

# Create an code128 barcode
ean = barcode.get_barcode_class('code128')

# Data you want to encode as a barcode
data = 'shirt - 50$'

# Create the barcode and save it as an image
ean_barcode = ean(data, writer=ImageWriter())
ean_barcode.save('barcode')
