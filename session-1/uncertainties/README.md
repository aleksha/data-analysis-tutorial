# Uncertainties

## Profile likelihood

Log-likelihood profile is easy to draw.

Note, to evaluate profiled-likelihood one have to use an option `profile=True`.

See `profile.py`.

## Contours

Profile likelihood is exactly, what **Minuit (MINOS)** is doing, when procuces countours.

See [slide 53](https://indico.cern.ch/event/72320/contributions/2082589/attachments/1037201/1478048/roofit-intro-roostats-v11a.pdf)

A machinery to use Minuit from Ostap is also available.
See [an example](https://github.com/OstapHEP/ostap/blob/bc897f09f415f46334a62c82fb07f86d8497147b/ostap/fitting/tests/test_fitting_minuit.py).

## Validation of uncertainties

Here we follow [Kerim Guseynov's tutorial](https://indico.cern.ch/event/902801/)
(access could be restricted).

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


