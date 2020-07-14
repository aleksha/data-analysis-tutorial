# Dealing with Monte-Carlo
  * Random number generators
  * How to re-weight MC to data?
  * Weighted fit for efficiency evaluation.
  * How to estimate efficiency for not-well reconstructed events?
  
## Random number generation in ROOT

See [documentetion](https://root.cern.ch/doc/master/classTRandom.html) to
a **TRandom** class family.

One can also have a look on [docs](https://docs.python.org/3/library/random.html) 
for **random** modules in Python standard library and a 
[random sampling in NumPy](https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html).

Two aspects to keep in mind:
  * What is the period of the random generator you use?
  * What is the seeding startegy.

More delatils in Bohm and Zech book.

## Efficency evalueation

Efficency is the a ratio of numbers for **accepted** and **generated events**.
However, these are not statistically independent samples.
The right way is to use independent samples of **accepted** and **rejected events**.
```python
h_eff = 1. / (1. + h_rej / h_acc)
```

Note, that uncertainty for 0 events is +-1.

These idea can be also used for two factors analysis. See **two_factors.pdf**.

See more on binomial efficencies in [ostap tutorial](https://lhcb.github.io/ostap-tutorials/getting-started/Histos.html).

## Optimal binning

It is not a rare case when one needs to find the binbing of the histogram that ensures 
almost equal bin populations. An example is building effciency map on a number of 
accepted events; This task could be solved using **eqaul_bins** method:

```python
very_fine_binned_histo = ... ## get the fine binned histograms 
edges1 = fine_binned.equal_edges ( 10 ) ## try to fing binning with 10 almost equally populated bins 
edges2 = fine_binned.equal_edges ( 10 , wmax = 5 ) ## try to fing binning with 10 almost equally populated bins, but avoid bins wider than "wmax"
```


## Weighted events 

We also quote here Bohm and Zech (page 120):

> We discussed (page 61) some statistical properties of weighted events and
> realized that the relative statistical error of a sum of N weighted events can be much
> larger than the Poisson value 1/√N, especially when the individual weights are very
> different. Thus we will usually refrain from weighting. However, there are situations
> where it is not only convenient but essential to work with weighted events. If a large
> sample of events has already been generated and stored and the p.d.f. has to be
> changed afterwards, it is of course much more economical to re-weight the stored
> events than to generate new ones because the simulation of high energy reactions
> in highly complex detectors is quite expensive. Furthermore, for small changes the
> weights are close to one and will not much increase the errors. As we will see later,
> parameter inference based on a comparison of data with a Monte Carlo simulation
> usually requires re-weighting anyway.
>
> An event with weight **w** stands for **w** identical events with weight 1. 
> When interpreting the results of a simulation, i.e. calculating errors, 
> one has to take into account the distribution of a sum of weights:

**var(sum(w_i)) = sum(w_i^2)**

> Strongly varying weights lead to large statistical fluctuations and 
> should therefore be avoided.

## Re-weighting with Ostap

Here, we follow [official tutorial](https://lhcb.github.io/ostap-tutorials/tools/reweighting.html).

## Weighted fit for efficiency evaluation

Sometimes multidimensional efficency map is provided not by a simulation, 
but from the data itself (for example, from calibration sample). Nest
weighted fit procedure can be used to evaluate an efficency:
```python
h_eff  = TH2F(... # efficency map on x and y variables

mass   = ROOT.RooRealVar('mass','disctiminating var', ...  )
x      = ROOT.RooRealVar('x','x var', ...  )
y      = ROOT.RooRealVar('y','y var', ...  )
weight = ROOT.RooRealVar( ... )
varset = ROOT.RooArgSet ( mass, x, y,  weight )

dataset_with_weights = ROOT.RooDataSet ( 'dataset_with_weights' , 'temp dataset' , varset )
for event in dateset_original:
    w = (1. / h_eff(event["x"], event["y"]) ).value() # histo as function
    mass.setVal( evemt["mass"] )
    weight.setVal( w)
    dataset_with_weights.add( varset )

dataset_weighted = dataset_with_weights.makeWeighted( "weight" )
result_w = model.fitTo( dataset_weighetd, ... )
result_o = model.fitTo( dataset_original, ... )
```

Use original-to-weighted ratio as an efficency for dataset.

### Related systematics

Note, that the results of the weighted and non-weighted fits are correlated.
To distinguish uncertainties related to a finite size of a calibration sample
a sampling-based toy Monte-Carlo procedure can be used:
  1. Sample an efficiency histogram a lot of times.
  2. Perform weighted fit procedure using these sampled histograms.
  3. Evaluate mean and the standard deviation of the result.
Mean value should be in agreement with the nominal one.
Standard deviation can be interpreted as a corresponding systematics.

There is an easy way to sample the histograms according to their content, 
e.g. for toy-experiments: 
```python
h_new = h_original.sample()
H_new_posivive = h_original.sample( accept = lambda s : s > 0 )
```
Better to use second way with the requirement that sampled values are positive

### Important issues
  * Check that the correlated requrements are the same in the efficency evaluation
  * Calculate the uncertainty for extarapolation (events placed outside of the
      efficiency map) by comparing different extrapolation techniques.
      At least constatnt and linear.


## Efficiency and not-well reconstructed events

Even truth-matched (detector hits a done by a generated particle / decay products
of interest) events can be not well reconstructed. It's good to perform a fit with 
the full (S+B)-model for them to get a fraction of thruth-matched events.

One can also can conside a fit of the data-like mixture of simulated events
and background events generated according a model obtained from a fit of
real data. This give mre precise correction factor.

## Homework

### Tasks
  1. Re-weight an MC dataset to the data for three variables: transverce momentum, rapidity and multiplisity.
  2. Oprimize a signal selection requirements using re-wighted MC for signal and sidebands for the background.
  3. Detemine a particle identification efficiency as a function of pseudorapidity and transverse momentum for the dataset and the efficiency map provided by a teacher.
  4. Estimate signal selection efficency for the B-mesons using MC. Compare results of the naive and accurate estimation.

### Expected outcome
  1. Reaort
  2. Code
