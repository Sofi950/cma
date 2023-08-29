import numpy as np  
import cv2 

black = np.zeros([600,600])

#filas = black[1:2]
#print (filas)
#colum = black[:,1:2]
#print(colum)
black[200:400,200:400] = 255
print (black)
cv2.imshow("Foto", black)
cv2.waitKey(0)