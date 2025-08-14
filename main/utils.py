import random
import string
import qrcode
import os
from django.conf import settings

def generate_short_code(length=6):
    """Generate a random alphanumeric short code."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_qr_code(url):
    """Generate a QR code image for the given URL."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Ensure QR code directory exists
    qr_code_dir = os.path.join(settings.MEDIA_ROOT, 'qr_codes')
    os.makedirs(qr_code_dir, exist_ok=True)

    file_name = f"{generate_short_code(8)}.png"
    file_path = os.path.join(qr_code_dir, file_name)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    return f"qr_codes/{file_name}"
