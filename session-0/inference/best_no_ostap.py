k1 = 10; n1 = 10;
k2 = 48; n2 = 50;
N=1000

import matplotlib.pyplot as plt
from scipy.stats import binom

h1    = [] ; h2    = []
bins  = [] ; prior = []
for i in range(N):
    h1.append(0.)
    h2.append(0.)
    bins.append((0.5+i)/float(N))
    prior.append(1./float(N))


Norm1 = 0.
Norm2 = 0.
for i in range(N):
    p  = (0.5+i)/float(N)
    Norm1 += prior[i]*binom.pmf(k=k1,n=n1,p=p)
    Norm2 += prior[i]*binom.pmf(k=k2,n=n2,p=p)

for i in range(N):
    p  = (0.5+i)/float(N)
    h1[i] = binom.pmf(k=k1,n=n1,p=p)*prior[i]/Norm1
    h2[i] = binom.pmf(k=k2,n=n2,p=p)*prior[i]/Norm2


plt.plot(bins,h1)
plt.plot(bins,h2,"r")

from random import random as rndm
def gen( h ):
    b = int(rndm()*len(h))
    y = max(h)*rndm()
    while y>h[b]:
        b = int(rndm()*len(h))
        y = max(h)*rndm()
    return float(b)/len(h)

G = 100000
g = 0.; w = 0.; d = 0.
for i in range(G):
    p1 = gen(h1)
    p2 = gen(h2)
    if p1>p2:
        g+=1.
    t1 = binom.rvs(n=1,p=p1)
    t2 = binom.rvs(n=1,p=p2)
    if t1 != t2:
        if t1>t2:
            w+=1.
    else:
        d+=1.

print("Probability that Option 1 win at long run   : " + str( g/G ) + "\n" )
print("Probability that Option 1 win at single run : " + str( w/(G-d) ) )
print( str(w/(G)) + "  " +str(d/G) + "  " + str((G-d-w)/G))

plt.show()
