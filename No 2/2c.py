import numpy as np
import imageio.v2 as img
import matplotlib.pyplot as plt

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    imgZoomOut = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y / factor)
            ori_x = int(x / factor)
            
            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)

            imgZoomOut[y, x] = image[ori_y, ori_x]
    
    return imgZoomOut

image = img.imread('zebra.jpg')
skala = 0.5 

imgZoomOut = zoomMinus(image, skala)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(imgZoomOut)
plt.title("Zoomed Out Image")

plt.show()