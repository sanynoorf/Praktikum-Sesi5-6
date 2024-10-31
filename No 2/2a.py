import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = 'zebra.jpg'
image = img.imread(path)

height, width = image.shape[:2]

mirrored_image = np.zeros_like(image)

for y in range(height):
    for x in range(width):
        mirrored_image[y, x] = image[height - 1 - y, width - 1 - x]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(mirrored_image)
plt.title("Mirrored Image (Horizontal & Vertical)")

plt.show()
