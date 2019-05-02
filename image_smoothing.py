import cv2

def image_smoothing(date, host_id):
    img_with_noise = cv2.imread(date+host_id+'.png')
    median_smoothing = cv2.medianBlur(img_with_noise, 5)
    cv2.imwrite(date+host_id+'.png', median_smoothing) 
