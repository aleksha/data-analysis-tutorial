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
```math
N = \frac{\sigma}{L\timesB\times\varepsilon},
```
where enumerator contains [cross-section](https://en.wikipedia.org/wiki/Cross_section_(physics)) 
of the X production, and the denominator contains: integrated 
[luminosity](https://en.wikipedia.org/wiki/Luminosity_(scattering_theory)) 
(**L**), probebility of the X to decay into a selected final state (**B**) and overall 
efficiency of the detection.


## Fitting

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
