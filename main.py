# import QrCode module
import qrcode
# import constant in the QrCode module
from qrcode.constants import ERROR_CORRECT_H

# management of QrCode options
qr = qrcode.QRCode(
  version=2,
  error_correction=ERROR_CORRECT_H,
  box_size=10,
  border=3,
)

# add the data that will be read when reading the QrCode, here a url
qr.add_data('https://www.etiennejuz.com')
qr.make(fit=True)

# generate the QrCode in black and white
image = qr.make_image(fill_colr="black", back_color="white")

# save the Qrcode as "Etiennejuz_QrCode.png"
image.save('Etiennejuz_QrCode.png')