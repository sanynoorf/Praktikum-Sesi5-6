import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)
    height, width = image.shape[:2]
    
    max_dim_x = int(abs(width * cos_deg) + abs(height * sin_deg))
    max_dim_y = int(abs(width * sin_deg) + abs(height * cos_deg))
    outputImage = np.zeros((max_dim_y, max_dim_x, 3), dtype=image.dtype)

    for y in range(height):
        for x in range(width):
            newX = int(cos_deg * x - sin_deg * y)
            newY = int(sin_deg * x + cos_deg * y)
            
            if 0 <= newX < max_dim_x and 0 <= newY < max_dim_y:
                outputImage[newY, newX] = image[y, x]
    
    return outputImage

image = img.imread('zebra.jpg')
rotated_image = rotateImage(image, 45)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title("Rotated Image (45° at Pivot (0,0))")

plt.show()