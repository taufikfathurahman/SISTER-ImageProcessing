import numpy as np
import cv2
from threading import Thread
import time

class rgb2ycrcb(Thread):

    def __init__(self, img, date, host_id):
        Thread.__init__(self)
        self.img = img
        self.date = date
        self.host_id = host_id

    def run(self):
        height,width,channel = self.img.shape
        img_ycrcb = np.zeros((height,width,3))
        for i in np.arange(height):
            for j in np.arange(width):
                r = self.img.item(i,j,0)
                g = self.img.item(i,j,1)
                b = self.img.item(i,j,2)

                # RGB to YCbCr and representing it in 255 
                Y = 16 + ((65.481*r)/256. + (128.553*g)/256. + (24.966*b)/256.)
                Cb = 128 + ((-37.797*r)/256. - (74.203*g)/256. + (112.0*b)/256.)
                Cr = 128 + ((112.0*r)/256. - (93.786*g)/256. - (18.214*b)/256.)
                
                img_ycrcb.itemset((i,j,0),int(Y))
                img_ycrcb.itemset((i,j,1),int(Cr))
                img_ycrcb.itemset((i,j,2),int(Cb))

        cv2.imwrite(self.date+self.host_id+'.png', img_ycrcb)

def rgb2ycrcb_main(date, host_id):
    img = cv2.imread(date+host_id+'.png')
    img_toycrbc = rgb2ycrcb(img, date, host_id)
    start = time.time()
    img_toycrbc.start()
    img_toycrbc.join()
    end = time.time()
    
    print((end-start))