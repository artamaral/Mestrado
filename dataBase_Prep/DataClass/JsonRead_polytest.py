'''
Created on 9 de out de 2018

@author: aoliveir
'''

import json
from pathlib import Path
import sys
import os



class readJSON():
    
    def loadJSON(self):
        
        #PAth to files
        data_folder = Path("C:/Users/aoliveir/Documents/bdd100k_labels_release/bdd100k/labels")
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
        vertices = []
        obj_Xcenter = 0
        obj_Ycenter = 0
        obj_height = 0
        obj_width = 0   
        
        with open(path2File, mode='r') as read_file:
            
            #read JSON file
            annotations = json.load(read_file)
            
            #going deep on json           
            for annotation in annotations:
                
                #get img data
                #height, width = dataJSON.loadIMG(annotation["name"])
                    
                #save img path to txt
                path2image = image_folder / annotation["name"]
                dataJSON.writeTXT_train(path2image)
                
                #deeper on json                
                for annotation_labels in annotation["labels"]:
                    
                    #print(annotation["name"] + ',' + str(annotation["labels"]))
                    
                    #if the object does not have a box2d annotation...avoid error of null object 
                    if 'box2d' not in annotation_labels:
                        
                        #get object annotation from poly2d since it does not have box2d info 
                        for polys in annotation_labels["poly2d"]:
                            
                            #clear the aux variables
                            x = 0
                            y = 0
                            x1 = 0
                            y1 = 0
                            x2 = 0
                            y2 = 0    
                            
                            #get the poly2d array from json
                            vertices.append(polys["vertices"])
                            #print(polys["vertices"])
                            
                            #for each vertice get list  of point
                            for points in vertices:
                                
                                #from a list of points get each coordinates
                                for coordenates in points:
                                                            
                                    x = coordenates[0]
                                    y = coordenates[1]
                                    #print("x:" + str(x) +" y:" + str(y))
                                    
                                    '''
                                    Since polylines can have multiples vertices
                                    and assuming that the object is inside of it
                                    get the  most top left and bottom right coordinates
                                    to inscribe a rectangle
                                    '''
                                    if x <= x1 or x1 == 0:
                                        x1 = x
                                    
                                    if x > x2 or x2 == 0:
                                        x2 = x
                                    
                                    if y > y1 or y1 == 0:
                                        y1 = y
                                    
                                    if y <= y2 or y2 == 0:
                                        y2 = y        
                                                       
                            obj_Xcenter = (x1+x2)/2
                            obj_Ycenter = (y1+y2)/2
                            obj_width = x2 - x1
                            obj_height = y1 - y2
                            print(x1,x2,y1,y2)
                            print(str(annotation["name"])+',',str(annotation_labels["category"])+',', str(obj_Xcenter) + ',' ,str(obj_Ycenter)+ ',' ,str(obj_width)+ ',' ,str(obj_height)) 
                            vertices.clear()
                            #if we find a polyline get it break to check the next 'label'
                           
                            break
                        #if we have a box2d go on...                                               
                        continue
                    
                    #alse get info from box2d
                    else:
                        
                        type = annotation_labels["category"]
                        x1 = annotation_labels["box2d"]['x1']
                        y1 = annotation_labels["box2d"]['y2']
                        x2 = annotation_labels["box2d"]['x2']
                        y2 = annotation_labels["box2d"]['y1']
                        
                        obj_Xcenter = (x1+x2)/2
                        obj_Ycenter = (y1+y2)/2
                        obj_width = x2 - x1
                        obj_height = y1 - y2
                        
                        print(x1,x2,y1,y2)
                        print(str(annotation["name"])+',',str(annotation_labels["category"])+',', str(obj_Xcenter) + ',' ,str(obj_Ycenter)+ ',' ,str(obj_width)+ ',' ,str(obj_height)) 
                   
                    #prepare variable to write darknet std file    
                    img_Data = annotation_labels["category"] +" ",annotation_labels["box2d"]['x1'],annotation_labels["box2d"]['y1'],annotation_labels["box2d"]['x2'],annotation_labels["box2d"]['y2']
                    
                    path2train = train_folder / annotation["name"]
                    
                                        #dataJSON.writeTXT_bddbox2D(path2train,img_Data)
                       
        return 0            
                       
    def loadIMG(self,imgFileName):
        
        image_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/image_data")   
        path2image = image_folder / imgFileName
        #img = cv2.imread(path2image,1)     
        #height, width, channels = img.shape
    
        #print(height, width, channels) 
  
        #return height, width
    
    
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
    
    
   