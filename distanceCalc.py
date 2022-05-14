"""
Calculates the distance between two points in a galaxy
"""
import numpy as np

def distance(x1, x2, y1, y2, galDist):
    #calculate distance between two points (in pc)
    #x1, y1 = xprime and yprime, x2, y2 = x&y coords, dist = distance to galaxy (Mpc)
    # returns distance in pc
    d = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    x = galDist *10**6 * np.tan(d*np.pi/180)*100))
    return(x)
