import cv2
import numpy as np

# Load the encrypted image
encrypted_img = cv2.imread('encrypted_image.bmp')

# Load the secret key
secret_key = np.load('secret_key.npy')

# Decrypt the image using XOR operation
decrypted_img = cv2.bitwise_xor(encrypted_img, secret_key)

# Save the decrypted image as a .jpg file
cv2.imwrite('decrypted_image.jpg', decrypted_img)
