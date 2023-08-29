import cv2 

vid = cv2.VideoCapture("coca.MOV")
if vid.isOpened() == False:
    print("nosepuedeleerlacamara")

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

#sopa= cv2.VideoWriter("coca.MOV", cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))


while True:
    ret, frame = vid.read()
    cv2.imshow("michi", frame)
    #sopa.write(frame) 
    if cv2.waitKey(1) == 32: break
    

vid.release()
#sopa.release()