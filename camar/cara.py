import cv2 

vid = cv2.VideoCapture(1)
clasif = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    ret, frame = vid.read()
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    caract = clasif.detectMultiScale(gris, 1.1, 8)
    eyee = eye.detectMultiScale(gris, 1.1, 8)
    for(x,y,w,h) in eyee:
        cv2.rectangle(frame, (x,y), (x+w, y + h), (255,0,0), 2)
    for(x,y,w,h) in caract:
        cv2.rectangle(frame, (x,y), (x+w, y + h), (0,0,255), 2)
    cv2.imshow("michi", frame)
    if cv2.waitKey(1) == 32: break


vid.release()
