import numpy
import pandas as pd
import sys
import matplotlib.pyplot as plt
from scipy.stats import beta as beta
 
if __name__ == "__main__":
	avg1 = float(sys.argv[1])
	std1 = float(sys.argv[2])
	avg2 = float(sys.argv[3])
	std2 = float(sys.argv[4])
	

	data1 = numpy.random.normal(loc=avg1,scale=std1,size=[5000])
	data2 = numpy.random.normal(loc=avg2,scale=std2,size=[5000])

	plt.hist(data1,histtype='step',color='r',normed=True)
	plt.hist(data2,histtype='step',color='b',normed=True)
	numpy.savetxt("d1.txt",data1)
	numpy.savetxt("d2.txt",data2)
	plt.savefig("distribution.png")
