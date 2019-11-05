import cv2 as cv
import numpy as np
import os

def partA():
    read=cv.VideoCapture('/SB#0342_Task0/Task0.2/Video Processing/Videos/RoseBloom.mp4')
    v,i = read.read()
    flag=0
    while v:
    	if flag==150:
    		cv.imwrite('/SB#0342_Task0/Task0.2/Video Processing/Generated/frame_as_6.jpg',i)
    		break
    	flag+=1
    	v,i=read.read()


def partB():
    img=cv.imread('/SB#0342_Task0/Task0.2/Video Processing/Generated/frame_as_6.jpg')
    red=img.copy()
    red[:,:,0]=0
    red[:,:,1]=0
    cv.imwrite('/SB#0342_Task0/Task0.2/Video Processing/Generated/frame_as_6_red.jpg',red)
partA()
partB()
