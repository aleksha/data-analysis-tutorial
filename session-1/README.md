# Signal extraction

## Content

  * Fitting a signal:
    - Chi-square and maximum likelihood fits.
    - Extended and non-extended fits.
  * Uncertainty validation using Toy-Monte-Carlo.
  * Distributions for a signal and a background components:
    - Sideband subtruction;
    - Fit-in-bin technique;
    - __sPlot__ unfolding techinque.

## A typical task

Let's assume that we have a detector, which (somehow) detect a charged product of a decay of a particle (**X**),
which appears in some collision experiment. There is a certain probability that **N** events appear during
data taking:

**N = σ / (L B ε)**,

where enumerator contains [cross-section](https://en.wikipedia.org/wiki/Cross_section_(physics)) 
of the X production (**σ**), and the denominator contains: integrated 
[luminosity](https://en.wikipedia.org/wiki/Luminosity_(scattering_theory)) 
(**L**), probability of the X to decay into a selected final state (**B**) and overall 
efficiency of the detection (**ε**). Note, that **N** is a Poisson-distributed random value.

In practice, there are background events in addition to signal ones. 
The task is to make an estimation (**S**) of **N**. 
Different estimators (means different rules for calculating an estimate 
of a given quantity based on observed data) are possible.
The attractiveness of different estimators can be judged by looking at 
their properties, such as:
  * [unbiasedness](https://en.wikipedia.org/wiki/Unbiasedness)
  * [mean square error](https://en.wikipedia.org/wiki/Mean_square_error)
  * [consistency](https://en.wikipedia.org/wiki/Consistent_estimator)
  * [asymptotic distribution](https://en.wikipedia.org/wiki/Asymptotic_distribution)
  * [efficiency](https://en.wikipedia.org/wiki/Efficiency_(statistics))
  * [robustness](https://en.wikipedia.org/wiki/Robust_statistics)
  * etc

One of the problems is that **S** is not the only parameter. Other so-called 
[nuisance parameters](https://en.wikipedia.org/wiki/Nuisance_parameter) 
(peak position, peak width, background model parameters) should be estimated simultaniously 
with **S**.

There are a lot of different estimators and esimator types:
  * Maximum likelihood estimators (MLE)
  * Least squares
  * Bayes estimators
  * Method of moments estimators
  * Cramér–Rao bound
  * Minimum mean squared error (MMSE), also known as Bayes least squared error (BLSE)
  * Maximum a posteriori (MAP)
  * Minimum variance unbiased estimator (MVUE)
  * Nonlinear system identification
  * Best linear unbiased estimator (BLUE)
  * Unbiased estimators — see estimator bias.
  * Particle filter
  * Markov chain Monte Carlo (MCMC)
  * Kalman filter, and its various derivatives
  * Wiener filter

In our practice we will mainly use Maximum likelihood estimators.

## Maximum likelihood method

Maximum likelihood estimation (MLE) is a method of estimating the parameters of a probability 
distribution by maximizing a **likelihood function**, so that under the assumed statistical 
model the observed data is most probable. The point in the parameter space that maximizes 
the likelihood function is called the maximum likelihood estimate.

Likelihood function (**L**), for a given model, which is discribed by a probablity
density function (**p**) depending on a parameter (**theta**), and data point (**x**)
is defined as:
  
  **L(theta|x) = p(X=x|theta)**

For several data points an overall likelihood is a product of individual.

Log-likelihood function is a logarithmic transformation of the likelihood function.
Because logarithms are strictly increasing functions, maximizing the likelihood 
is equivalent to maximizing the log-likelihood. As a logarithm of a product is 
a sum of logarithm calculations become easy. For a large number of data points
likelihood is a very small number, and it's logarithm is easy to handle.

As the sample size increases to infinity, sequences of maximum 
likelihood estimators have next properties:
  * consistency: the sequence of MLEs converges in probability to the value being estimated;
  * functional invariance: if **T** is MLE for a parameter **t**, and **g(t)** is a tranformation,
     then MLE for **a=g(t)** is **g(T)**;
  * efficiency: no consistent estimator has lower asymptotic mean squared error than the MLE;
  * asymptotic normality;
  * second-order efficiency after correction for bias: meaning that it has minimal 
     mean squared error among all second-order bias-corrected estimators.

Maximum-likelihood estimation is justified by a so-called 
[Wilks' theorem](https://en.wikipedia.org/wiki/Wilks%27_theorem).
The problem is that statistical tests (a parameter estimation can be considered as a finding 
of a best hypothesis / model to discribe observed data) generally require knowledge 
of the probability distribution of the test statistic. This is often a problem for likelihood method, 
where the probability distribution can be very difficult to determine.
states says that for infinite sample size, the distribution of the test statistic 
**−2log⁡(Λ)**  asymptotically approaches the chi-squared distribution under the null 
hypothesis. Here, **Λ** denotes the likelihood ratio: **Λ(t,tbest|x) = L(t|x)/L(tbest|x)**.
If **tbest** is a best parameter, then **Λ** shows how far one can move on **t**-scale
to be consistent with data (**x**).

### How MLE works

Let's consider a simple example in order to understand how MLE works.
We will have a 10 measurements of normal distributed quantity with known mean value
equal to zero and unknown (but fixed) width parameter. The goal will be to make an
estimation of sigma.

```bash
ostap -b mle_by_hand.py
```

## Chi-squared method

For the case of the large **N**, when the data can be grouped in bins with
the binning which covers enough all features of shapes for a signal and a
background distributions, a method of the chi-squared minimization could
be used to obtain parameters of distributions.

The idea of the method is that number of the event in each group (bin)
follows overall pdf and at the same time follows Poisson statistics.
As we already mentioned in the limit of large numbers Poisson statistics 
aproachs Gaussian distribution. The variance of the Poisson random variable 
is the random variable (standard deviation is a square root of it).
So for each set of parameters discribing overall pdf for each bin a
diviation in values of standard diviations can be calculated.
A sum of **n** normally distributed independent random values follows
well known **chi-squared distribution with (n-1) degrees of freedom**.

See more about [chi-squared distribution](https://en.wikipedia.org/wiki/Chi-square_distribution).

The fitting method is to find a minimum of chi2 in the parameter space.

Chi-squared method allows to calculated a confidense interval for
parameters from the change of a chi2. See, for example, a statistics 
part of [Review of Particle Physics](http://pdg.lbl.gov/2018/reviews/rpp2018-rev-statistics.pdf).

## Fitting in Ostap

Here we follow an [official tutorial](https://lhcb.github.io/ostap-tutorials/).

### Avalable pre-defined models

List below isn't exhausive (take a look into Ostape source code for the updates):
 * [Signal](https://lhcb.github.io/ostap-tutorials/fitting/signals.html)
 * [Background](https://lhcb.github.io/ostap-tutorials/fitting/backgrounds.html)
 * [Other](https://lhcb.github.io/ostap-tutorials/fitting/others.html)
 * [2D](https://lhcb.github.io/ostap-tutorials/fitting/2d.html)
 * [3D](https://lhcb.github.io/ostap-tutorials/fitting/3d.html)


### Fit result
The class **RooFitResult** get many decorations that allow to access fit results.
Also the simple math with fiting parameters is supported.
```python
result = ...
par1 = result.params()  ## get all floating parameters 
par2 = result.params( float_only = False ) ## all parameters 
a,v  = result.param ( 'a' )      ## par by name 
a,v  = result.param (  a  )      ## par by RooFit object itself 
p    = result.a                 ## par as attribute 
for par in result :   print par                ## iteration 
for name,par in result.iteritems() : print par ## iteration
print result.cov  ( 'a' , 'b' )   ## get the covariance submatrix  
print result.corr ( 'a' , 'b'  )  ## get the correlation coefficient
s = result.sum       ('S','B' ) ## S+B
d = result.divide    ('S','B' ) ## S/B
s = result.subtract  ('B','B1') ## B-B1
m = result.multiply  ('A','B' ) ## A*B 
f = result.fraction  ('S','B' ) ## S/(S+B)
```


## Validation of uncertainties

Here we follow [Kerim Guseynov's tutorial](https://indico.cern.ch/event/902801/)
(access could be restricted).

The result of a fit is ** parameter = value± +/- stat.err**.

After performing a fit one have to validate its result. As uncertainties obtained from 
the fitting routines are statistical, one need a number of data samples that differ 
within statistical unsertainties. An easiest way to get them, is to generate a random 
samples according to parameters of the obtained fit results.

```python
import ostap.fitting.toys as Toys
Toys.make_toys(
    pdf,           # the model to fit:  
    nToys,         # number of generate-fitTo repetitions
    data,          # variables to be pdf.generate’d
    gen_config,    # dict:  pdf.generate(..., **gen_config)
    fit_config={}, # dict:  pdf.fitTo(..., **fit_config)
    init_pars={},  # parameters’ values from the exp. fit
    more_vars={},  # dict:  {’key’:  lambda res, pdf:  func}
    silent=True,
    progress=True  # progress bar:  fraction of toys completed
)
```

If one wants to have different pdfs for generation and fitting:
```python
Toys.make_toys2(gen_pdf, fit_pdf, nToys, data,
    gen_config, fit_config, 
    gen_pars, fit_pars,
    more_vars, silent, progress)
)
```


```python
result, stats = Toys.make_toys(model, nToys, ...)
#result {’parname’:  [VE1, VE2, ...], ...} is a dict of lists of VE
result['parname'].value()
result['parname'].error()
#stats  {’parname’:  SE, ...} is  dict of Ostap.StatEntity’s
SE.nEntries(); 
SE.min(); 
SE.max(); 
SE.mean(); 
SE.rms()
```

**Important:** take care about initial random number generator seedidng.
For example (correct but reproducability of a result will impossible):
```python
import time
int_num = int(time.time())
ROOT.RooRandom.randomGenerator().SetSeed(int_num)
```

## Signal distribution

### Sideband subtruction

This method exploit an approach that shape of a background events under a signal peak
is the same as outside a peak. One can subtract the distribution from the distribution
for the events in the peak region.

Usually **+/-2sigma** around a peak position is used for the signal region and 
**(-7,-5)sigma** and **(5,7)-sigma*** intervals are used for subtraction.

**Important**:
  - Take care about proper normalization;
  - Background distribution should be quite flat.

### Fit-in-bin

One can split a data into subsamples on a control variable and perform a MLE in each bin.
This method is quite CPU consuming.


### sPlot techinqie

Here, idea is quite simple. Each event in MLE fitting has certain contribution to the
signal and background part of likelihood function. One can calculate a statistical
weight for each event with remarkable properties, which allow using them to determine
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

## Homework

### Tasks

  1. Create a toy model with fixed parameters containing peaking signal (30%) and a backgrounds of two cathegories: peaking (10&) and smooth (40%).
  2. For the 3000 events find an optimal binning for the chi2 fits
  3. Compare outcome and performance of the binned chi2 fit and unbinned maximum likelihood fit for different statistics of:
      - 50 events
      - 3000 events
      - 100000 events
  4. Validate uncertainties of the unbinned maximum likelihood fit for 3000 events.
  5. Compare parameters of the extended and non-extended maximum likelihood fits (50 and 3000 events).
  6. Add a non-correlated variable with different shapes for signal and a backgrounds. 
   Try to extract the distribution of the signal for this variable with three methods;

### Expected outcome
  * Document in pdf-format containing proper information 
  * Add code into your git repository
