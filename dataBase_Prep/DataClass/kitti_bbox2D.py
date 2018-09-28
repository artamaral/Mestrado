'''
Created on 28 de set de 2018

@author: aoliveir


kitti class definition


#Values    Name      Description
----------------------------------------------------------------------------
   1    type         Describes the type of object: 'Car', 'Van', 'Truck',
                     'Pedestrian', 'Person_sitting', 'Cyclist', 'Tram',
                     'Misc' or 'DontCare'
   1    truncated    Float from 0 (non-truncated) to 1 (truncated), where
                     truncated refers to the object leaving image boundaries
   1    occluded     Integer (0,1,2,3) indicating occlusion state:
                     0 = fully visible, 1 = partly occluded
                     2 = largely occluded, 3 = unknown
   1    alpha        Observation angle of object, ranging [-pi..pi]
   4    bbox         2D bounding box of object in the image (0-based index):
                     contains left, top, right, bottom pixel coordinates
   3    dimensions   3D object dimensions: height, width, length (in meters)
   3    location     3D object location x,y,z in camera coordinates (in meters)
   1    rotation_y   Rotation ry around Y-axis in camera coordinates [-pi..pi]
   1    score        Only for results: Float, indicating confidence in
                     detection, needed for p/r curves, higher is better.

'''

class Kitti_bbox2D(object):
    '''
    classdocs
    '''


    def __init__(self, type,truncated,occluded,alpha,bbox,dimensions,location,rotation_y,score):
        '''
        Constructor
        '''
        self.type = ""
        self.truncated = truncated
        self.occluded = occluded
        self.alpha=alpha
        self.bbox = [0,0,0,0]
        self.dimension = [0,0,0]
        self.location = [0,0,0]
        self.rotation_y = rotation_y
        self.score = score

    def __lt__(self, value):
        return object.__lt__(self, value)


    def __reduce_ex__(self, protocol):
        return object.__reduce_ex__(self, protocol)


    def __reduce__(self):
        return object.__reduce__(self)


    def __str__(self):
        return object.__str__(self)


    def __getattribute__(self, name):
        return object.__getattribute__(self, name)


    def __eq__(self, value):
        return object.__eq__(self, value)


    def __gt__(self, value):
        return object.__gt__(self, value)


    def __hash__(self):
        return object.__hash__(self)


    def __new__(self,type):
        return object.__new__(type)


    def __delattr__(self, name):
        return object.__delattr__(self, name)


    def __init_subclass__(self, *args, **kwargs):
        return object.__init_subclass__(self, *args, **kwargs)


    def __le__(self, value):
        return object.__le__(self, value)


    def __dir__(self):
        return object.__dir__(self)


    def __subclasshook__(self, *args, **kwargs):
        return object.__subclasshook__(self, *args, **kwargs)


    def __setattr__(self, name, value):
        return object.__setattr__(self, name, value)


    def __sizeof__(self):
        return object.__sizeof__(self)


    def __ge__(self, value):
        return object.__ge__(self, value)


    def __repr__(self):
        return object.__repr__(self)


    def __ne__(self, value):
        return object.__ne__(self, value)


    def __format__(self, format_spec):
        return object.__format__(self, format_spec)

        
        
        