Introduction tutorial
=====================

Precursors:
 * _Ostap_ software stack installed

Download the project, go to **stat** directory, start _Ostap_:
```bash
git clone https://github.com/aleksha/PNPI-PhD.git
cd PNPI-PhD/stat/
ostap
```

Optionally one can specify the list of python files to be executed 
before appearance of the interactive command prompt: 
```bash
ostap a.py b.py
```
Note, if there will be a crash during executing of the scripts, when variabels will
not be avalabe aftewards. In case of success they stand.

The list of optional arguments can include also root-files, in this case the files will 
be opened and their handlers will be available via local list **root_files**
```bash
ostap a.py b.py c.py d.py  file1.root file2.root e.py file3.root 
```

The script automatically opens **TCanvas** window with a little bit modified recommended LHCb style.
An option **--no-canvas** prevent of doing this.

To run in a batch regime (execute scripts and exit) use **-b, --batch** option.

List of other options can be found using **-h, --help** options.

To exit _Ostap_ use **exit()**, or **quit()**, or **Ctrl+D** followed by **Enter**.

First steps
-----------

The standard call launch IPython and create default canvas (can be called as __canvas__).
The ROOT decoration is preloaded.
For exaple next commands create ROOT hystogram, fill it with 2 and 1.9 (it returns bin number;
remember that in ROOT bin numbering starts from 1), draw, and save into file **temp.png**
```ipython
In [1]: h = ROOT.TH1F("h","h",10,0,10)
In [2]: h.Fill(2)
Out[2]: 3
In [3]: h.Fill(1.9)
Out[3]: 2
In [5]: h.Draw()
In [6]: canvas >> "temp.png"
Out[6]: <ROOT.TCanvas object ("glCanvas") at 0x561613c75f20>
```
To see, which ROOT object are available type:
```ipython
In [7]: dir(ROOT)
```
To see, which methods are available for particular object see help (type **q** to exit help).
For example:
```ipython
In [8]: help(ROOT.TH1F)
```
**Note: that there a lot of methods in addition to the standard ROOT one!**

Value with error object (VE)
----------------------------

One of the basic object of _Ostap_ framework is Value with error (_VE_).
Uncertainty assumed to be gaussian.
```ipython
In [9]: VE
Out[9]: ROOT.Ostap.Math.ValueWithError
In [10]: help(VE)
In [11]: a = VE(1,1)
In [12]: b = VE(10,1)
In [13]: c = a+b
In [14]: print(c)
( 11 +- 1.41421 )
In [15]: c
Out[15]: ( 11 +- 1.41421 )

```
Note that **second parameter for initialisation is variance**,
while **standard deviation is used in the output!!**

```ipython
In [16]: d = VE(1,2)
In [17]: d
Out[17]: ( 1 +- 1.41421 )
In [18]: d.value()
Out[18]: 1.0
In [19]: d.error()
Out[19]: 1.4142135623730951
```

Basic operation with _VE_ could be found in basic _Ostap_ example:
```bash
ostap -b $OSTAPDIR/../examples/math/math_ex001_functions.py 
```

Quite inportant, but not obviours features (methods):
-----------------------------------------------------
Background-over-signal ratio B/S estimate from the equation:

      error(S) = 1/sqrt(S) * sqrt ( 1 + B/S).

Valid for Poisson numbers, for which uncertainty is sqrt(S).
All above is due to the background.

```ipython
In [1]: help(VE)
In [2]: n = VE(10000,100**2)
In [3]: n.b2s()
Out[3]: ( 1 +- 0 )
In [4]: m = VE(10000,150**2)
In [5]: m.b2s()
Out[5]: ( 1.25 +- 0.03375 )
```

Calculate the ``effective purity'' ratio using the identity (function
is not working so far):

      p = S/(S+B) = 1/( 1 + B/S ), 
 

Formating (rounding) according to PDG:
 - http://pdg.lbl.gov/2010/reviews/rpp2010-rev-rpp-intro.pdf
 - section 5.3 of doi:10.1088/0954-3899/33/1/001
        
 Quote:
      The basic rule states that if the three highest order digits of the error
      lie between 100 and 354, we round to two significant digits. If they lie between
      355 and 949, we round to one significant digit. Finally,
      if they lie between 950 and 999, we round up to 1000 and keep two significant digits.
      In all cases, the central value is given with a precision that matches that of the error.

```ipython
>>> ve  = VE( ...
>>> vr  = ve.pdg()
>>> print ' Rounded value with error is  %s ' % vr
```

Relative uncertainry can be calculated using **prec()** function.
```ipython
>>> v = VE(...
>>> p = v.prec()
```
