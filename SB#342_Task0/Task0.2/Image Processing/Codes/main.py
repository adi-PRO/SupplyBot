import cv2 as cv
import numpy as np
import os
import csv
from PIL import Image 
bird=cv.imread('/SB0#342_Task0/Task0.2/Image Processing/Images/bird.jpg')
cat=cv.imread('/SB#0342_Task0/Task0.2/Image Processing/Images/cat.jpg')
flowers=cv.imread('/SB#0342_Task0/Task0.2/Image Processing/Images/flowers.jpg')
horse=cv.imread('/SB#0342_Task0/Task0.2/Image Processing/Images/horse.jpg')
name=['bird.jpg','cat.jpg','flowers.jpg','horse.jpg']
height=[bird.shape[0],cat.shape[0],flowers.shape[0],horse.shape[0]]
width=[bird.shape[1],cat.shape[1],flowers.shape[1],horse.shape[1]]    
channels=[bird.shape[2],cat.shape[2],flowers.shape[2],horse.shape[2]]
dimensions=[bird.shape,cat.shape,flowers.shape,horse.shape]
center=[bird[height[0]//2][width[0]//2],cat[height[1]//2][width[1]//2],flowers[height[2]//2][width[2]//2],horse[height[3]//2][width[3]//2]]
def partA():
    with open('/SB#0342_Task0/Task0.2/Image Processing/Generated/stats.csv','w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0,4):
            filewriter.writerow([name[i],height[i],width[i],channels[i],center[i][0],center[i][1],center[i][2]])
        """filewriter.writerow(['bird.jpg', 'Profession'])
        filewriter.writerow(['cat.jpg', 'Software Developer'])
        filewriter.writerow(['flowers.jpg', 'Software Developer'])
        filewriter.writerow(['horse.jpg', 'Manager'])"""



def partB():
    red=cat.copy()
    red[:,:,0]=0
    red[:,:,1]=0
    cv.imwrite('/SB#0342_Task0/Task0.2/Image Processing/Generated/cat_red.jpg',red)

def partC():
    alpha=Image.open(r'/SB#0342_Task0/Task0.2/Image Processing/Images/flowers.jpg')
    alpha.putalpha(128)
    """b,r,g=cv.split(flowers)
    a=np.ones(b.shape,dtype=b.dtype)*50
    brga=cv.merge((b,r,g,a))"""
    alpha.save('/SB#0342_Task0/Task0.2/Image Processing/Generated/flowers_alpha.png')    

def partD():
    h=horse
    for i in range(0,h.shape[0]):
        for j in range(0,h.shape[1]):
            h[i,j]=0.3*h[i,j,2]+0.59*h[i,j,1]+0.11*h[i,j,0]
    cv.imwrite('/SB#0342_Task0/Task0.2/Image Processing/Generated/horse_gray.jpg',h)

partA()
partB()
partC()
partD()
