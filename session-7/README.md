# Statistical tests

## General

A statistical hypothesis test is a method of statistical inference used to make decisions whether 
the collected data support a particular hypothesis. Two paradigms are available on the market:
  * Frequentist inference is a type of statistical inference based in frequentist probability, 
     which treats “probability” in equivalent terms to “frequency” and draws conclusions 
     from sample-data by means of emphasizing the frequency or proportion of findings in the data. 
  * Bayesian inference based on the Bayes' theorem is used to update the probability for a hypothesis 
     as more evidence or information becomes available. 

## Paired samples

A typical task of scientific researcher is to make inference about the question:
"Does a factor, which is infuencing of a cerain thing make a difference?"
To answer this question a measurement on a thing is done without and with the factor application.
These measurements frequently has a digital (or digital-like, for example yes-no) outcomes -- 
paired variables. Paired samples are samples to make inferences about the differences between 
two paired variables. 

An example, of such paired samples can be found in files: `WR2023-40yds.txt` and `RB2023-40yds.txt`.
These are results of 40-yard dash (a sprint covering 40 yards, 36.576 m), which athlets perform.
The question can be formulated as: "Does athlets tired after their 1st attempt?"

### Wilcoxon's test

Deascription:
  * https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test

Implementation:
  * https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html

```python
a1 = ... # initial sample
a2 = ... # sample with factor applied
import numpy as np
from scipy.stats import wilcoxon
res1 = wilcoxon( np.array(a1), np.array(a2) )
res2 = wilcoxon( np.array(a1), np.array(a2), alternative='greater')
print("Wilcoxon (difference) p-value : " + str( res1.pvalue ) )
print("Wilcoxon (positive  ) p-value : " + str( res2.pvalue ) )
```

**Note:** test statistics should be modified in case of no difference in paired sample.

### Student's t-test

The question can be reformulated to "Is the mean of difference between values 
in paired sample is not compatible with zero value?".

```python
diff2 = ... # list with differences 
import numpy as np
from scipy.stats import t
sample_mean = np.mean(diff2)
sample_variance = np.var(diff2, ddof=1)  # Note: set ddof=1 to calculate sample var
t_statistic = sample_mean / np.sqrt(sample_variance / len(diff2) )
pvalue = 1 - t.cdf(df=len(diff2) - 1, x=abs(t_statistic))
print("t test                p-value : " + str(pvalue) )
```

### Sign test

Each deviation between values in paired samples can be substiuted by +1 or -1 one, 
in cases they are positives or negative. Zeros should be dropped.
Test statistics **N(+1)-N(-1)** (in case of no-difference hypothesis) follows
binomial distribution with **p=0.5**. One can derive a confidence interval for
a given confidence level. See:
 * https://github.com/aleksha/data-analysis-tutorial/tree/master/session-0/inference#clopper-pearson-frequentists-approach 

## Problems

 * Implement sign test for the question about athlets.
