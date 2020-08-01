# Fitting tutorial

## Download file with data

```bash
wget http://adzyuba.web.cern.ch/adzyuba/d/test_file.root
```

## Browsing dataset

```python
from ostap.utils.timing import timing
from ostap.utils.memory import memory
rfile = ROOT.TFile("test_file.root","READ")
with memory():
    ds_pi = rfile["ds_pi"]
    ds    = rfile["ds_k"]
with timing():
    print( ds )
```

## Variables in the dataset

  1.  `pt` - transverce momentum of charm baryon candidate
  2.  `y` - rapidity pf charm baryon
  3.  `ct` - **Lifetime*SpeadOfLight, mm**
  4.  `ch` - quality of a decay chain fit
  5.  `id` - assumed ID (negative for antyparticles)
  6.  `ipc` - **Chi2IP** how far is an impact parameter of a reconstructed baryon from a related primary vertex (pp interaction point)
  7.  `p_p` - proton full momentum
  8.  `eta_p` - proton pseudorapidity
  9.  `phi_p` - proton azimuthal angle
  10. `p_k` - kaon (K-) full momentum
  11. `eta_k` - kaon pseudorapidity
  12. `p_3` - pion (for **ds_pi**) or K+ (**ds**) full momentum
  13. `eta_3` - its pseudorapidity
  14. `ntrk` - number of reconstructed so-called long track in the event
  15. `NNp` - var for proton to be proton (neural network decision)
  16. `im` - mass of **pKh** candidate
  17. `im_kp` - mass with **proton --> kaon** hypothesis
  18. `im_pi` - mass with **proton --> pion** hypothesis
  19. `im_hp` - mass with **K+ --> pi+**
  20. `m12` - two-body mass for products (1 and 2)
  21. `m13` - 1 and 3
  22. `m23` - 2 and 3
  23. `NNk` - var kaon to be kaon (neural network decision)
  24. `NN3` - K+ to be K+ (or pi+ to be pi+)
  25. `lgi` - **log10(Chi2IP)**

## RooFit objects

## Working with dataset

Here we at first reduce a dataset with cut and when select a small 1% 
random subsample of the reduced one..
```python
im = ROOT.RooRealVar ('im', 'im',  2.240 , 2.330 )
sds = 0.01*ds_pi.reduce( ROOT.RooArgSet(im),"im<2.4" )
sds
sds.draw("im")
```

## Simple fitting

Lets create simple composite (signal + background) model 
and male maximum liklihood unbinned fit.
```python
import ostap.fitting.models as Models
sig_ga = Models.Gauss_pdf( 'sig_ga', xvar=im, mean=(2.2875 ,  2.286 , 2.289), sigma=(0.0045 ,  0.003 , 0.010 ) )
bkg0 = Models.Bkg_pdf ( 'bkg0' , xvar = im , power = 0 )
model= Models.Fit1D   ( signal = sig_ga , background = bkg0 )
r,w = model.fitTo(sds, silent=True, draw=True)
print(r)
```

If we'd like to know the fignal fraction without taking into account overall 
event number fluctuation, then we can use non-extended fit. Uncertainties will
change a bit.
```python
model_ext= Models.Fit1D   ( signal = sig_ga , background = bkg0 , extended = False)
r,w = model_ext.fitTo(sds, silent=True, draw=True)
print(r)
```

Fitting of histogram is easy. Note, that it's a MLE.
```python
histo = ROOT.TH1F("histo","histo",45,2.24,2.33)
for e in sds:
    histo.Fill( e.im )
histo.Draw()
r,w = model.fitHisto(histo, draw=True)
```

To use chi-squre fit we have to make binned dataset. `minNll` is
representing chi2 now. 
```python
dh = ( ds.reduce( ROOT.RooArgSet( im ) , "im>0" ) ).binnedClone()
r,w = model.chi2fitTo( dh, draw=True)
r.minNll()
```

## More sophisicated signal shapes.

Some pretty decoration is easy to make. See `Functions.py`
as an example. 

If one fit full **ds_pi** (Lambda_c-->p+K-pi+ case), when he/she will spot
that fit with simple Gaussian doesn't work sufficiently well.
Ostap provides a lot of different signal shapes. Try
```bash
ostap -b fitter_apolo.py
ostap -b fitter_bukin.py
```
