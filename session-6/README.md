# Fourier transformation / Regression
    * Why fast Fourier transform (FFT) is needed?
    * Using SciPy for FFT
    * What is a regression?
    * Least square and Maximum Likelihood regression methods
    * Using TMVA to solve regression problem (MLP, BTD).

## Fourier transform

In mathematics, a Fourier transform (FT) is a mathematical transform that decomposes a function 
(often a function of time, or a signal) into its constituent 
frequencies, such as the expression of a musical chord in terms of the volumes and frequencies of its constituent notes. 
The term Fourier transform refers to both the frequency domain representation and the mathematical operation 
that associates the frequency domain representation to a function of time. 

We met it alreadu in a Introduction to N&HEP course, when discussing electron scattering on nuclei 
and particles, where a space distribution of charge define features of the electron scattering cross 
section. See Povh·Rith·Scholz·Zetsche's "Particles and Nuclei" (page 62 and futher).

An algorithm of **fast Fourier transform (FFT)** computes the discrete Fourier transform (DFT) of a sequence, 
or its inverse (IDFT), converting a signal from its original domain (often time or space) to a representation 
in the frequency domain and vice versa. For data-analysis FFT is a filtering algorithms allowing 
to understand a noise composition and reduce it.

### Example of using SciPy for FFT for the TPC noise generation
Time-Projection Chamber (TPC) signal is discussed in a 
[MS Word document](https://github.com/aleksha/electronic-noise/blob/master/docs/MC4NOISE.docx). 
Fourier analysis is used to obtain features of the electronic noise of the TPC.

Analysis is done using **fft** pack in SciPy:
  * https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.fft.html#scipy.fftpack.fft

### IPython example

First one has to download a data file (`dump.txt`)

```bash
wget http://adzyuba.web.cern.ch/adzyuba/d/dump.txt
```

Then, see `FFT.ipynb` on how to remove some noise.

## Regression analysis

In statistical modeling, **regression analysis** is a set of statistical processes 
for estimating the relationships between a dependent variable (often called 
the 'outcome variable') and one or more independent variables (often called 
'predictors', 'covariates', or 'features'). 

It's quite a bad term, as can be confused with a 
[regression toward the mean](https://en.wikipedia.org/wiki/Regression_toward_the_mean),
a "result" of the first paper about regression analysis by John Galton.

We did alredy regression, when were construction classification variables.

As physicsts we have try to avoid pure regression and try to understand 
underlying nature of phenomena (see cow example below). But sometimes,
it's hard to avoid it --- we  have some data and need to evaluate best 
value of other variable out of it. Plus, someone can gives up and go
to a finance sector, where they care only about money...

## Assumptions
By itself, a regression is simply a calculation using the data. In order to interpret the output 
of a regression as a meaningful statistical quantity that measures real-world relationships, 
researchers often rely on a number of classical assumptions. These often include:

  * The sample is representative of the population at large.
  * The independent variables are measured with no error.
  * Deviations from the model have an expected value of zero. 
  * The variance of the residuals is constant across observations (homoscedasticity).
  * The residuals are uncorrelated with one another. Mathematically, the variance–covariance 
    matrix of the errors is diagonal.

## Least square

### SciPy
 * [Solve a linear least-squares problem with bounds on the variables.](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.lsq_linear.html)
 * [Solve a nonlinear least-squares problem with bounds on the variables.](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html)

1st component of PCA and linear regresion is a bit different but quite close concepts.
For the 2D case **x** and **y** are equally important, so the total length perpendicular
to a line is minimised. Instead, for the least square method the lines are parallel
to the y-direction.

Least square liniear regressions are sensitive to the outliers.

### Typical mistakes

  * Non-homoscedasticity (American TV example)
  * Strondly correlated predictors (height and foot length example)
  * Non-adecvate model (cow example)
  * Parameter correlated with another "hidden" paramtters 
     (clouds and enemy palane number on successfull bombing)

## Jackknife resampling

The jackknife estimate of a parameter can be found by estimating the parameter for each subsample omitting the _i_-th observation.

See more in example folder.
