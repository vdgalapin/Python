# Module for QR Code Generator
# pip install pyqrcode

# Module for PNG Image format
# pip install pypng

# Module for Pandase
# pip install pandas


# Importing QR pyqrcode
import pyqrcode
import png

# Reading Excel Files
import pandas as pd
f = open("boxandloc.txt", "r")


boxandloc =  pd.read_excel('boxandloc.xlsx')

for y in boxandloc.items():
    for x in y[1]:
        if (y[0] == 'Box'):
            url = pyqrcode.create(x)
            fileLocation = 'box_qrcodes/' + x +'.svg'
            url.svg(fileLocation, scale = 8)
        elif(y[0] == 'Location'):
            location = 'A01-' + x
            fileLocation = 'loc_qrcodes/' + location +'.svg'
            url = pyqrcode.create(location)
            url.svg(fileLocation, scale = 8)
