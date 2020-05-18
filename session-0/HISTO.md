ROOT histograms and functions in Ostap
======================================

Standard _ROOT_ histograms and functions (_TH1_  and _TF1_ class) have 
a lot of useful decoration. One can use original methods as well. See:
 - https://root.cern.ch/doc/master/classTH1.html
 - https://root.cern.ch/doc/master/classTF1.html
 - https://lhcb.github.io/ostap-tutorials/getting-started/Histos.html
 - https://lhcb.github.io/ostap-tutorials/more-on-histograms/hparams.html

```ipython
In [1]: help(ROOT.TH1F)
In [2]: help(ROOT.TF1)
In [3]: h1 = ROOT.TH1F("h","Histo;x;y",10,0,1)
In [4]: h1.GetXaxis().GetTitle()
Out[4]: 'x'
```

