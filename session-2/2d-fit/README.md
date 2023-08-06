# Why 2d fits are useful

Consider a calibration problem:
  * `x` -- initial voltage in mV times 1pF calibration capacity
  * `y` -- aplified signal Coulomb

What is amplification coefficeint? We'll use arbirtary units.
It's descrived by `x/(0.001*y)`.

## Naive approach 

```python
X = VE(mean(x),stdev(x)**2)
Y = VE(mean(y),stdev(y)**2)
R = Y/X
```

This doesn't preserve correlation.

## 2D fit approach

Fit with two dimensional gaussian.

See 'TwoDFit.ipynb':
```
Ratio_fit   : ( 46.8434 +- 0.0130 ) 
Ratio_naive : ( 46.8398 +- 0.0111 )
```

The larger uncertainties for 2d fit can be validated by bootstrapping.
See `ValidateTwoDFit.ipynb`.


**Note:** In the end of the day naive nmethod gives 10% lower uncertainnties.

**Remamber:** Mean value is en effective, but not a robust extimate.
