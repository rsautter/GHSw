import numpy
import pandas as pd
from math import sqrt
import sys

def wSum(bca,bcl,weightType):
	'''
	wSum - weigth sum
	----------------------------------------------
	Input:
	bca - box counting area
	bcl  -box counting length
	weightType - type of weight (1, 2, 3)

	Output:
	GHS - the weigthed sum of bca and bcl
	----------------------------------------------
	Type I - w1 = sqrt(bca)/bca
	Type II - w2 =  2 * w1
	Type III - w2 = bcl
	'''
	output = 0.0
	alpha,beta = 1.0,1.0

	if(weightType == 1):
		alpha, beta = sqrt(bca)/bca, 1
	elif(weightType == 2):
		alpha, beta = 1.0, 2.0
	elif(weightType == 3):
		alpha, beta = 1.0, bcl
	else:
		print("\nWarning,invalid weight code, using default weights.\n	")
	
	#error handling:
	if(alpha+beta<0):
		raise Exception("Invalid sum weights")	

	output = (alpha*bca+beta*bcl)/(alpha+beta)	
	#print("Weight:",alpha,beta)

	return output

def ghs(data1, data2,onlyGHS=False):
	'''
	GHS - Geometric Histogram Separation
	----------------------------------------------
	Input:
	data1,data2 - The data samples - list or numpy.ndarray
   onlyGHS - return only GHS, otherwise return BCA, BCL and GHS

	Output:
	BCA, BCL, GHS - The metrics - tuple of float64

	----------------------------------------------
	This function measures the Box Counting Area (BCA) and
	the Box Counting Linear (BCL) between data1 and data2.
	The GHS is measured as average of BCA square root and BCL.
	'''
	hist1, bins1 = numpy.histogram(data1)
	hist2, bins2 = numpy.histogram(data2)
	both = numpy.concatenate((bins1,bins2))
	# n is the number of bins (average between the number of both bins)
	n = int(len(both)/2)
	rnge = (numpy.min(both),numpy.max(both))
	hist1, bins1 = numpy.histogram(data1,bins=n,range=rnge)
	hist2, bins2 = numpy.histogram(data2,bins=n,range=rnge)
	
	hist1 = (hist1-numpy.min(hist1))/(numpy.max(hist1)-numpy.min(hist1))
	hist2 = (hist2-numpy.min(hist2))/(numpy.max(hist2)-numpy.min(hist2))

	# since both histograms have same bins, dy is the intersection:
	dx = (rnge[1]-rnge[0])/n
	dy = numpy.minimum(hist1,hist2)

	# ao is the relative area  
	ao = numpy.sum(dy)

	a_height = numpy.max(hist1)
	b_height = numpy.max(hist2)
	c_height = numpy.max(dy)

	bcl = (a_height+b_height-2.0*c_height)/(a_height+b_height)
	bca = 1.0 - (ao) / (2.0 - ao)

	if(onlyGHS):
		return (bcl+sqrt(bca))/2.0
	return bca,bcl,(bcl+sqrt(bca))/2.0

def ghsw(data1,data2,typeSum=2,onlyGHS=False):
	'''
	GHS - Geometric Histogram Separation
	----------------------------------------------
	Input:
	data1,data2 - The data samples - list or numpy.ndarray
	typeSum - Type of sum (1, 2, or 3)
   onlyGHS - return only GHS, otherwise return BCA, BCL and GHS

	Output:
	BCA, BCL, GHS - The metrics - tuple of float64

	----------------------------------------------
	This function measures the Box Counting Area (BCA) and
	the Box Counting Linear (BCL) between data1 and data2.
	The GHS is measured as average of BCA square root and BCL.
	'''
	hist1, bins1 = numpy.histogram(data1)
	hist2, bins2 = numpy.histogram(data2)
	both = numpy.concatenate((bins1,bins2))
	# n is the number of bins (average between the number of both bins)
	n = int(len(both)/2)
	rnge = (numpy.min(both),numpy.max(both))
	hist1, bins1 = numpy.histogram(data1,bins=n,range=rnge)
	hist2, bins2 = numpy.histogram(data2,bins=n,range=rnge)
	
	hist1 = (hist1-numpy.min(hist1))/(numpy.max(hist1)-numpy.min(hist1))
	hist2 = (hist2-numpy.min(hist2))/(numpy.max(hist2)-numpy.min(hist2))

	# since both histograms have same bins, dy is the intersection:
	dx = (rnge[1]-rnge[0])/n
	dy = numpy.minimum(hist1,hist2)

	# ao is the relative area  
	ao = numpy.sum(dy)

	a_height = numpy.max(hist1)
	b_height = numpy.max(hist2)
	c_height = numpy.max(dy)

	bcl = (a_height+b_height-2.0*c_height)/(a_height+b_height)
	bca = 1.0 - (ao) / (2.0 - ao)
	try:
		ghs = wSum(bca,bcl,typeSum)
	except:
		raise
	if(onlyGHS):
		return ghs
	return bca,bcl,ghs

if __name__ == "__main__":
	'''
	Call structres:
		python ghsw.py data1.csv data2.csv type parameter
		python ghsw.py data1.csv data2.csv type		
 	'''
	d1 = pd.read_csv(sys.argv[1]).dropna()
	d2 = pd.read_csv(sys.argv[2]).dropna()
	if len(sys.argv)== 5:
		bca,bcl,ghs = ghsw(d1[sys.argv[4]], d2[sys.argv[4]], int(sys.argv[3]))
	else:
		bca,bcl,ghs = ghsw(d1, d2, int(sys.argv[3]))
	print("BCA:"+str(bca)+"\nBCL:"+str(bcl)+"\nGHS:"+str(ghs))
