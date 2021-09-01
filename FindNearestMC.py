"""
Holds functions useful for finding the nearest MC to a location in a galaxy.
"""
import numpy as np
from astropy.table import Table
import os


def int2mass(x, aco, res=150.0):
    area = (res/2.0)**2*np.pi/np.log(2.0)
    y = x * aco * area
    return(y)
    
def mass2int(mass, aco, res=150.0):
    area = (res/2.0)**2*np.pi/np.log(2.0)
    inten = mass / (aco * area)
    return(inten)

def arraySort(variable, distance):
    # sorts variable by shortest distance
    pattern = distance.argsort()
    dist = distance[pattern]
    var = variable[pattern]
    return (var, dist)

def findNearest(varArray, value, distArray):
    # sorts variable by distance, returning closest with given value and that value
    var, dist = arraySort(varArray, distArray) 
    ind = np.where(var >= value)
    
    if len(dist[ind]) > 0:
        nearest    = np.argmin(dist[ind])
        nearDist   = dist[ind][nearest] * 1000
        varVal     = var[ind][nearest]
    else:
        nearDist   = float('nan')
        varVal     = float('nan')
        
    return(varVal, nearDist)


def printNearest(filestr, kind, value, SNRcutoff = 3.0, test = "SNe", distList = None):
    # takes galaxy name, kind of sorting (SNR, Intensity, or Mass), and value we want (min SNR, intensity, or mass) 
    # and returns distance to the nearest molecular cloud and the min value found of kind requested
    # setting test to anything other than "SNe" will access the flat galaxy maps for running the model SNe pop.
    # If running the model population, distList must be used to pass the list of random distances.
            
    if test == "SNe":
        fileName = "/home/mayker.1/Desktop/SNeCO_Data_Products/FlatSNeDistanceMaps/{}FlatSNeData.txt".format(filestr)
        if os.path.isfile(fileName):
            flatData = Table.read(fileName, format = "ascii") 
            distArr = flatData["distSNe"][i]
        else:
            return(np.float('nan'),np.float('nan'))
    else:
        fileName = "/home/mayker.1/Desktop/SNeCO_Data_Products/FlatGalaxyMaps/{}FlatData.txt".format(filestr)
        if os.path.isfile(fileName):
            flatData = Table.read(fileName, format = "ascii") 
            distArr = distList
        else:
            return(np.float('nan'),np.float('nan'))
    
    #apply SNR cutoff
    intenCut, distCut, massCut = [],[],[]
    for i in range(len(flatData)):
        if (flatData["SNR"][i] >= SNRcutoff):
            intenCut.append(flatData["Intensity"][i])
            distCut.append(distArr[i])
            massCut.append(flatData["mass"][i])

    if kind == 'SNR':
        valFound, nearestMCSN = findNearest(np.array(distArr), value, np.array(distArr))    
    elif kind == 'Intensity':
        valFound, nearestMCSN = findNearest(np.array(intenCut), value, np.array(distCut))
    else:
        valFound, nearestMCSN = findNearest(np.array(massCut), value, np.array(distCut))

    return(nearestMCSN, valFound)  
