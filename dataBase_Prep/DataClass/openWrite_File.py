'''
Created on 4 de out de 2018

@author: aoliveir
'''
from pathlib import Path
import csv 
import sys
import kitti_bbox2D
import os
from builtins import str



#read and write data from training kitti data
class readTXT():

    def readTXT_kittibbox2D(self):
        
        #/Users/artamaral/darknet/kitti
        #/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/source_Data/
        #/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/data_object_image_2/training
        #/Users/artamaral/darknet/kitti/source_Data"
        #/Users/artamaral/Google Drive/Programação/Java/Mestrado/dataBase_Prep/data_object_image_2/training/image_2"

        data_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/source_Data")
        image_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/image_data")
        train_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/source_Data/path2train")
        
        path2File = data_folder / "000000.txt"
        path2image = image_folder / "000000.png"
        path2train = train_folder / "000000.txt"
        list2train = train_folder / "train.txt"
        
        #path2image =str(path2image)
        
        print(path2image)
        print(path2train)
        print(path2File)
        
        
        # Print image
        #img = cv2.imread(path2image,1)
        #cv2.imshow('image',img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()


        # to separate the file name from path
        head, tail = os.path.split(path2File)
        head2, tail2 = os.path.split(path2image)

        # while exist a file in the folder, keep doing!        
        while (path2File.is_file()):
                   
            #Opena file as csv
            with open(path2File, mode='r',errors="strict") as csv_file:
                
                #since files has a space between string...separate  at each space
                csv_reader = csv.reader(csv_file, delimiter=" ")
                
                # for each string in the line
                for row in csv_reader:
                
                    #if in the end of file, break!
                    if row[0] == "":
                        break
                    
                    #if it's not category I want skip!
                    if row[0] == "Misc" or row[0] == "DontCare":
                        print("Skip: ",row[0])
                    
                    #get the fields necessary
                    else:   
                        type = row[0]
                        bbox_l = row[4]
                        bbox_t = row[5]
                        bbox_r = row[6]
                        bbox_b = row[7]
                        
                        # do the mats as necessary for darknet
                        x_center = float(bbox_l) + (float(bbox_r) - float(bbox_l))/2
                        y_center = float(bbox_t) + (float(bbox_b) - float(bbox_t))/2
                        x_width = float(bbox_r) - float(bbox_l)
                        y_high = float(bbox_b) - float(bbox_t)        
                        
                        # if some data  seems to be wrong
                        if x_center < 0 or y_center < 0:
                            print(ArithmeticError)
                            
                        
                        # print(height, width, channels)
                        print(type, x_center, y_center, x_width, y_high)
                        
                        img_Data = str(type) + " " + str(x_center) + " " + str(y_center) + " " + str(x_width) + " " + str(y_high)
                        
                        print(path2train)               
                        readTXT.writeTXT_kittibbox2D(self,path2train,img_Data)
            
            #height, width, channels = img.shape
            #print(height, width, channels) 
            
            readTXT.writeTXT_train(self,list2train,path2image)
            
            #get the file name, extract the extension and update the counter... 
            tail = int(tail[:6])
            tail = tail + 1
            
            tail2 = int(tail2[:6])
            tail2 = tail2 + 1
        
            #transform back the updated file name as a string            
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
            
            # Write the full parth of files
            fileName =  str(tail) + ".txt"
            path2File = data_folder / fileName
            path2train = train_folder / fileName
                     
            fileName =  str(tail2) + ".png"
            path2image = image_folder / fileName
            path2image = str(path2image)
            
            #img_Data = str(type) + " " + str(x_center) + " " + str(y_center) + " " + str(x_width) + " " + str(y_high)
            
            #readTXT.writeTXT_kittibbox2D(self,path2File,img_Data)
                               
            csv_file.close()
            
                        
        return 0
    
    
    def writeTXT_kittibbox2D(self,path2File,img_Data):
        
        
        with open(path2File, mode='w') as filewriter:
            
            #writer = writer(filewriter, delimiter=' ')
            filewriter.write(img_Data +"\n")
            
            filewriter.close()
                      
        return 0  
    
    #write all file to be trained names in a txt file
    def writeTXT_train(self,list2train,path2image):
        
        
        with open(list2train, mode='a') as filewriter:
            
            #writer = writer(filewriter, delimiter=' ')
            filewriter.write(str(path2image) + "\n")
            
            filewriter.close()
                      
        return 0  
    
    
if __name__ == "__main__":
    
    obj_class = readTXT()
    #p = obj_class.path2_R_W()
    
    obj_class.readTXT_kittibbox2D()
  
    






     