# GHSw - Geometric Histogram Separation

This technique geometrical distance between two empirical histograms, this algorithm is inspired on box-counting.

## Install

    pip install git+https://github.com/rsautter/GHSw

Colab:

    !pip install git+https://github.com/rsautter/GHSw
    
## Usage

    ghsw(data1,data2,typeSum=2,onlyGHS=False)
    
  * data1, data2 - set of points 
  * typeSum:
    * 1 - w1 = sqrt(BCA)/BCA
	* 2 - w2 =  2 * w1
	* 3 - w2 = BCL
  * onlyGHS - return BCA and BCL?
  
## Examples
  Some study cases are presented in notebook folder.
  
## Log
Oct. 11, 2020 - Changed name, added some examples\
Jul. 08, 2019 - Kullback-Leibler distance and Hellinger distance are now available for raw data\
&emsp;&emsp; &emsp; &emsp; &emsp; - Added a plot script\
Jul. 04, 2019 - Fewer modifications, related to the number of bins
