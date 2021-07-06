
import numpy as np

def findErrVals(errArray):
    '''
    Takes the error array and returns the smallest non-zero
    error, the average error, and the median error.
    '''
    nonZeroErrVals = []
    errVals = np.sort(errArray)

    for i in range(len(errArray)):
        if errVals[i] > 0.0:
            nonZeroErrVals.append(errVals[i])
            
    lowErr = nonZeroErrVals[0]
    # aveErr = np.average(nonZeroErrVals)
    # medErr = np.median(nonZeroErrVals)
    
    return(lowErr)

def nonZeroErrArray(errVals, usedErr):
    """
    Takes given error array and replaces 0.0 values with error value of choice.
    """
    nonZErr = []
    #nonZErr = np.where(errVals == 0.0, usedErr, errVals)
    for i in range(len(errVals)):
        if errVals[i] > 0.0:
            nonZErr.append(errVals[i])
        else:
            nonZErr.append(usedErr)
    return(nonZErr)   

def findSignalArray(Int, Err):
    """
    Takes an array of measured values and an array of their errors and returns the SNR array.
    """
    SN = []
    for i in range(len(Int)):
        SN.append(Int[i]/Err[i])
    return(SN)

def findSignal(Int, Err):
    """
    Takes an int and a non-zero err and returns int/err
    """
    
    usedErr = findErrVals(ErrArr)

    if np.isnan(Int) or np.isnan(Err) == True:
        SN = float("nan")
    elif Int == 0.0:
        SN = 0.0
    else:
        SN = float(Int)/float(Err)
    return(SN)
