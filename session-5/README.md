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

## Weighted events 

Bohm and Zech discussed (page 61) some statistical properties of weighted events and
realized that the relative statistical error of a sum of N weighted events can be much
larger than the Poisson value 1/√N, especially when the individual weights are very
different. Thus we will usually refrain from weighting. However, there are situations
where it is not only convenient but essential to work with weighted events. If a large
sample of events has already been generated and stored and the p.d.f. has to be
changed afterwards, it is of course much more economical to re-weight the stored
events than to generate new ones because the simulation of high energy reactions
in highly complex detectors is quite expensive. Furthermore, for small changes the
weights are close to one and will not much increase the errors. As we will see later,
parameter inference based on a comparison of data with a Monte Carlo simulation
usually requires re-weighting anyway.

An event with weight **w** stands for **w** identical events with weight 1. 
When interpreting the results of a simulation, i.e. calculating errors, 
one has to take into account the distribution of a sum of weights:

**var(sum(w_i)) = sum(w_i^2)**

Strongly varying weights lead to large statistical fluctuations and 
should therefore be avoided.


## Homework

### Tasks
  1. Re-weight an MC dataset to the data for three variables: transverce momentum, rapidity and multiplisity.
  2. Oprimize a signal selection requirements using re-wighted MC for signal and sidebands for the background.
  3. Detemine a particle identification efficiency as a function of pseudorapidity and transverse momentum for the dataset and the efficiency map provided by a teacher.
  4. Estimate signal selection efficency for the B-mesons using MC. Compare results of the naive and accurate estimation.

### Expected outcome
  1. Reaort
  2. Code
