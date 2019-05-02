import numpy as np
import cv2
from threading import Thread
import time

class rgb2hsv(Thread):

    def __init__(self, img, date, host_id):
        Thread.__init__(self)
        self.img = img
        self.date = date
        self.host_id = host_id

    def run(self):
        height,width,channel = self.img.shape
        img_hsv = np.zeros((height,width,3))
        for i in np.arange(height):
            for j in np.arange(width):
                r = self.img.item(i,j,0)
                g = self.img.item(i,j,1)
                b = self.img.item(i,j,2)

                r_ = r/255.
                g_ = g/255.
                b_ = b/255.
                Cmax = max(r_,g_,b_)
                Cmin = min(r_,g_,b_)
                delta = Cmax-Cmin

                # Hue Calculation
                if delta == 0:
                    H = 0
                elif Cmax == r_ :
                    H = 60 * (((g_ - b_)/delta) % 6)
                elif Cmax == g_:
                    H = 60 * (((b_ - r_)/delta) + 2)
                elif Cmax == b_:
                    H = 60 * (((r_ - g_)/delta) + 4)

                # Saturation Calculation
                if Cmax == 0:
                    S = 0
                else :
                    S = delta / Cmax
                
                # Value Calculation
                V = Cmax 
                
                # Set H,S,and V to image
                img_hsv.itemset((i,j,0),int(H))
                img_hsv.itemset((i,j,1),int(S))
                img_hsv.itemset((i,j,2),int(V))

        cv2.imwrite(self.date+self.host_id+'.png', img_hsv)

def rgb2hsv_main(date, host_id):
    img = cv2.imread(date+host_id+'.png')
    img_tohsv = rgb2hsv(img, date, host_id)
    start = time.time()
    img_tohsv.start()
    img_tohsv.join()
    end = time.time()
    print((end-start))