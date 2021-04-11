# Jackknife resampling

In statistics, the jackknife is a resampling technique especially useful for variance and bias estimation. 
The jackknife pre-dates other common resampling methods such as the bootstrap. 
The jackknife estimator of a parameter is found by systematically leaving out each observation from a dataset and 
calculating the estimate and then finding the average of these calculations. 

The jackknife is a linear approximation of the bootstrap.[1] 

## Example

The `jack.py` use all subsamplles of the given length to calculate linear model.
Central 90% bands are drawn.

### About datasample
  
Among all S&P500 companies some regulary pay devidents. More ofer, they increase a percentage each year.
This allows to use their stocks in an obligation mode. Here is an attempt to predict future annual payment.

See example in `APD.png`.

Lines are:
  * blue dashed - linear model
  * red dashed - `ROB=0.7` fit
  * green dashed - exponential model
  * solid lines - a kind of interval estimation
