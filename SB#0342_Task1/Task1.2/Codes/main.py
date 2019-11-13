###############################################################################
## Author: Team Supply Bot
## Edition: eYRC 2019-20
## Instructions: Do Not modify the basic skeletal structure of given APIs!!!
###############################################################################


######################
## Essential libraries
######################
import cv2
import numpy as np
import os
import math
import csv




########################################################################
## using os to generalise Input-Output
########################################################################
codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Images'))
generated_folder_path = os.path.abspath(os.path.join('..', 'Generated'))




############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################
def process(ip_image):
    ###########################
    ## Your Code goes here
    ## placeholder image
    sector_image = np.ones(ip_image.shape[:2],np.uint8)*255
    ## check value is white or not
    print(sector_image[0,0])
    ## Your Code goes here
    ###########################
    #MASKING
    lowerwhite=np.array([255,255,255])
    upperwhite=np.array([255,255,255])
    sector_image=cv2.inRange(ip_image,lowerwhite,upperwhite)
    sector_image=cv2.bitwise_and(ip_image,ip_image,mask=sector_image)
    sector_image=cv2.bitwise_not(sector_image)
    #Extract outside big circle
    cimg=ip_image.copy()
    img=cv2.cvtColor(ip_image,cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=50,param2=50,minRadius=300,maxRadius=330)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    #center of circle
    x=circles[0,0,0]
    y=circles[0,0,1]
    #Remove everything except boundary of circle detected
    for i in range(0,ip_image.shape[0]):
        for j in range(0,ip_image.shape[1]):
            if (cimg[i,j,0]==0 and cimg[i,j,1]==255 and cimg[i,j,2]==0): 
                cimg[i,j,0]=0
                cimg[i,j,1]=0
                cimg[i,j,2]=0
            else:
                cimg[i,j,0]=255
                cimg[i,j,1]=255
                cimg[i,j,2]=255
    #Removal of unwanted portions from Masked Image
    for i in range(0,ip_image.shape[0]):
        for j in range(0,ip_image.shape[1]):
            if (cimg[i,j,0]==255 and cimg[i,j,1]==255 and cimg[i,j,2]==255):
                sector_image[i,j,0]=255
                sector_image[i,j,1]=255
                sector_image[i,j,2]=255
            else:
                break
    for i in range(ip_image.shape[0]-1,0,-1):
        for j in range(ip_image.shape[1]-1,0,-1):
            if (cimg[i,j,0]==255 and cimg[i,j,1]==255 and cimg[i,j,2]==255):
                sector_image[i,j,0]=255
                sector_image[i,j,1]=255
                sector_image[i,j,2]=255
            else:
                break
    for i in range(x-20,x+20):
        for j in range(y-20,y+20):
            sector_image[i,j,0]=255
            sector_image[i,j,1]=255
            sector_image[i,j,2]=255
    print(sector_image.shape)
    cv2.imshow("window", sector_image)
    cv2.waitKey(1);
    return sector_image




    
####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Do not modify this code!!!
####################################################################
def main():
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    ## Reading 1 image at a time from the Images folder
    for image_name in os.listdir(images_folder_path):
        ## verifying name of image
        print(image_name)
        ## reading in image 
        ip_image = cv2.imread(images_folder_path+"/"+image_name)
        ## verifying image has content
        print(ip_image.shape)
        ## passing read in image to process function
        sector_image = process(ip_image)
        ## saving the output in  an image of said name in the Generated folder
        cv2.imwrite(generated_folder_path+"/"+"image_"+str(i)+"_fill_in.png", sector_image)
        i+=1


    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
