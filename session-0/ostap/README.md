# Ostap tutorial

## Tutorials
A copy of the [official Ostap tutorial](https://lhcb.github.io/ostap-tutorials/)
is done with a permissions from Ivan Belyaev (father of this system).

See also [LHCb tutorials](https://github.com/lhcb/ostap-tutorials)

In addition, some attepmts could be found in `OSTAP.md` and `HISTO.md` files

## Module importing

Unfortunately official ostap tutorial contain old (LHCb) naming of the modules.
Proper one can be found in a source code (test folders):
  * Math (including math for `VE`) - [link](https://github.com/OstapHEP/ostap/tree/master/ostap/math/tests)
  * Fitting - [link](https://github.com/OstapHEP/ostap/tree/master/ostap/fitting/tests)
  * Histo - [link](https://github.com/OstapHEP/ostap/tree/master/ostap/histos/tests)
  * I/O - [link](https://github.com/OstapHEP/ostap/tree/master/ostap/io/tests)
  * Trees - [link](https://github.com/OstapHEP/ostap/tree/master/ostap/trees/tests)
  * ... and many more

Don't forget that there is a search inside repositories on a GitHub! 

### Commomly needed

```python
from ostap.math.math_ve import * # Math for VE
import ostap.io.zipshelve    as     zipshelve
import ostap.io.rootshelve   as     rootshelve
from   ostap.histos.histos  import h1_axis, h2_axes
```

## Particle physics

Check out `Ostap.Kinematics` and `Ostap.LorentzVector`.

  * {Datliz plot example}(https://github.com/OstapHEP/ostap/blob/master/ostap/math/tests/test_math_dalitz.py)

## More features

 - **Math**
    * [Finding roots](https://github.com/OstapHEP/ostap/blob/master/ostap/math/tests/test_math_rootfinder.py)
    * {Test for primes}(https://github.com/OstapHEP/ostap/blob/master/ostap/math/tests/test_math_primes.py)
    * Linear algebra([1](https://github.com/OstapHEP/ostap/blob/master/ostap/math/tests/test_math_linalgt.py), [2](https://github.com/OstapHEP/ostap/blob/master/ostap/math/tests/test_math_linalg2.py))
    * [Interpolation](https://github.com/OstapHEP/ostap/blob/master/ostap/math/tests/test_math_interpolation.py)
    * {Derivatives}(https://github.com/OstapHEP/ostap/blob/master/ostap/math/tests/test_math_derivative.py)
    * [Integrals](https://github.com/OstapHEP/ostap/blob/master/ostap/math/tests/test_math_integral.py)
    * [Covariance matrix transformation](https://github.com/OstapHEP/ostap/blob/master/ostap/math/tests/test_math_covtransform.py)
  - **Input/output**
    * [Shelves](https://github.com/OstapHEP/ostap/blob/master/ostap/io/tests/test_io_shelves.py)
  - **Useful utils** [link](https://github.com/OstapHEP/ostap/tree/master/ostap/utils)
    * Memory - you can see how much memory a part of your code takes
    * Timing - same with timing
    * Progress bar
    * PDG format
  - **Graphs**
    * How to make graphs easy, please, check [this link](https://github.com/OstapHEP/ostap/blob/1196b8676adba9422687ddef13ddfa5553d53e09/ostap/histos/graphs.py)
    * [Graph summary](https://github.com/OstapHEP/ostap/blob/master/ostap/plotting/tests/test_plotting_summary_graph.py)
  - **Histograms**
    * [Test functionality](https://github.com/OstapHEP/ostap/blob/master/ostap/histos/tests/test_histos_histos.py)
    * [Compare](https://github.com/OstapHEP/ostap/blob/master/ostap/histos/tests/test_histos_compare.py)
    * [Interpolation](https://github.com/OstapHEP/ostap/blob/master/ostap/histos/tests/test_histos_interpolation.py)
    * Parametrization ([1](https://github.com/OstapHEP/ostap/blob/master/ostap/histos/tests/test_histos_parameterisation.py), [2](https://github.com/OstapHEP/ostap/blob/master/ostap/histos/tests/test_histos_parameterisation2.py), [3](https://github.com/OstapHEP/ostap/blob/master/ostap/histos/tests/test_histos_parameterisation3.py))
  - **Statistics**
    * Best Linear Unbiased Estimator [BLUE](https://github.com/OstapHEP/ostap/blob/master/ostap/stats/tests/test_stats_blue.py)
    * [Moments](https://github.com/OstapHEP/ostap/blob/master/ostap/stats/tests/test_stats_moment.py)
  - **Logger**
    * [test logger](https://github.com/OstapHEP/ostap/blob/master/ostap/logger/tests/tesst_logger_logger.py)
