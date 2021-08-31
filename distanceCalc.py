"""
Calculates the distance between two points in a galaxy
"""

def distance(x1, x2, y1, y2, galDist):
    #calculate distance between two points (in kpc)
    #x1, y1 = xprime and yprime, x2, y2 = x&y coords, dist = distance to galaxy (kpc)
    # returns distance in pc
    d = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    x = galDist * np.tan(d*np.pi/180)*1000
    return(x)