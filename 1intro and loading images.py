import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('gsw1.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR
#IMREAD_UNCHANGED

##cv2.imshow('image',img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

##plt.imshow(img,cmap='gray',interpolation='bicubic')
##plt.plot([50,100],[80,100])
##plt.show()

cv2.imwrite('gsw1.jpg',img)#to write images

