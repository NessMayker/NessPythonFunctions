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
from normalize import norm



def runModels(galaxy, image, centerCoord, pa, incl, galDist, modelType = 1):
    rX, rY = [],[]
   
    if os.path.isfile(image):

        # read in fits files
        hdu_int  = pyfits.open(image)
        intMap      = hdu_int[0].data

        #Convert x & y pixels to ra and dec
        wcs      = WCS(hdu_int[0].header, naxis=2)
        naxis    = wcs._naxis # size of image naxis[0] = x and [1] = y
        grid     = np.indices((naxis[1],naxis[0]))
        ra, dec  = wcs.wcs_pix2world(grid[1],grid[0],0)

        #deproject ra and dec to dx and dy
        radius, projang, dx, dy = deproject(center_coord=centerCoord, incl=incl, pa=pa, ra=ra, dec=dec,return_offset=True)

        #flatten data structures 
        f_int  = intMap.flatten()
        f_ra   = ra.flatten()
        f_dec  = dec.flatten()    
        f_dx   = dx.flatten()
        f_dy   = dy.flatten()

        #remove nans
        keep  = np.where(np.isfinite(f_int))
        ra    = f_ra[keep]
        dec   = f_dec[keep]
        inten = f_int[keep]
        dx    = f_dx[keep]
        dy    = f_dy[keep]
        
        for j in range(100):

            #if model is random
            if modelType == 1:
                numrowsX = len(ra)    
                numrowsY = len(dec)  

                randIntX = np.random.randint(low=0, high=numrowsX)
                randIntY = np.random.randint(low=0, high=numrowsY)
                
                rX.append(ra[randIntX])
                rY.append(dec[randIntY])

            #if model is gas density weighted
            else:
                intArr = np.clip(inten, a_min=0.0, a_max=None)
                total = sum(intArr)
                prob  = intArr/total 
                prob  = norm(prob)
                nX = len(ra)
                nY = len(dec)
                indiciesX = np.arange(nX, dtype=int)
                randIntX = np.random.choice(indiciesX, p=prob)
                indiciesY = np.arange(nY, dtype=int)
                randIntY = np.random.choice(indiciesY, p=prob)

                rX.append(ra[randIntX])
                rY.append(dec[randIntY])

            
        return(rX,rY)


