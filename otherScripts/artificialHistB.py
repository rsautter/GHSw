import numpy
import pandas as pd
import sys
import matplotlib.pyplot as plt
from scipy.stats import beta as beta
 
if __name__ == "__main__":
	a1 = float(sys.argv[1])
	b1 = float(sys.argv[2])
	a2 = float(sys.argv[3])
	b2 = float(sys.argv[4])
	

	data1 = numpy.random.beta(a=a1,b=b1,size=[5000])
	data2 = numpy.random.beta(a=a2,b=b2,size=[5000])
	maximum = numpy.concatenate((data1,data2)).max()
	print("Max",maximum)

	print("Moments 1 - ", beta.stats(a1, b1, moments='mvsk'))
	numpy.savetxt("Moments1.txt",beta.stats(a1, b1, moments='mvsk'),fmt="%.3f")
	print("Moments 2 - ", beta.stats(a2, b2, moments='mvsk'))
	numpy.savetxt("Moments2.txt",beta.stats(a2, b2, moments='mvsk'),fmt="%.3f")
	plt.hist(data1,histtype='step',color='r',normed=True)
	plt.hist(data2,histtype='step',color='b',normed=True)
	numpy.savetxt("d1.txt",data1)
	numpy.savetxt("d2.txt",data2)
	plt.savefig("distribution.png")
