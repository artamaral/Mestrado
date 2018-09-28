'''
Created on 28 de set de 2018

@author: aoliveir
'''
from pathlib import Path
import csv 
import sys
import kitti_bbox2D



class readTXT():

    def readTXT_kittibbox2D(self,path2File):
        
        objRead = kitti_bbox2D.Kitti_bbox2D
        with open(path2File, mode='r') as csv_file:
            
            csv_reader = csv.DictReader(csv_file, delimiter=' ')
            print(csv_reader)
            
            for row in csv_reader:
                
                print(row)
                
                objRead.type = row[0]
                objRead.truncated = row[1] 
                objRead.occluded = row[2]
                objRead.alpha = row[3]
                objRead.bbox = [row[4],row[5],row[6],row[7]]
                objRead.dimensions = [row[8],row[9],row[10]]
                objRead.location = [row[11],row[12],row[13]]
                objRead.rotation_y = row[14]
                objRead.score = row[15]
                
            print(objRead)                    
            return 0
    
    def path2read(self):    
    
        data_folder = Path("C:/Users/aoliveir/eclipse-workspace/dataBase_Prep/source_Data")

        path2File = data_folder / "000001.txt"
        print("File to open ",path2File)
        return path2File
    
if __name__ == "__main__":
    
    obj_class = readTXT()
    p = obj_class.path2read()
    
    obj_class.readTXT_kittibbox2D(p)
  
    