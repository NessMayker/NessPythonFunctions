def findStats(fracArray, valsArray):
	'''    
	Returns the 5,16,50,84,95th percentiles.

	Parameters
	----------
	lst : array of floats
	    array of fractional values of sample
	vals : array of floats
		array we want to retreive number from at found index

	Returns
	-------
	stats : array of floats
		array of floats that has each of the 5,16,50,84,95th percentiles.   
	'''

	import numpy as np

	import sys
	#sys.path.append('/Users/nessmayker/Desktop/NessPythonFunctions')
	sys.path.append('/home/mayker.1/Desktop/NessPythonFunctions')
	from findAtIndex import atIndex

	K = [0.05,0.16,0.5,0.84,0.95]
	stats = []

	for i in range(len(K)):
		val = atIndex(fracArray,K[i],valsArray)
		rndVal = round(val, 2)
		stats.append(rndVal)

	return(stats)
