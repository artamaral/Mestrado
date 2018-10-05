'''
Created on 5 de out de 2018

@author: aoliveir
'''
from pathlib import Path
import csv 
import sys
import kitti_bbox2D
import os
from builtins import str

class CUlane_readTXT():
    '''
    classdocs
    '''



    def readTXT_CUlane_Polyline(self):
        
        
        data_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/source_Data")
        image_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/image_data")
        train_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/source_Data/path2train")
        
        path2File = data_folder / "00030.txt"
        path2image = image_folder / "000000.png"
        path2train = train_folder / "000000.txt"
        list2train = train_folder / "train.txt"
        
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
        
        polyline = []
        x_polyline = 0
        y_polyline = 0
        # while exist a file in the folder, keep doing!        
        while (path2File.is_file()):
                   
            #Opena file as csv
            with open(path2File, mode='r',errors="strict") as csv_file:
                
                #since files has a space between string...separate  at each space
                csv_reader = csv.reader(csv_file, delimiter=" ")
                
                
                # for each string in the line
                for row in csv_reader:
                    
                    x = 0
                    y = 1
                    
                    lenghtCSV = len(row)
                    #if in the end of file, break!
                    if row[0] == "":
                        break
                    
                    for a in row:
                        if y < lenghtCSV:
                            x_polyline = row[x]
                            y_polyline = row[y]
                            polyline.append([x_polyline,y_polyline])
                            x = x + 2
                            y = y + 2
                        
                                 
                    
                    '''
                        # do the mats as necessary for darknet
                        #x_center = float(bbox_l) + (float(bbox_r) - float(bbox_l))/2
                        #y_center = float(bbox_t) + (float(bbox_b) - float(bbox_t))/2
                        #x_width = float(bbox_r) - float(bbox_l)
                        #y_high = float(bbox_b) - float(bbox_t)        
                        
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
            '''                   
            print(polyline)
            csv_file.close()
            break
            
                        
        return 0
    
    
    def writeTXT_kittibbox2D(self,path2File,img_Data):
        
        
        with open(path2File, mode='w') as filewriter:
            
            #writer = writer(filewriter, delimiter=' ')
            filewriter.write(img_Data +"\n")
            
            filewriter.close()
                      
        return 0  
    
    def writeTXT_train(self,list2train,path2image):
        
        
        with open(list2train, mode='a') as filewriter:
            
            #writer = writer(filewriter, delimiter=' ')
            filewriter.write(str(path2image) + "\n")
            
            filewriter.close()
                      
        return 0  
    
    
if __name__ == "__main__":
    
    obj_class = CUlane_readTXT()
    #p = obj_class.path2_R_W()
    
    obj_class.readTXT_CUlane_Polyline()