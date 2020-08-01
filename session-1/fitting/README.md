# Fitting tutorial

## Download file with data

Here is some test dataset of the unknown source.
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

Please, note very useful `timing()` and  `memory()` utils of Ostap.

## Variables in the dataset

  * **ds_pi** - charmed baryons into p+ K- pi+ final state
  * **ds_k**  - charmed baryons into p+ K- K+ 

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

As Ostap relays on **RooFit** for fits, an understanging of the underlying objects
are necessary. Here are some of them:
  * `RooAbsArg` is the common abstract base class for objects that represent 
    a value (of arbitrary type) and "shape" that in general depends on (is a client of) 
    other `RooAbsArg` subclasses.
  * `RooRealVar` represents a variable that can be changed from the outside. 
    For example by the user or a fitter.
  * `RooArgList` is a container object that can hold multiple `RooAbsArg` objects. 
    The container has list semantics which means that:
    - Contained objects are ordered, The iterator follows the object insertion order.
    - Objects can be retrieved by name and index
    - Multiple objects with the same name are allowed
  * `RooArgSet` is a container object that can hold multiple `RooAbsArg` objects. 
    The container has set semantics which means that:
     - Every object it contains must have a unique name returned by GetName().
     - Contained objects are not ordered, although the set can be traversed using an iterator returned by createIterator(). The iterator does not necessarily follow the object insertion order.
     - Objects can be retrieved by name only, and not by index.
  * `RooDataSet` is a container class to hold unbinned data. The binned equivalent is `RooDataHist`. 
    In `RooDataSet`, each data point in N-dimensional space is represented by a `RooArgSet` of `RooRealVar`, 
    Since `RooDataSet` saves every event, it allows for fits with highest precision. With a large amount 
    of data, however, it could be beneficial to represent them in binned form, i.e., `RooDataHist`. 
    Binning the data will incur a loss of information, though. `RooDataHist` on the other hand may suffer 
    from the curse of dimensionality if a high-dimensional problem with a lot of bins on each axis is tackled. 
  * `RooDataHist` is a container class to hold N-dimensional binned data. Each bin's central coordinates 
    in N-dimensional space are represented by a `RooArgSet` containing `RooRealVar`,
  * `RooFitResult` is a container class to hold the input and output of a PDF fit to a dataset. It contains:
    - Values of all constant parameters
    - Initial and final values of floating parameters with error
    - Correlation matrix and global correlation coefficients
    - NLL and EDM at mininum


See more in a [RooFit class reference documentation](https://root.cern.ch/doc/master/group__Roofitcore.html).

### `RooArgSet` and `RooArgList`

All these classes have got set of additional python-like methods for iteration, extension, addition, 
element access checking the content etc... Also several methods to provide more coherent interfaces 
(e.g. add vs Add) are added. 

### `RooRealVar`

Few simple operations are added to simplify the calculations with `RooRealVar` objects:
```python
x = ROOT.RooRealVar( ... )
x + 10 
x - 10 
x * 10 
x / 10 
10 + x 
10 - x 
10 * x 
10 / x
x += 2 
x -= 2 
x *= 2 
x /= 2 
x ** 3
```

### `RooAbsData` and `RooDataSet`

These methods also have got the extended interface with many useful methods and operators, 
like e.g. concatenation of datasets a+b and merging them a*c. `RooDataSet` class also has go many methods, 
that are similar to those of `ROOT.TTree`, in particular project and draw:

```python
dataset = ... 
dataset.draw('mass','pt>1')  
histo   = ...
dataset.project ( histo , 'mass', 'pt>1' )
```

Many other methonds like `statVar`, `sumVar` , `statCov` , `vminmax` are also the same 
as for `ROOT.TTree`, see above.

```python
s1    = dataset.statVar ('eff') 
s2    = dataset.sumVar  ('eff') 
r     = dataset.statCov ('eff','pt') 
mn,mx = dataset.vminmax ('eff')
```

### `RooFitResult`

The class `RooFitResult` get many decorations that allow to access fit results
```python
result = ...
par1 = result.params()  ## get all floating parameters 
par2 = result.params( float_only = False ) ## all parameters 
a,v  = result.param ( 'a' )      ## par by name 
a,v  = result.param (  a  )      ## par by RooFit object itself 
p    = result.a                  ## par as attribute 
for par in result :
   print (par)                ## iteration 
for name,par in result.iteritems() : print par ## iteration
   print ( result.cov  ( 'a' , 'b'  ) ) ## get the covariance submatrix  
   print ( result.corr ( 'a' , 'b'  ) ) ## get the correlation coefficient
```

Also the simple math with fiting parameters is supported
```python
result = ...
s = result.sum       ('S','B' ) ## S+B
d = result.divide    ('S','B' ) ## S/B
s = result.subtract  ('B','B1') ## B-B1
m = result.multiply  ('A','B' ) ## A*B 
f = result.fraction  ('S','B' ) ## S/(S+B)
```

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

## More complex PDFs

Some pretty decoration is easy to make. See `Functions.py`
as an example. 

If one fit full **ds_pi** (Lambda_c-->p+K-pi+ case), when he/she will spot
that fit with simple Gaussian doesn't work sufficiently well.
Ostap provides a lot of different signal shapes. Try
```bash
ostap -b fitter_apolo.py
ostap -b fitter_bukin.py
```
