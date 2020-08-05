# More complex examples

```bash
wget http://adzyuba.web.cern.ch/adzyuba/d/test_file.root
```

## Composite PDFs

Models can contain composite signals and background.

A dataset for **Lambda_c->pK-pi+** contains a mis-ID background:
  * **D+->K+K-pi+** (K+ --> p miss-ID);
  * **Ds+->K+K-pi+** (K+ --> p miss-ID);
  * **Ds+->pi+K-pi+** (pi+ --> p miss-ID).
They are visible in a mass distribution, for which a proton energy is
recalculated under kaon mass hypothesis.

See `combine.py`, which fits an upper sideband.

## Convolution

Ostap provides helper class that simplify construction of fit models taking into accotun resolution functions:

'''python
pdf = ...
cnv_pdf = Convolution_pdf ( 'Cnv            ' , 
                             pdf = pdf        , 
                             resolution = ... )
'''

As resolution one can specify
  * Any resolutuon model (`RooAbsPdf`)
  * simple number s, in this case the gaussian resolution model with `sigma = s` will be used
  * Any `RooAbsReal` objetct, it will be used as sigma for gaussian resoltuion model

There are several optional flags:
  * `useFFT=True` : use Fast-Fourier-Transform or plain numerical convolution ?
  * `nbins=100000` : sampling for Fast-Fourier-Transform
  * `buffer=0.25` : buffer size for Fast-Fourier-Transform, argument for `setBufferFraction` call
  * `nsigmas=6` : window size for plain numeric convolution, the argument for `setConvolutionWindow` 


See `convolution.py`, which fits with `Voigt_pdf`, smeared and non-smeared `BreitWigner_pdf`.

## 2D and 3D fits

For 2D and 3D cases there are base classes PDF2 and PDF3 that in turn 
inhetic from PDF and gets all the nice functionality. Of course several 
new method specific for 2D and 3D-cases are added and th ebehaviosu of 
some 1D-specific methods is fixed. 

### Useful 2D-background models

2D-models useful to describe non-factorazable (**f(x,y)!=f(x)*f(y)**) background:
  * `PolyPos2D_pdf` : positive (non-negative) polynomial in 2D
  * `PolyPos2Dsym_pdf` : positive (non-negative) symmetric polynomial in 2D
  * `PSPol2D_pdf` : product of phase spaces functions, modulated with 2D polynomial
  * `PSPol2Dsym_pdf` : symmetric product of phase spaces, modulated with 2D polynomial
  * `ExpoPSPol2D_pdf` : sxponential times phase space times positive 2D-polynomial
  * `ExpoPol2D_pdf` : product of exponents times positive 2D-polynomial
  * `ExpoPol2Dsym_pdf` : symmetric version of above
  * `Spline2D_pdf` : 2D-generic positive (non-negative) spline
  * `Spline2Dsym_pdf` : 2D symmetric positive (non-negative) spline

### Useful 3D-modelss

3D-models useful to describe non-factorazable (**f(x,y,z)!=f(x)*f(y)*f(z)**) background:
  * `PolyPos3D_pdf` : positive (non-negative) polynomial in 3D
  * `PolyPos3Dsym_pdf` : positive (on-negative) symmetric polynomial in 3D
  * `PolyPos3Dmix_pdf` : positive partly symmetric (x<-->y) polynomial in 3D

