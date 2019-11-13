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
    cir_cen=[]
    #Detection of red circle and its center starts here
    lowerRed=np.array([0,0,83])
    upperRed=np.array([80,51,255])
    mask_red=cv2.inRange(ip_image,lowerRed,upperRed)
    res_red=cv2.bitwise_and(ip_image,ip_image,mask=mask_red)
    red_gray=cv2.cvtColor(res_red,cv2.COLOR_BGR2GRAY)
    circles_red = cv2.HoughCircles(red_gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles_red = np.uint16(np.around(circles_red))
    for i in circles_red[0,:]:
        cir_cen.append([i[0],i[1]])
    print(cir_cen[0][0],cir_cen[0][1])
    xr=cir_cen[0][0]
    yr=cir_cen[0][1]
    #Detection of RED circle ends here
    #Detection of GREEN circle starts here
    lowerGreen=np.array([0,165,0])
    upperGreen=np.array([154,255,255])
    mask_green=cv2.inRange(ip_image,lowerGreen,upperGreen)
    res_green=cv2.bitwise_and(ip_image,ip_image,mask=mask_green)
    green_gray=cv2.cvtColor(res_green,cv2.COLOR_BGR2GRAY)
    cv2.imshow('thresholded',green_gray)
    circles_green=cv2.HoughCircles(green_gray,cv2.HOUGH_GRADIENT,2,20,param1=50,param2=30,minRadius=0,maxRadius= 0)
    circles_green = np.uint16(np.around(circles_green))
    for i in circles_green[0,:]:
        cir_cen.append([i[0],i[1]])
    cv2.imshow('detected circles',res_green)
    print(cir_cen[1][0],cir_cen[1][1])
    xg=cir_cen[1][0]
    yg=cir_cen[1][1]
    #Detection of GREEN CIRCLE ENDS HERE
    #Calculation of angle begins
    angle = 0.00
    xc,yc=ip_image.shape[0]//2,ip_image.shape[1]//2
    m1=-1*(yc-yr)/(xc-xr)
    m2=-1*(yc-yg)/(xc-xg)
    ang1=0
    ang2=0
    if(xc==xr):
        if(yr>yc):
            ang1=270
        else:
            ang1=90
    if(xc==xg):
        if(yg>yc):
            ang2=270
        else:
            ang2=90
    if(yc==yr):
        if(xr<xc):
            ang1=180
        else:
            ang1=0
    if(yc==yg):
        if(xg<xc):
            ang2=180
        else:
            ang2=0
    if(ang1==0):
        ang1=math.degrees(math.atan((m1)))
        if(xr<xc and yr>yc):
            ang1+=180          #third quadrant
        elif(xr<xc and yr<yc):
            ang1+=180     #2nd quadrant
        elif(xr>xc and yr>yc):
            ang1+=360   #4th quadrant
    if(ang2==0):
        ang2=math.degrees(math.atan((m2)))
        if(xg<xc and yg>yc):
            ang2+=180          #third quadrant
        elif(xg<xc and yg<yc):
            ang2+=180     #2nd quadrant
        elif(xg>xc and yg>yc):
            ang2+=360   #4th quadrant
    angle=abs(ang2-ang1)
    if(angle > 180):
        angle=360-angle
    angle = float("{0:.2f}".format(angle))
    cv2.imshow("window", ip_image)
    cv2.waitKey(1)
    return angle




    
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
    line = []
    ## Reading 1 image at a time from the Images folder
    for image_name in os.listdir(images_folder_path):
        ## verifying name of image
        print(image_name)
        ## reading in image 
        ip_image = cv2.imread(images_folder_path+"/"+image_name)
        ## verifying image has content
        print(ip_image.shape)
        ## passing read in image to process function
        A = process(ip_image)
        ## saving the output in  a list variable
        line.append([str(i), image_name , str(A)])
        ## incrementing counter variable
        i+=1
    ## verifying all data
    print(line)
    ## writing to angles.csv in Generated folder without spaces
    with open(generated_folder_path+"/"+'angles.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(line)
    ## closing csv file    
    writeFile.close()



    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
