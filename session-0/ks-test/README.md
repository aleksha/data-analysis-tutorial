# Example of Kolmogorov-Smirnov test

## Task

There are 16 samples, which contains reconstructed energies with the same input, but different channels of a multichannel pre-amplifire. One have to say, are these samples statistillay different or not.

## Kolmogorov-Smirnov test

In statistics, the **Kolmogorov–Smirnov test** (or KS test) is a nonparametric test of the equality of continuous or discontinuous one-dimensional probability distributions.
The test that can be used to compare a sample with a reference probability distribution (one-sample KS test), or to compare two samples (two-sample KS test). It is named after Andrey Kolmogorov and Nikolai Smirnov. 

[The two-sample KS](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test#Two-sample_Kolmogorov%E2%80%93Smirnov_test) test is one of the most useful and general nonparametric methods for comparing two samples, as it is sensitive to differences in both location and shape of the empirical cumulative distribution functions of the two samples. 

> Note that the two-sample test checks whether the two data samples come from the same distribution. 
> This does not specify what that common distribution is (e.g. whether it's normal or not normal). 
> A shortcoming of the Kolmogorov–Smirnov test is that it is not very powerful because it is devised to be sensitive 
> against all possible types of differences between two distribution functions.

The `scipy` realization of the KS test is used for the task. 
See details on the [link](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html).

## Example

First one let's plot the data as histogramms. For this one can use `Draw-All.py` script.
The result is presented in a figure [fig_raw.png](https://github.com/aleksha/data-analysis-tutorial/blob/master/session-0/ks-test/figs/fig_raw.png).

It's visible that distributions have no commont location parameter. In these sense they all be different.

To perform KS-test all the distribution has been shifted (with no re-scaling) to approximately same location parameter. A new location parameter is choosen that the [median](https://en.wikipedia.org/wiki/Median) of a new distribution shoud be equal 160. Median is a robust location parameter estimator (see [robust statistics](https://en.wikipedia.org/wiki/Robust_statistics)).

After the shift a KS-test is performed using `Shift-KS-test-2.py` script. At two-sigma significance level is used.
The results are presented in `figs/` directory. For example, figure `figs/fig_ks_wrt_ch00.png` shows the comparison of the 1st sample with other samples.

## To reproduce exactly this result

To reproduce this result one can try to use **Ostap** _via_ **conda**.
Tne next is tested with Ubuntu 20.04 LTS (64-bit).

First you have to install and update conda. Here are the commands:
```bash
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
source ~/miniconda3/etc/profile.d/conda.sh # replace "~/miniconda3/" with your conda path if you've changed it
conda config --add channels conda-forge
conda update -n base -c defaults conda
```
**Note:** If you close your shell you will have to run conda.sh again; alternatively, you can run "conda init" to make the script run automatically each time you open your shell, for more information run "conda init --help"

Next step is to setup the environment and install the requirements.
```bash
conda create --name pres-mc
conda activate pres-mc
conda install --yes --file requirements.txt
```

Everything is ready to start ostap:
```bash
ostap -b Draw-All.py
ostap -b Shift-KS-test-2.py
```
