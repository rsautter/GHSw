import bootstrapped.bootstrap as bs
import bootstrapped.stats_functions as bs_stats
import numpy
import ghsw
import distanceMetrics
import matplotlib.pyplot as plt

def plotConfidenceInterval(x,avg, minValues,maxValues,color):
    plt.plot(x,avg,color=color)
    plt.fill_between(x,avg,minValues,maxValues,facecolor=color,alpha=0.2)    

def getBootstrapGHS(beta1, beta2, density, bootstrapSampleSize, weightType):
    ghsResultList = []  
    for i in range(bootstrapSampleSize):
        bca,bcl,ghs = ghsw.ghsw(beta1.getDistribution(density), beta2.getDistribution(density), weightType,onlyGHS=False)
        ghsResultList.append(ghs)
    result = bs.bootstrap(numpy.array(ghsResultList), stat_func=bs_stats.mean)
    return result

def getBootstrapHellKl(beta1, beta2, density, bootstrapSampleSize):
    resultListKL = []
    resultListHell = []  
    for i in range(bootstrapSampleSize):
        resultListHell.append(distanceMetrics.hellinger1(beta1.getDistribution(density), beta2.getDistribution(density)))
        resultListKL.append(distanceMetrics.dkl(beta1.getDistribution(density), beta2.getDistribution(density)))
    rBKL = bs.bootstrap(numpy.array(resultListKL), stat_func=bs_stats.mean)
    rBHell = bs.bootstrap(numpy.array(resultListHell), stat_func=bs_stats.mean)
    return rBKL,rBHell
    

class betaDistribution:

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def getDistribution(self,size):
        data = numpy.random.beta(a=self.a,b=self.b,size=[size])
        data += self.c
        return data
    

'''

Bootstrap Test
------

Given the parameters from two beta distributions (d1 and d2),
performs the distribution sampling with n samples, and evaluates the botstrap for this sample 

'''
if __name__ == "__main__":
    # Distribution Properties
    
    # best distance 
    b1 = betaDistribution(0.6, 3.0, 0.0)
    b2 = betaDistribution(3.0, 0.6, 0.0)


    # Test arguments
    bootstrapSampleSize = 3000
    weightType = 3

    '''
    -------------------------
    Testing few cases:
    -------------------------
    '''
    resultLst = []
    empDistributionDensity = [100,400,700,1000] 
    for w in range(1,4):
        for density in empDistributionDensity:
            result = getBootstrapGHS(b1, b2, density, bootstrapSampleSize, w)
            resultLst.append(["GHS-w"+str(w),density,result.lower_bound,result.value,result.upper_bound])
    for density in empDistributionDensity:
        kl,hell = getBootstrapHellKl(b1, b2, density, bootstrapSampleSize)
        resultLst.append(["KL",density,kl.lower_bound,kl.value,kl.upper_bound])
        resultLst.append(["Hellinger",density,hell.lower_bound,hell.value,hell.upper_bound])
    numpy.savetxt("bootstrap_GHS_result.csv",resultLst,delimiter=",",header="Metric,Distribution Density,Min GHS,Avg GHS, Max GHS",fmt="%s")
        
    
    '''
    -------------------------
    Testing many cases:
    -------------------------
    '''
    #minSamples,maxSample,dSample = 150,1500,10
    # results to store
    #avgGHS,minGHS,maxGHS=[],[],[]
    #densities = []

    #for distDensity in range(minSamples,maxSample,dSample):
    #    result = getBootstrapGHS(b1,b2,distDensity,bootstrapSampleSize,weightType)
    #    densities.append(distDensity)
    #    avgGHS.append(result.value)
    #    minGHS.append(result.lower_bound)
    #    maxGHS.append(result.upper_bound)

    #plotConfidenceInterval(densities,avgGHS, minGHS,maxGHS,'blue')
    #result = numpy.array([densities,minGHS,avgGHS,maxGHS]).T
    #plt.title("")
    #plt.ylabel("Average")
    #plt.xlabel("Distribution Density")
    #plt.xlim((140,1510))
    #plt.show()
    #numpy.savetxt("bootstrap_result.csv",result,delimiter=",",header="density,min,avg,max")

