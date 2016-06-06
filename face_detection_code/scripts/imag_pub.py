#!/usr/bin/env python

"""
A ROS node which reads images from a given directory, 
detects faces, and publishes the images with the detected 
faces encircled over the sensor_msgs/Image topic which 
can be subscribed by rviz for visualisation.
"""

import sys
import os
import rospy
import math
import cv2
import glob
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
    
## Command-line function. 
# 
# Reads and checks the number of command-line arguments 
# and calls the imag_pub function
#
#path_name_1 variable is the OpenCV directory
#
#path_name_2 variable is the database directory
def main(argv):
    no_arg = 2
    if not len(sys.argv) > no_arg:
       print 'Please enter only the file paths.'
       sys.exit()    

    path_name_1 = str(sys.argv[1])
    path_name_2 = str(sys.argv[2])
    imag_pub(path_name_1, path_name_2)

##Publisher function.
#    
#Detects faces in an image and publishes it.  
def imag_pub(path_name_1,path_name_2):
    if not os.path.exists(path_name_1):
        print 'Path to the OpenCV directory does not exist.'
        sys.exit()

    if not os.path.exists(path_name_2):
        print 'Path to the image directory does not exist.'
        sys.exit()

    pub = rospy.Publisher("sensor_msgs/Image", Image, queue_size=10)
    rospy.init_node('imag_pub', anonymous=True)
    rate = rospy.Rate(0.5) # 1 Hz
        
    ## loads the required XML classifiers
    file_path_1 = path_name_1 + '/data/haarcascades/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_cascade.load(file_path_1)
  
    
    ## loads the image in grayscale
    image_list=[]
    file_path_2 = path_name_2 + '/*jpg'
    for image in glob.glob(file_path_2):
        img = cv2.imread(image)
        image_list.append(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        ## detects faces & returns positions of faces as Rect(x,y,w,h)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  

        ## draws circles around the detected faces
        for (x,y,w,h) in faces:
            square =(w/3)**2 +(h/3)**2
            radius =int(math.sqrt(square))
            cv2.circle(img,(x+w/2,y+h/2),radius,(0,0,255),2)


        ## converts OpenCV image to ROS image
        bridge= CvBridge()    
        out_image = bridge.cv2_to_imgmsg(img, "bgr8")
        
        
        ## publishes the image with detected faces 
        pub.publish(out_image)
        rate.sleep()
                    
   
if __name__ == '__main__':
  try:
    main(sys.argv)
  except rospy.ROSInterruptException:
    pass
