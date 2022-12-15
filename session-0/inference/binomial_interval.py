#-------------------------------------------------------------------------------
CL           = 0.95
n            = 50
my_linewidth = 3
#-------------------------------------------------------------------------------
alpha = 1-CL
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy.stats import f
#-------------------------------------------------------------------------------
mm = np.array(list(range(n+1)))
print( mm )
#-------------------------------------------------------------------------------
pl_L = [] ; pl_U = []
pf_L = [] ; pf_U = []
for m in mm:
    if m==0:
        pl_L.append( 0.0 )
        pf_L.append( 0.0 )
    else:
        pl_L.append( beta.ppf(    alpha/2.,   m, n-m+1 ) )
        pf_L.append( 1./( 1.+ (n-m+1) / ( m*f.ppf(alpha/2.,2*m,2*(n-m+1) ) ) ) )

    if (n-m)== 0 :
        pl_U.append( 1.0 )
        pf_U.append( 1.0 )
    else:
        pl_U.append( beta.ppf( 1.-alpha/2., m+1, n-m   ) )
        pf_U.append( 1./(1.+ (n-m)/((m+1)*f.ppf(1.-alpha/2.,2*(m+1),2*(n-m)))))
#-------------------------------------------------------------------------------
p_L = np.array(pl_L)
print(p_L)
p_U = np.array(pl_U)
print(p_U)
#-------------------------------------------------------------------------------
f_L = np.array(pf_L)
print(f_L)
f_U = np.array(pf_U)
print(f_U)
#-------------------------------------------------------------------------------
plt.plot( mm, p_L, 'k-',linewidth=my_linewidth)
plt.plot( mm, p_U, 'k-',linewidth=my_linewidth)
#plt.plot( mm, f_L, 'bo')
#plt.plot( mm, f_U, 'bo')
#-------------------------------------------------------------------------------
plt.xlabel('m')    
plt.ylabel('95% доверительный интервал для параметра p')   
plt.title('n = '+str(n))
plt.grid(True)
#-------------------------------------------------------------------------------
fig =plt.gcf()
fig.set_size_inches(9, 9)
plt.show()
#-------------------------------------------------------------------------------
