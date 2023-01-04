"""QR is short for Quick Response, and they are named so because they can be read quickly by a cell phone.
They are used to take information from transitory media and put it on your cell phone. 


What is a QR code?

QR codes are used to encode and decode the data into a machine-readable form.
The use of camera phones to read two-dimensional barcodes for various purposes is currently a popular topic in both types of research and practical applications.
It contains a grid of black squares on a white background, which can be read by any imaging device such as a camera,
and processed to extract the required data from the patterns that are present in the horizontal components of the image.

To generate QR Codes with Python you need to install only one Python library : pip install pyqrcode
"""

import pyqrcode
from pyqrcode import QRCode

# String which represent the QRCode
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"

# Generate QR Code
url = pyqrcode.create(s)

#Create and save the png file naming "myqr.png"
url.svg("myqr.svg", scale = 8)
