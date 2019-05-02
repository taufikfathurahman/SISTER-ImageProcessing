import numpy as np 
import cv2
import time

start = time.time() 
# Read color image
img = cv2.imread('gambar.jpg')

# Get the image's height, width, and channels
height, width, channel = img.shape

# Create blank grayscale image
img_grayscale = np.zeros((height,width,1))

# CALCULATE
for i in np.arange(height):
    for j in np.arange(width):
        r = img.item(i,j,0)
        g = img.item(i,j,1)
        b = img.item(i,j,2)

        # RGB to Grayscale
        y = 0.299*r + 0.587*g + 0.144*b

        img_grayscale.itemset((i,j,0),int(y))

# Write image
cv2.imwrite('image_grayscale.jpg',img_grayscale)
# View image
end = time.time()
print((end-start))