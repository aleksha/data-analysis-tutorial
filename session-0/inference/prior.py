k1 = 59; n1 = 60;
k2 = 59; n2 = 60;

lin = True

N=1000

bins = []
for i in range(N+1):
    bins.append(1.*i/float(N))

from ostap.histos.histos import h1_axis

from scipy.stats import binom

h1 = h1_axis( bins )
h2 = h1_axis( bins )
prior1 = h1_axis( bins )
prior2 = h1_axis( bins )
for i in range(N):
    prior1[i+1]=1./float(N)
    if lin:
        prior2[i+1]=2.*(0.5+i)/float(N)
    else:
        if (0.5+i)/float(N) < 0.9:
            prior2[i+1]=0
        else:
            prior2[i+1]=10./float(N)
h2.red()

Norm1 = 0.
Norm2 = 0.
for i in range(N):
    p  = (0.5+i)/float(N)
    Norm1 += prior1[i+1]*binom.pmf(k=k1,n=n1,p=p)
    Norm2 += prior2[i+1]*binom.pmf(k=k2,n=n2,p=p)

for i in range(N):
    p  = (0.5+i)/float(N)
    h1[i+1] = binom.pmf(k=k1,n=n1,p=p)*prior1[i+1]/Norm1
    h2[i+1] = binom.pmf(k=k2,n=n2,p=p)*prior2[i+1]/Norm2


h2.Draw("hist")
h1.Draw("same hist")
print("Posterior mean vs. Laplas rule of success")
print("Option 1")
print(h1.mean())
print( (k1+1)/(n1+2) )
print("Option 2")
print(h2.mean())
print( (k2+1)/(n2+2) )

