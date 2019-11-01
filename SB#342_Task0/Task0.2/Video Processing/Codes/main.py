import cv2 as cv
import numpy as np
import os

def partA():
    read=cv.VideoCapture('/home/aditya/eYantra/SB#342_Task0/Task0.2/Video Processing/Videos/RoseBloom.mp4')
    v,i = read.read()
    flag=0
    while v:
    	if flag==150:
    		cv.imwrite('/home/aditya/eYantra/SB#342_Task0/Task0.2/Video Processing/Generated/frame_as_6.jpg',i)
    		break
    	#cv.imwrite('/home/aditya/eYantra/SB#342_Task0/Task0.2/Video Processing/Generated/frame_as_6.jpg',i)
    	#cv.imshow(i)
    	#cv.waitKey(1000)
    	#cv.destroyAllWindows()
    	flag+=1
    	v,i=read.read()


def partB():
    img=cv.imread('/home/aditya/eYantra/SB#342_Task0/Task0.2/Video Processing/Generated/frame_as_6.jpg')
    red=img.copy()
    red[:,:,0]=0
    red[:,:,1]=0
    cv.imwrite('/home/aditya/eYantra/SB#342_Task0/Task0.2/Video Processing/Generated/frame_as_6_red.jpg',red)
partA()
partB()