# Signal extraction

## Content

  * Fitting a signal:
    - Chi-square and maximum likelyhood fits.
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
(**L**), probebility of the X to decay into a selected final state (**B**) and overall 
efficiency of the detection (**ε**). Note, that **N** is a Poisson-distributed random value.

In practice, there are background events in addition to signal ones. 
The task is to make an estimation (**S**) of **N**. 
Differnt estimators (means different rules for calculating an estimate 
of a given quantity based on observed data) are posiible.
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
density function (**p**) depoending on a parameter (**theta**), and data point (**x**)
is defined as:
  
  **L(theta|x) = p(X=x|theta)**

For several data points an overall likelihood is a porduct of individual.

Log-likelihood function is a logarithmic transformation of the likelihood function.
Because logarithms are strictly increasing functions, maximizing the likelihood 
is equivalent to maximizing the log-likelihood. As a logrithm of a product is 
a sum of logarithm calculations become easy. For a large number of data points
likelihood is a very small number, and it's logarythm is easy to handle.

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
states says that  for infinite sample size, the distribution of the test statistic 
**−2log⁡(Λ)**  asymptotically approaches the chi-squared distribution under the null 
hypothesis. Here, **Λ** denotes the likelihood ratio: **Λ(t,tbest|x) = L(t|x)/L(tbest|x)**.
If **tbest** is a best parameter, then **Λ** shows how far one can move on **t**-scale
to be consistent with data (**x**).

## How MLE works

Let's consider a simple example in order to understand how MLE works.
We will have a 10 measurements of normal distributed quantity with known mean value
equal to zero and unknown (but fixed) width parameter. The goal will be to make an
estimation of sigma.

## Fitting

## Validation of ncertainties

Here we follow Kerim Guseynov's tutorial.

The result of a fit is ** parameter = value± +/- stat.err**.

After performing a fit one have to validate its result. As uncertainties obtained from 
the fitting routines are statistical, one need a number of data samples that differ 
within statistical unsertainties. An easeast way to get them, is to generate a random 
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

## Homework

### Tasks

  1. Create a toy model with fixed parametrs containing peaking signal (30%) and a bakgrounds of two cathegories: peaking (10&) and smooth (40%).
  2. For the 3000 events find an optimal binning for the chi2 fits
  3. Compare outcome and performance of the binned chi2 fit and unbinneb maximum likelihood fit for different statistics of:
      - 50 events
      - 3000 events
      - 100000 events
  4. Validate uncertainties of the unbinned maximum likelihood fit for 3000 events.
  5. Compare parameters of the extended and non-extended maximum likelihood fits (50 and 3000 events).
  6. Add a non-correlated variable with differentr shapes for signal and a backgrounds. 
   Try to extract the distribution of the signal for this variable with three methods;

### Expected outcome
  * Document in pdf-format containig proper information 
  * Add code into your git repository
