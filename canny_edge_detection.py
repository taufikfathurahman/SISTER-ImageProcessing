import cv2

def canny_ed(date, host_id):
    my_img = cv2.imread(date+host_id+'.png')
    canny_edges = cv2.Canny(my_img,100,200)
    cv2.imwrite(date+host_id+'.png', canny_edges)