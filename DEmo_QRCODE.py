import pyqrcode
from pyqrcode import QRCode
Email= "parth.shukla1989@gmail.com\n"
MobileNo = "\n9599587014\n"
LinkedID="https://www.linkedin.com/parthshukla"

obj = pyqrcode.create(Email+MobileNo+LinkedID)
obj.svg('MYQR.svg',scale=5)