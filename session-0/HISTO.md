ROOT histograms and functions in Ostap
======================================

Standard _ROOT_ histograms and functions (_TH1_  and _TF1_ class) have 
a lot of useful decoration. One can use original methods as well. See:
 - https://root.cern.ch/doc/master/classTH1.html
 - https://root.cern.ch/doc/master/classTF1.html
 - https://lhcb.github.io/ostap-tutorials/getting-started/Histos.html
 - https://lhcb.github.io/ostap-tutorials/more-on-histograms/hparams.html

## Create histogram

Using ROOR constructor
```ipython
In [1]: help(ROOT.TH1F)
In [2]: help(ROOT.TF1)
In [3]: h1 = ROOT.TH1F("h","Histo;x;y",10,0,1)
In [4]: h1.GetXaxis().GetTitle()
Out[4]: 'x'
In [5]: help(ROOT.TF2)
```

By bin adges:
```python
from   ostap.math.ve import VE
from ostap.histos.histos import h1_axis, h2_axes 
y_bins  = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
pt_bins = [1, 2, 3, 4, 5, 6, 7, 8]
h1d = h1_axis(pt_bins)
h2d = h2_axis(y_bins,pt_bins)
```

## Interation over a histogramm

Remember that in ROOT bin numbering starts from one!
It's due too the underflow and overflow bins.

```python
for i in range(10):
    h1d.Fill(2.5)
    h2d.Fill(2.75,2.5)
a = h1d[2]
print(a)
b = h1d[(2,2)]
print(b)
h1d[3] = VE(6,6**2)
h1d.red()
h1d.Draw("e1")
```

## Manipulation with histograms

```python
# multiply by function 
h1 *= lambda x : 1+0.25*((x-10)/10)**2

# add with constant
 h2 = 1 + h1

# sum two histograms 
h3 = h1 + h2

# division 
h4 = h1 / h3

## division 
h4 = 1 / h4

# power
h5 = h4**4

def fun1(x) : return x*x
# sum with function 
h6 = fun1 + h4

ff = ROOT.TF1('f1','x+5',-10,10) 
# divide by the function 
h7 = h6 / ff 

# historam as function
print ('h1(3.1415) :' + str( h1(3.1415                ) ) )
print ('h1(3.1415) :' + str( h1(3.1415, interpolate=0 ) ) )
print ('h1(3.1415) :' + str( h1(3.1415, interpolate=1 ) ) )
print ('h1(3.1415) :' + str( h1(3.1415, interpolate=2 ) ) )
print ('h1(3.1415) :' + str( h1(3.1415, interpolate=3 ) ) )

 hh = ROOT.TH1D('hh','',60,0,30)
 for i in hh : hh[i] = 5+(i/2)%3
 # convert to TF1
 f0 = hh.asTF1 ( interpolate=0 ) ## no interpolation 
 f1 = hh.asTF1 ( interpolate=1 )
 f2 = hh.asTF1 ( interpolate=2 )
 f3 = hh.asTF1 ( interpolate=3 )
 
 f0.SetLineColor(3)
 f1.SetLineColor(2)
 f2.SetLineColor(4)
 f3.SetLineColor(8)
 
 ## absolute value 
 h1a = abs ( h1 )
 
 ## power 
 h1s = h1**2.2 
 
 ## exp and any other functions 
 h1s = exp(h1)
 
 ## running sum:
 h = h1.sumv()
 h = h1.sumv( increasing = True  ) ## default 
 h = h1.sumv( increasing = False )
 
 ## various stats
 print( 'mean             : ' + str( h1.mean     ()  ) )
 print( 'rms              : ' + str( h1.rms      ()  ) )
 print( 'skewness         : ' + str( h1.skewness ()  ) )
 print( 'kurtosis         : ' + str( h1.kurtosis ()  ) )
 print( 'moment(6)        : ' + str( h1.moment   (6) ) )
 print( 'centralMoment(8) : ' + str( h1.centralMoment (8) ) )
 print( 'stat             : ' + str( h1.stat     ()  ) )
 

## sample histogram
h = h1.sample()

## dump
print ( ' dump:' + str( h1.dump(60,20) ))

## smear the histogram (convolute with gaussian)
h = h1.smear ( 2 )

## parameterizations
pp = h1.positive  (5)  ## as a positive polynomial of 5th order (Bernstein)
p  = h1.polynomial(4)  ## as 4th order polynomial
l  = h1.legendre  (3)  ## as 3rd order Legendre polynomial
t  = h1.chebyshev (4)  ## as 4th order Tchebyshev polynomial
f  = h1.fourier   (8)  ## as 8th order Fourier sum 
c  = h1.cosine    (8)  ## as 8th order Fourier cosine  sum 

## efficiencies
fun = ROOT.TF1 ('ff','1-(x-1)**2',0,1)
import random 
hT  = ROOT.TH1F('hT','',20,0,1)  ## total or original'
hA  = hT.clone()                 ## acepted
hR  = hT.clone()                 ## rejected 
for i in range(10000) :
    v = fun.GetRandom()
    hT.Fill ( v )
    if random.uniform(0,1) < 0.3333 :  hA.Fill ( v )
    else                            :  hR.Fill ( v )  

## naive efficiency as accpeted/total
eff1 = hA / hT
 
## "Zech" efficiency 
eff3 = hA % hT 

## "safe" recipe:  e = hA / ( hA + hR ) = 1/(1+hR/hA) 
eff4 = 1/(1+hR/hA)
```
