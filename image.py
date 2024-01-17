import cv2 as cv
import numpy as np
img=cv.imread(r"/home/admin1/Downloads/img.png")
cv.circle(img,(34,105),10,(0,0,0),5)
cv.imshow("image",img)
#cv.putText(img,"learning",(40,110),int(1),(0,150,0),1)
#cv.imshow("text",img)
cv.waitKey(0)
