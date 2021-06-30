def detecFrac(lim, array):
    '''
    Returns the fraction of detections in an array given the cutoff.
        Parameters
    ----------
    lim   : float
        cutoff limit (detections must be grreater than or equal to)
    array : array
        array of values to search for detections
    
    Returns
    -------
    frac : float
        detection fraction
    '''

    import numpy as np

    k, l = 0, 0
    
    for i in range(len(array)):
        if (np.isnan(array[i]) == False):
            l += 1
            if (array[i] >= lim):
                k += 1

    frac = (k*1.0)/(l*1.0)

    return(frac)