#-------------------------------------------------------------------------------
n_list       = [ ]
my_linewidth = 3
N_points     = 50
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import poisson
from math import log2
#-------------------------------------------------------------------------------
for ii in range(N_points){
    n_list.append(1.+2.ii)
nn = np.array(n_list)
#-------------------------------------------------------------------------------
entropy_list = []
for n in n_list:
    entropy = []
    for p in pp:
        e = 0.0
        for i in range(n+1):
            #print(str(i)+" "+str(n)+" "+str(p)+" "+str(binom.pmf(i,n,p)))
            if binom.pmf(i,n)>0: 
                e += ( -binom.pmf(i,n,p)*log2( binom.pmf(i,n,p) ) )
        entropy.append(e)
    entropy_list.append( np.array( entropy ) )
#-------------------------------------------------------------------------------
plt.plot( pp, entropy_list[0], 'k-',linewidth=my_linewidth)
plt.plot( pp, entropy_list[1], 'k--',linewidth=my_linewidth)
plt.plot( pp, entropy_list[2], 'k-.',linewidth=my_linewidth)
#plt.plot( mm, p_U, 'k-',linewidth=my_linewidth)
#-------------------------------------------------------------------------------
plt.xlabel('p')    
plt.ylabel('Энтропия')   
#plt.title('n = '+str(n))
plt.grid(True)
#-------------------------------------------------------------------------------
plt.show()
#plt.savefig("ci.png")
#-------------------------------------------------------------------------------
