"""
Holds functions useful for finding the nearest MC to a location in a galaxy.
"""

import os
import numpy as np
import astropy.io.fits as pyfits
from astropy.io import ascii
from astropy.table import Table
from astropy.wcs import WCS
from reproject import reproject_interp

import sys
sys.path.append('/home/mayker.1/Desktop/PythonFunctions')
from deprojectGalaxy import deproject

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

def nearestMCMethod(galaxy, image, errimage, alphaCOimg, centerCoord, pa, incl, galDist, otherra, otherdec, othername):
    
    if os.path.isfile(image):

        # read in fits files
        area = (150.0/2.0)**2*np.pi/np.log(2.0)
        hdu_int  = pyfits.open(image)
        intMap      = hdu_int[0].data

        hdu_err = pyfits.open(errimage)
        errMap      = hdu_err[0].data

        if(os.path.isfile(alphaCOimg)):
            hdu_aco  = pyfits.open(alphaCOimg)

            acoMap, footprint = reproject_interp(hdu_aco, hdu_int[0].header) 

            massMap = intMap * acoMap * area
        else: massMap = intMap * 6.7 * area

        #Convert x & y pixels to ra and dec
        wcs      = WCS(hdu_int[0].header, naxis=2)
        naxis    = wcs._naxis # size of image naxis[0] = x and [1] = y
        grid     = np.indices((naxis[1],naxis[0]))
        ra, dec  = wcs.wcs_pix2world(grid[1],grid[0],0)

        #deproject ra and dec to dx and dy
        radius, projang, dx, dy = deproject(center_coord=centerCoord, incl=incl, pa=pa, ra=ra, dec=dec,return_offset=True)

        #flatten data structures 
        f_int  = intMap.flatten()
        f_err  = errMap.flatten()
        f_mass = massMap.flatten()
        f_ra   = ra.flatten()
        f_dec  = dec.flatten()    
        f_dx   = dx.flatten()
        f_dy   = dy.flatten()

        #remove nans
        keep  = np.where(np.isfinite(f_int))
        ra    = f_ra[keep]
        dec   = f_dec[keep]
        inten = f_int[keep]
        err   = f_err[keep]
        mass  = f_mass[keep]
        dx    = f_dx[keep]
        dy    = f_dy[keep]

        SNR = []
        for i in range(len(inten)):
            if err[i] == 0.0:
                SNR.append(0.0)
            elif inten[i] < 0.0:
                SNR.append(0.0)           
            else:
                SNR.append(inten[i]/err[i])
        SNR = np.array(SNR)      
        
        
        print("at Mass cutoff A for", galaxy)
        
        idx  = (mass > 10**5.5) * (SNR > 3.0)
        mass = mass[idx]
        dx   = dx[idx]
        dy   = dy[idx]
            
        otherRad, otherPA, otherdx, otherdy = deproject(center_coord=centerCoord, incl=incl, pa=pa, ra=otherra, dec=otherdec, return_offset=True)           

        nearestMCx55 = findNearest(dx, otherdx, dy, otherdy)
        nearestMC55 = angDistToPc(nearestMCx55,galDist)
        
        print("Nearest 55", nearestMC55, galaxy)        
        
        idx  = (mass > 10**6.5) 
        mass = mass[idx]
        dx   = dx[idx]
        dy   = dy[idx]
            
        nearestMCx65 = findNearest(dx, otherdx, dy, otherdy)
        nearestMC65 = angDistToPc(nearestMCx65,galDist)                    
        
        print("Nearest 65", nearestMC65, galaxy)        
        
        print("done with", galaxy, " ", othername)  
        return(nearestMC55, nearestMC65)
    else:
        print("No file for ", galaxy)
        n55, n66 = [],[]
        for j in range(len(othername)):
            n55.append(float("nan"))
            n66.append(float("nan"))
        return(n55, n66)


