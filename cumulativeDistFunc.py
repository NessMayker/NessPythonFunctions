def makeCDF(array, min = 0.0, max = 1.0):
	'''
	Makes a cumulative distribution function given an array.

	Parameters
	----------
	array   : array
	    array of values to make into CDF

	Returns
	-------
	x : array
	    linspace array to plot against CDF
	cdf : array
		CDF array 
	'''
	import numpy as np

	sortedArray = np.sort(array)
	cdf = sortedArray
	cdfFin = []
	#cdf = np.cumsum(sortedArray, dtype=float)
	for i in range(len(cdf)):
		if np.isnan(cdf[i]) == False:
			cdfFin.append(cdf[i])
	#     if cdf[i] < 0.0:
	#     	cdf[i] = 0.0
	num = len(cdfFin)
	y = np.linspace(min,max,num)
	return(cdfFin, y)