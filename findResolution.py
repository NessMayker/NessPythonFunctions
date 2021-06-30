def findRes(beamsize, distance):
    """
    Calculate resolution of a map given beamsize and distance to galaxy.    

    Parameters
    ----------
    beamsize  : float
        beamsize of array in degrees
    distance : float
        distance to galaxy in Mpc
    
    Returns
    -------
    resolution : float
        resolution of map in pc
    """
    import numpy as np
    beamRad = beamsize * np.pi / 180.0
    resolution = np.sin(beamRad/2.0) * distance * 10**6 * 2.0
    return(resolution)