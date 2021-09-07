"""
Holds functions useful for finding the nearest MC to a location in a galaxy.
"""
import numpy as np

def int2mass(x, aco, res=150.0):
    area = (res/2.0)**2*np.pi/np.log(2.0)
    y = x * aco * area
    return(y)
    
def mass2int(mass, aco, res=150.0):
    area = (res/2.0)**2*np.pi/np.log(2.0)
    inten = mass / (aco * area)
    return(inten)

def angDistToPc(x,galDist):
    return(galDist*10**6*np.tan(x*np.pi/180))

def findNearest(x1,x2,y1,y2):
    # Where x1 & y1 are 1d arrays of map coordinates
    # x2,y2 are the coords of the SNe
    n = len(x1)
    m = len(x2)
    if n != 0:
        x1Vec = np.tile(x1, (m,1)) #constant x along column
        y1Vec = np.tile(y1, (m,1)) #constant y along column
        x2Vec = np.tile(x2, (n,1)) #constant x along column
        y2Vec = np.tile(y2, (n,1)) #constant y along column
        x2Vec = np.transpose(x2Vec) #constant x along rows
        y2Vec = np.transpose(y2Vec) #constant y along rows

        dist = np.sqrt((x1Vec-x2Vec)**2 + (y1Vec-y2Vec)**2)    

        mindist = np.nanmin(dist, axis = 1)
    else: 
        mindist = float("nan")
    
    return(mindist)
