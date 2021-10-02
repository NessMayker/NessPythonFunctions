
import numpy as np


def atIndex(lst, K, vals): 
    '''
    Returns the value in an second array at the index that is closest to the value requested.


	Parameters
	----------
	lst : array of floats
	    array of values that we want to find requested value
	K : float
		value we want to find in lst
	vals : array of floats
		array we want to retreive number from at found index

	Returns
	-------
	x : array
	    linspace array to plot against CDF
	cdf : array
		CDF array 
    '''


    absVal = []
    
    for i in range(len(lst)):
        number = np.abs((lst[i]) - K)
        absVal.append(number)
    value = np.min(absVal)    
    index = absVal.index(value)
    want  = vals[index]
    return(want)



def getClosest(val1, val2, target):
    if (target - val1 >= val2 - target):
        return(val2)
    else:
        return(val1)            
 
# Returns value closest to target value in sorted array
def findClosest(array, target):
 
    #Edge cases
    if (target <= array[0]):
        return(array[0], 0)

    if (target >= array[-1]):
        return(array[-1], len(array))
 
    #Binary search
    i, j, mid = 0, len(array), 0
    
    while (i < j):
        mid = (i + j) // 2
 
        if (array[mid] == target):
            return(array[mid], np.where(array==target))
 
        # If target is less than middle value, search on left side
        if (target < array[mid]) :
 
            # If target is greater than the previous to middle, return closest of the two
            if (mid > 0 and target > array[mid - 1]):
                value = getClosest(array[mid - 1], array[mid], target)
                return(value, np.where(array==value))
 
            # Repeat for right half
            j = mid
         
        # If target is greater than mid
        else :
            if (mid < len(array) - 1 and target < array[mid + 1]):
                value = getClosest(array[mid], array[mid + 1], target)
                return(value, np.where(array==value))
                 
            # update i
            i = mid + 1
         
    # Only a single value remains after search
    return (array[mid], np.where(array==target))
