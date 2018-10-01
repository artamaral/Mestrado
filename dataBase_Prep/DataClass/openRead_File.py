'''
Created on Sep 29, 2018

@author: artamaral
'''
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
        
        data_folder = Path("/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/source_Data/")
        image_folder = Path("/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/image_Data/")
        
        path2File = data_folder / "000000.txt"
        path2image = image_folder / "000000.png"
        
        img = cv2.imread("/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/image_data/000000.png",0)
        cv2.imshow('image',img)
        
        #with open(path2File, mode='r') as :

        
        # to separate the file name from path
        head, tail = os.path.split(path2File)

                
        while (path2File.is_file()):
            
            
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
                    width = float(bbox_r) - float(bbox_l)
                    high = float(bbox_b) - float(bbox_t)        
                    
                    if x_center < 0 or y_center < 0:
                        print(ArithmeticError)
                    
                    print(type, x_center, y_center, width, high)
             
            tail = int(tail[:6])
            tail = tail + 1
            
            if tail == 5:
                break
                        
            if tail < 10:
                tail = "00000" + str(tail)
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
                               
        csv_file.close()              
        return 0
    
    def path2_R_W(self):    
        
        #/Users/artamaral/Downloads/training/label_2
        data_folder = Path("/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/source_Data/")

        path2File = data_folder / "000001.txt"
        print("File to open ",path2File)
        return path2File
    
if __name__ == "__main__":
    
    obj_class = readTXT()
    p = obj_class.path2_R_W()
    
    obj_class.readTXT_kittibbox2D()
  
    
