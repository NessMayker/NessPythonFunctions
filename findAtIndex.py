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
    import numpy as np

    absVal = []
    
    for i in range(len(lst)):
        number = np.abs((lst[i]) - K)
        absVal.append(number)
    value = np.min(absVal)    
    index = absVal.index(value)
    want  = vals[index]
    return(want)