import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import norm
import pandas as pd
import sys


#python version (discrete suppervised):
#source:
def hellinger1(p, q):
	return norm(np.sqrt(p) - np.sqrt(q)) /  np.sqrt(2)

def hellinger(a,b):
	p, _ = np.histogram(a)
	q, _ = np.histogram(b)
	p, q = p/np.sum(p), q/np.sum(q)
	return hellinger1(p,q)

def kl(d1, d2):
	dd1,dd2 = d1/sum(d1),d2/sum(d2)
	where = (d1>0.0001) & (d2>0.0001) 
	if not (True in where):
		return np.inf
	return sum(dd1[where]*np.log(dd1[where]/dd2[where]))

def dkl1(d1, d2):
	dd1,dd2 = d1/sum(d1),d2/sum(d2)
	where = (d1>0.0001) & (d2>0.0001) 
	if not (True in where):
		return np.inf
	return sum((dd1[where]-dd2[where])*np.log(dd1[where]/dd2[where]))

def dkl(a,b):
	p, _ = np.histogram(a)
	q, _ = np.histogram(b)
	p, q = p/np.sum(p), q/np.sum(q)
	return dkl1(p,q)

if __name__ == "__main__":
	d1, d2 = pd.read_csv(sys.argv[1],header=None),pd.read_csv(sys.argv[2],header=None)
	p0,bins = np.histogram(pd.concat([d1,d2]))
	p1,bins1 = np.histogram(d1,bins=bins)
	p2,bins2 = np.histogram(d2,bins=bins)
	p1 = np.array(p1,dtype=np.float32)/sum(p1)
	p2 = np.array(p2,dtype=np.float32)/sum(p2)
	output = [[kl(p1,p2),kl(p2,p1),dkl(p1,p2),hellinger1(p2,p1)]]
	print("KL1:"+str(kl(p1,p2)))
	print("KL2:"+str(kl(p2,p1)))
	print("DKL:"+str(dkl(p1,p2)))
	print("Hell:"+str(hellinger1(p2,p1)))
	np.savetxt("distances.txt",output,header="kl1,kl2,dkl,hell",delimiter=",",comments='')
	
