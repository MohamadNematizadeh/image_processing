import cv2
import numpy as np

# Load the image
img = cv2.imread('input/Mona_Lisa.jpg')

# Generate a random secret key
secret_key = np.random.randint(0, 256, size=(img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)

# Encrypt the image using XOR operation
encrypted_img = cv2.bitwise_xor(img, secret_key)

# Save the encrypted image as a .bmp file
cv2.imwrite('encrypted_image.bmp', encrypted_img)

# Save the secret key as a .npy file
np.save('secret_key.npy', secret_key)