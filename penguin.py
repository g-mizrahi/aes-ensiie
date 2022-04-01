from PIL import Image
from Crypto.Cipher import AES
import numpy as np

def encrypt_ECB(msg, key = b'Sixteen byte key'):
    assert isinstance(key, bytes) and len(key)==16
    cipher = AES.new(key, AES.MODE_ECB)
    return(cipher.encrypt(msg))


im = Image.open("figures/fish.png")

pixels = list(im.getdata())

flat_pixels = bytes([val for elem in pixels for val in elem])
ECB_encrypted_flat_pixels = encrypt_ECB(flat_pixels)

ECB_encrypted_pixels = [tuple(ECB_encrypted_flat_pixels[i:i+4]) for i in range(0, len(ECB_encrypted_flat_pixels), 4)]

ECB_img = Image.new('RGB', im.size)
ECB_img.putdata(ECB_encrypted_pixels)

ECB_img.show()
