def findStats(fracArray, valsArray):
	'''    
	Returns the 16,50,84th percentiles.

	Parameters
	----------
	lst : array of floats
	    array of fractional values of sample
	vals : array of floats
		array we want to retreive number from at found index

	Returns
	-------
	stats : array of floats
		array of floats that has each of the 16,50,84th percentiles.   
	'''

	import numpy as np

	import sys
	#sys.path.append('/Users/nessmayker/Desktop/NessPythonFunctions')
	sys.path.append('/home/mayker.1/Desktop/NessPythonFunctions')
	from findAtIndex import atIndex

	K = [0.16,0.5,0.84]
	stats = []

	for i in range(len(K)):
		val = atIndex(fracArray,K[i],valsArray)
		rndVal = round(val, 2)
		#rndVal = val
		stats.append(rndVal)

	return(stats)
