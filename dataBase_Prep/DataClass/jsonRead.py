'''
Created on 9 de out de 2018

@author: aoliveir
'''

import json
from pathlib import Path
import sys
import os
import cv2



class readJSON():
    
    def loadJSON(self):
        
        #PAth to files
        data_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/source_Data/bdd100k_labels_release/bdd100k/labels")
        image_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/image_data")
        train_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/source_Data/path2train")
        path2File = data_folder / "bdd100k_labels_images_val.json"
        
        # new class readJSON
        dataJSON = readJSON()
       
        #variables to get data from JSON
        type = ""
        x1 = ""
        y1 = ""
        x2 = ""
        y2 = ""    
        
        with open(path2File, mode='r') as read_file:
            
            #read JSON file
            annotations = json.load(read_file)
            
            for annotation in annotations:
                
                #get img data
                height, width = dataJSON.loadIMG(annotation["name"])
                    
                #save img path to txt
                path2image = image_folder / annotation["name"]
                dataJSON.writeTXT_train(path2image)
                
                for annotation_labels in annotation["labels"]:
                    
                    if 'box2d' not in annotation_labels:
                        continue
                    
                    type = annotation_labels["category"]
                    x1 = annotation_labels["box2d"]['x1']
                    y1 = annotation_labels["box2d"]['y1']
                    x2 = annotation_labels["box2d"]['x2']
                    y2 = annotation_labels["box2d"]['y2']
                    
                    print(annotation["name"]+',',annotation_labels["category"]+',',annotation_labels["box2d"]['x1'],annotation_labels["box2d"]['y1'],annotation_labels["box2d"]['x2'],annotation_labels["box2d"]['y2'])                      
                    
                    img_Data = annotation_labels["category"] +" ",annotation_labels["box2d"]['x1'],annotation_labels["box2d"]['y1'],annotation_labels["box2d"]['x2'],annotation_labels["box2d"]['y2']
                    
                    path2train = train_folder / annotation["name"]
                    
                    dataJSON.writeTXT_bddbox2D(path2train,img_Data)
                       
        return 0            
                       
    def loadIMG(self,imgFileName):
        
        image_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/image_data")   
        path2image = image_folder / imgFileName
        img = cv2.imread(path2image,1)
             
        height, width, channels = img.shape
    
        print(height, width, channels) 
  
        return height, width
    
    
    #write all file to be trained names in a txt file
    def writeTXT_train(self,path2image):
        
        
        train_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/source_Data/path2train")
        list2train = train_folder / "train.txt"
        
        with open(list2train, mode='a') as filewriter:
            
            filewriter.write(str(path2image) + "\n")
            
            filewriter.close()
                      
        return 0
    
    def writeTXT_bddbox2D(self,path2File,img_Data):
           
        with open(path2File, mode='w') as filewriter:
            
            #writer = writer(filewriter, delimiter=' ')
            filewriter.write(img_Data +"\n")
            
            filewriter.close()
                      
        return 0               
  
if __name__ == "__main__":
    
    dataJSON = readJSON()
    
    dataJSON.loadJSON()
    
    
   