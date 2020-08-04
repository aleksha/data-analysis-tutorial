# Signal distribution for other variables

## Sideband subtruction

This method exploit an aproach that shape of a bagrouund events under a signal peak
is the same as outside a peak. One can subtrack the distribution from the distribution
for the events in the preak region.

Usually **+/-2sigma** around a peak position is used for the signal region and 
**(-7,-5)sigma** and **(5,7)-sigma*** intervals are used for subtruction.

**Important**:
  - Take care about proper normalisation;
  - Background distribution should be quite flat.

## Fit-in-bin

One can split a data into subsamples on a control variable and perform a MLE in each bin.
This method is quite CPU consuming.

## sPlot techinqie

Here, idea is quite simple. Each event in MLE fitting has certain contribution to the
signal and background part of likelihood function. One can calculate a statistical
weight for each event with rearkble properties, which allow to use them to detrmine
distribution of a control variable.

**Important:** control variables have to be independent on a discriminating variable(s)!

Useful links:
 * [Official paper](https://www.sciencedirect.com/science/article/pii/S0168900205018024?via%3Dihub)
 * [Arxiv version](https://arxiv.org/abs/physics/0402083)
 * [Alex Rogozhnikov's explanation](http://arogozhnikov.github.io/2015/10/07/splot.html)

Using __sPlot__ is rather trivial in Ostap:
```python
dataset = ...
model   = Fit1D ( signal = ... , backgrund = ... ) 
model.fitTo ( dataset )
print datatset   
model.sPlot ( dataset )  ## <--- HERE 
print datatset           ## <--- note appearence of new variables
```
