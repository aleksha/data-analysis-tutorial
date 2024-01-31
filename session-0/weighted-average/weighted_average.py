ll = [ (0.150,0.020), (0.250,0.090), (0.080,0.050), (0.160,0.050), (0.060,0.100),
       (0.360,0.200), (0.180,0.070), (0.190,0.090), (0.300,0.070), (0.211,0.063),
       (0.197,0.042), (0.260,0.130), (0.420,0.200), (0.273,0.090), (0.182,0.070),
       (0.140,0.040), (0.180,0.035), (0.120,0.070), (0.160,0.045), (0.200,0.064)]

from math import sqrt
from random import choice
from statistics import mean, stdev

def wav(lst):
    n=len(lst)
    sm2=0.
    xm=0.
    for v in lst:
        sm2+=1./pow(v[1],2)
    sm = sqrt(1./sm2)
    for v in lst:
        xm += (v[0]/pow(v[1],2)) / sm2
    return (xm,sm)


   
B=10000

xb = []
sb = []

for b in range(B):
    lb = []
    for i in range(len(ll)):
        lb.append( choice(ll) )
    ans = wav(lb)
    xb.append(ans[0])
    sb.append(ans[1])

print("Weighted mean")
print(wav(ll))
print("Bootstrap of mean (mean and stdev)")
print(mean(xb))
print(stdev(xb))
print("Bootstrap of sigma (mean and stdev)")
print(mean(sb))
print(stdev(sb))

for idx in range(len(ll)):
    lt = ll.copy()
    val = lt.pop(idx)
    print(str(idx) + " "+ str(val) + "  " + str(wav(lt)) + "  " + str( (val[0]-wav(lt)[0])/sqrt(pow(val[1],2)+pow(wav(lt)[1],2)) ) )
    
