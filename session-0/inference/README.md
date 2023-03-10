# Frequentisits and Bayesian inferences

> "Bayesians address the question everyone is interested in by using assump-
> tions no-one believes, while Frequentists use impeccable logic to deal with an
> issue of no interest to anyone" (c) Louis Lyon

See next links to digg into problem:
  * https://arxiv.org/abs/1301.1273
  * https://indico.cern.ch/event/343570/contributions/804186/attachments/676123/929060/Lyons_L2.pdf

## Clopper-Pearson (frequentists approach)

Confidence interval for certain confidence levels, number of trials and number of success.
Requires `scipy` and `matplotlib`

```bash
python binomial_interval.py
```

## Bayesian approach

bayesian comparison of two options. For example: 10/10 vs. 48/50:
```bash
ostap best.py
```

Check prior influence:
```bash
ostap prior.py
```
## Rule of succession

Answering a question: "f we repeat an experiment that we know can result 
in a success or failure, **n** times independently, and get **s** successes, 
and **n−s** failures, then what is the probability that the next repetition 
will succeed?", Laplace proposed to use **(s+1)/(n+2)** ratio to compute 
probability.

This is equivalent to the solution of bayesian approach with uniform prior.

For more details see:
  * https://en.wikipedia.org/wiki/Rule_of_succession
