
import qrcode

# Data, link, etc or text
data = "https://x.com/XxCiuffoxX"

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (from 1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (4 types)
                                                        # ERROR_CORRECT_L = Low
                                                        # ERROR_CORRECT_M = Medium
                                                        # ERROR_CORRECT_Q = Quartile
                                                        # ERROR_CORRECT_H = High
    box_size=10,  # Size of the modules (squares)
    border=4,  # Border size
)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True) 

# Create a QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")


