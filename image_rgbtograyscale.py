import numpy as np
import cv2
from threading import Thread
import time

class rgb2grayscale(Thread):

    def __init__(self, img, date, host_id):
        Thread.__init__(self)
        self.img = img
        self.date = date
        self.host_id = host_id

    def run(self):
        height,width,channel = self.img.shape
        img_grayscale = np.zeros((height,width,1))
        for i in np.arange(height):
            for j in np.arange(width):
                r = self.img.item(i,j,0)
                g = self.img.item(i,j,1)
                b = self.img.item(i,j,2)

                # RGB to Grayscale
                y = 0.299*r + 0.587*g + 0.144*b

                img_grayscale.itemset((i,j,0),int(y))

        cv2.imwrite(self.date+self.host_id+'.png', img_grayscale)

def rgb2grayscale_main(date, host_id):
    img = cv2.imread(date+host_id+'.png')
    img_tograyscale = rgb2grayscale(img, date, host_id)
    start = time.time()
    img_tograyscale.start()
    img_tograyscale.join()
    end = time.time()
    
    print((end-start))