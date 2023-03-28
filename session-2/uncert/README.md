# Understanding of uncertainties

Somtimes spectrum for the regression desn't have corresponding uncertainties.
An example is the optic spectrum, which one can plot by: 
```bash
ostap draw.py
```

The zoom for the range (700,800) clearly suggests that data on y-axis has some uncertainty.
The idea, how to obtian individual uncertainty for each point can be found in `find_unc.py` script.
It scans with in a certain window, make polynomial fit and assigna uncertainty as a 
standard deviation. These uncertainties can't be directly used in statistical tests, but
can give an feeling, which features of spectrum belong to physics effects and which
is just statistical fluctuation.

**Note** that performed scan relyies on assumption that there is no physics structures in 
narrow windows (inside the window function is smooth enough).

