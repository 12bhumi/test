import cv2 as cv
import numpy as np
img=cv.imread(r"/home/admin1/Downloads/img.png")
width,height=200,300
pts1=np.float32([[68,54],[97,47],[86,98],[112,82]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv.getPerspectiveTransform(pts1,pts2)
imgout=cv.warpPerspective(img,matrix,[width,height])
cv.imshow("image",img)
cv.imshow("cropped",imgout)
cv.waitKey(0)
