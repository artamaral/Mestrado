'''
Created on 9 de out de 2018

@author: aoliveir
'''

import json
from pathlib import Path
import sys
import os
from builtins import str
from _ast import Return



class readJSON():
    
    def loadJSON(self):
        
        data_folder = Path("C:/Users/aoliveir/git/Mestrado/dataBase_Prep/source_Data/bdd100k_labels_release/bdd100k/labels")
        
        path2File = data_folder / "bdd100k_labels_images_val.json"

        with open(path2File, mode='r') as read_file:
            
            annotations = json.load(read_file)
            
            for annotation in annotations:
                
                for annotation_labels in annotation["labels"]:
                    
                    if 'box2d' not in annotation_labels:
                        continue
                    
                    print(annotation["name"]+',',annotation_labels["category"]+',',annotation_labels["box2d"]['x1'],annotation_labels["box2d"]['y1'],annotation_labels["box2d"]['x2'],annotation_labels["box2d"]['y2'])    
                        #for annotation_box2d in annotation_labels["box2d"]:
                        
                        #print(annotation["name"],annotation_labels["category"],annotation_box2d["x1"],annotation_box2d["y1"],annotation_box2d["x2"], annotation_box2d["y2"] )
                    
                       
  
  
if __name__ == "__main__":
    
    dataJSON = readJSON()
    
    dataJSON.loadJSON()
    
    
   