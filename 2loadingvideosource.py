import cv2
import numpy as np
cap=cv2.VideoCapture(0)
#file open
##fourcc=cv2.VideoWriter_fourcc(*'XVID')
##out=vc2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    if cv2.waitKey(0)& 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


