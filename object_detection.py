import cv2

def object_detection(date, host_id):
    face_cascade = cv2.CascadeClassifier('object_detection_xml/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('object_detection_xml/haarcascade_eye.xml')
    my_img = cv2.imread(date+host_id+'.png')
    gray = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        my_img = cv2.rectangle(my_img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = my_img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
    cv2.imwrite(date+host_id+'.png', my_img)