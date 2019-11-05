import cv2
import numpy as np
import os

def partA():
    read=cv2.VideoCapture('../Videos/RoseBloom.mp4')
    v,i = read.read()
    flag=0
    while v:
    	if flag==150:
    		cv2.imwrite('../Generated/frame_as_6.jpg',i)
    		break
    	flag+=1
    	v,i=read.read()


def partB():
    img=cv2.imread('../Generated/frame_as_6.jpg')
    red=img.copy()
    red[:,:,0]=0
    red[:,:,1]=0
    cv2.imwrite('../Generated/frame_as_6_red.jpg',red)
partA()
partB()
