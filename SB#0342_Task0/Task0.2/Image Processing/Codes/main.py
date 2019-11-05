import cv2
import numpy as np
import os
import csv 
bird=cv2.imread('../Images/bird.jpg')
cat=cv2.imread('../Images/cat.jpg')
flowers=cv2.imread('../Images/flowers.jpg')
horse=cv2.imread('../Images/horse.jpg')
name=['bird.jpg','cat.jpg','flowers.jpg','horse.jpg']
height=[bird.shape[0],cat.shape[0],flowers.shape[0],horse.shape[0]]
width=[bird.shape[1],cat.shape[1],flowers.shape[1],horse.shape[1]]    
channels=[bird.shape[2],cat.shape[2],flowers.shape[2],horse.shape[2]]
dimensions=[bird.shape,cat.shape,flowers.shape,horse.shape]
center=[bird[height[0]//2][width[0]//2],cat[height[1]//2][width[1]//2],flowers[height[2]//2][width[2]//2],horse[height[3]//2][width[3]//2]]
def partA():
    with open('../Generated/stats.csv','w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0,4):
            filewriter.writerow([name[i],height[i],width[i],channels[i],center[i][0],center[i][1],center[i][2]])
 
def partB():
    red=cat.copy()
    red[:,:,0]=0
    red[:,:,1]=0
    cv2.imwrite('../Generated/cat_red.jpg',red)

def partC():
    img=flowers.copy()
    alpha = np.zeros([img.shape[0],img.shape[1],1], dtype=np.uint8) + 128
    bgra = np.dstack((img,alpha))
    cv2.imwrite('../Generated/flowers_alpha.png',bgra)

def partD():
    h=horse.copy()
    for i in range(0,h.shape[0]):
        for j in range(0,h.shape[1]):
            h[i,j]=0.3*h[i,j,2]+0.59*h[i,j,1]+0.11*h[i,j,0]
    cv2.imwrite('../Generated/horse_gray.jpg',h)

partA()
partB()
partC()
partD()
