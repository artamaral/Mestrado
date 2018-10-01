'''
Created on Sep 30, 2018

@author: artamaral
'''

import cv2
import numpy as np


if __name__ == '__main__':
    
    img = cv2.imread("/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/image_data/000000.png",1)
    
    width, height, channels = img.shape
    
    print(width,height, channels)
    
    #761.565 225.46 98.33000000000004 164.92000000000002
    #712.40 143.00 810.73 307.92
    
    pt1 = (int(712.40), int(143.00))
    pt2 = (int(810.73), int(307.92))
    black = (0,0,255)
    
    cv2.rectangle(img, pt1, pt2, black, thickness=3, lineType=8, shift=0)
    
    cv2.imshow('image',img)
    cv2.waitKey(0)
    print("---")
    
  

 
    