def getValue(file, ra, dec):
    """
    Pulls map value at given ra & dec.

    Parameters
    ----------
    file : string
        path name of map file
    ra   : float
        right ascension of target in decimal degrees
    dec  : float
        declination of target in decimal degrees
    
    Returns
    -------
    value : float
        value at given location within map. (nan = not in map)
    """
    from IsCoordInMap import IsInMap
    import astropy.io.fits as pyfits
    
    hdulist = pyfits.open(file)
    map = hdulist[0].data
    
    isInMap, xVal, yVal = IsInMap(file, ra, dec)
    
    if isInMap == True:
        value = map[yVal, xVal]      
    else:
        value = float("nan")
    
    return(value)
