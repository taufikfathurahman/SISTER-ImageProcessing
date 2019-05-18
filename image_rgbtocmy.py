import numpy as np
import cv2
from threading import Thread
import time

class rgb2cmy(Thread):

    def __init__(self, img, date, host_id):
        Thread.__init__(self)
        self.img = img
        self.date = date
        self.host_id = host_id

    def run(self):
        height,width,channel = self.img.shape
        img_cmy = np.zeros((height,width,3))
        for i in np.arange(height):
            for j in np.arange(width):
                r = self.img.item(i,j,0)
                g = self.img.item(i,j,1)
                b = self.img.item(i,j,2)

                # RGB to YCbCr and representing it in 255 
                c = 1 - (r/255.)
                m = 1 - (g/255.)
                y = 1 - (b/255.)
                
                img_cmy.itemset((i,j,0),int(c*100))
                img_cmy.itemset((i,j,1),int(m*100))
                img_cmy.itemset((i,j,2),int(y*100))


        cv2.imwrite(self.date+self.host_id+'.png', img_cmy)

def rgb2cmy_main(date, host_id):
    img = cv2.imread(date+host_id+'.png')
    img_tocmy = rgb2cmy(img, date, host_id)
    start = time.time()
    img_tocmy.start()
    img_tocmy.join()
    end = time.time()
    
    print((end-start))