# QRcode Generator

This script allows you to create QRcodes for various purposes, such as links, text, contact details, and more.

## Installation

1. Install the required dependencies using pip:

    ```bash
    pip install qrcode[pil]
    ```

## Usage

1. Open the `QRcode.py` script in a code editor.

2. Modify the `data` variable with the text or link you want to encode into the QR code.

3. Run the script:

    ```bash
    python QRcode.py
    ```

4. The script will generate a QR code image named `qrcode.png` in the same directory.

## Examples

You can create QR codes for various types of data, including:
- Links to websites or socials
- Contact details
- WiFi network information
- Phone numbers
- Email addresses
- Etc.

## Error_correct
Error correction is used to recover data if the QRcode is partially damaged, obscured, or distorted during scanning. Error correction levels offer different degrees of error recovery capability. 
- ERROR_CORRECT_L
    - Level "L" offers a low level of correction, up to 7%.
- ERROR_CORRECT_M
    - Level "M" offers a medium level of correction, up to 15%.
- ERROR_CORRECT_Q
    - Level "Q" offers a low level of correction, up to 25%.
- ERROR_CORRECT_H
    - Level "H" offers a high level of correction, up to 30%.

The choice of level depends on factors such as the likelihood of damage it may suffer, but the higher the level, the greater the size of the QRcode.

## Contributing

If you have suggestions or improvements to add, feel free to create a pull request.
You can send me suggestions to improve my work or make requests on my social profiles:
- [X or Twitter](https://x.com/XxCiuffoxX)
- [Instagram](https://instagram.com/xxciuffoxx)
