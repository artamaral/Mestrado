'''
Created on Sep 29, 2018

@author: artamaral
'''
from builtins import str
'''
Created on 28 de set de 2018

@author: aoliveir
'''
from pathlib import Path
import csv 
import sys
import kitti_bbox2D
import os
#import numpy as np
import cv2


class readTXT():

    def readTXT_kittibbox2D(self):
        
        #/Users/artamaral/darknet/kitti
        #/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/source_Data/
        #/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/data_object_image_2/training
        data_folder = Path("/Users/artamaral/darknet/kitti/source_Data")
        image_folder = Path("/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/data_object_image_2/training/image_2")
        
        path2File = data_folder / "000000.txt"
        path2image = image_folder / "000000.png"
        
        path2image =str(path2image)
        
        print(path2image)
        
        img = cv2.imread(path2image,1)
        
        #cv2.imshow('image',img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        
        height, width, channels = img.shape
    
        print(height, width, channels)
        

        
        # to separate the file name from path
        head, tail = os.path.split(path2File)
        head2, tail2 = os.path.split(path2image)

        
        print(path2File)
        print(path2File.is_file())
                
        while (path2File.is_file()):
            
            
            img = cv2.imread(path2image,1)
            
            with open(path2File, mode='r') as csv_file:
                
                csv_reader = csv.reader(csv_file, delimiter=" ")
                
                for row in csv_reader:
                
                    type = row[0]
                    bbox_l = row[4]
                    bbox_t = row[5]
                    bbox_r = row[6]
                    bbox_b = row[7]
                    
                    x_center = float(bbox_l) + (float(bbox_r) - float(bbox_l))/2
                    y_center = float(bbox_t) + (float(bbox_b) - float(bbox_t))/2
                    x_width = float(bbox_r) - float(bbox_l)
                    y_high = float(bbox_b) - float(bbox_t)        
                    
                    if x_center < 0 or y_center < 0:
                        print(ArithmeticError)
                        
                    height, width, channels = img.shape
                    print(height, width, channels)
                    print(type, x_center/width, y_center/height, x_width/width, y_high/height)
            
            #height, width, channels = img.shape
            #print(height, width, channels) 
            
            tail = int(tail[:6])
            tail = tail + 1
            
            tail2 = int(tail2[:6])
            tail2 = tail2 + 1
            
            if tail == 5:
                break
                        
            if tail < 10:
                tail = "00000" + str(tail)
                tail2 = "00000" + str(tail2)
                print(isinstance(tail, str))
            
            elif tail >= 10 and tail < 100:
                tail = "0000" + str(tail)
                print(isinstance(tail, str)) 
            
            elif tail >= 100 and tail < 1000:
                tail = "000" + str(tail)
                print(isinstance(tail, str))  
            
            elif tail >= 1000 and tail < 10000:
                tail = "00" + str(tail)
                print(isinstance(tail, str)) 
                
            else:
                ArithmeticError    
            
            fileName =  str(tail) + ".txt"
            
            path2File = data_folder / fileName
            print(path2File)
            
            fileName =  str(tail2) + ".png"
            path2image = image_folder / fileName
            path2image = str(path2image)
            
                               
            csv_file.close()
            
                        
        return 0
    
    def path2_R_W(self):    
        
        #/Users/artamaral/Downloads/training/label_2
        data_folder = Path("/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/source_Data/")

        path2File = data_folder / "000001.txt"
        #print("File to open ",path2File)
        return path2File
    
if __name__ == "__main__":
    
    obj_class = readTXT()
    p = obj_class.path2_R_W()
    
    obj_class.readTXT_kittibbox2D()
  
    
