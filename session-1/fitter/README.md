# Fitting tutorial

## Download file with data

```bash
wget http://adzyuba.web.cern.ch/adzyuba/d/test_file.root
```

## Browsing dataset

```python
from ostap.utils.timing import timing
from ostap.utils.memory import memory
rfile = ROOT.TFile("test_file.root","READ")
with memory():
    ds_pi = rfile["ds_pi"]
    ds    = rfile["ds_k"]
with timing():
    print( ds )
```

## Variables in the dataset

  1.  `pt` - transverce momentum of charm baryon candidate
  2.  `y` - rapidity pf charm baryon
  3.  `ct` - **Lifetime*SpeadOfLight, mm**
  4.  `ch` - quality of a decay chain fit
  5.  `id` - assumed ID (negative for antyparticles)
  6.  `ipc` - **Chi2IP** how far is an impact parameter of a reconstructed baryon from a related primary vertex (pp interaction point)
  7.  `p_p` - proton full momentum
  8.  `eta_p` - proton pseudorapidity
  9.  `phi_p` - proton azimuthal angle
  10. `p_k` - kaon (K-) full momentum
  11. `eta_k` - kaon pseudorapidity
  12. `p_3` - pion (for **ds_pi**) or K+ (**ds**) full momentum
  13. `eta_3` - its pseudorapidity
  14. `ntrk` - number of reconstructed so-called long track in the event
  15. `NNp` - var for proton to be proton (neural network decision)
  16. `im` - mass of **pKh** candidate
  17. `im_kp` - mass with **proton --> kaon** hypothesis
  18. `im_pi` - mass with **proton --> pion** hypothesis
  19. `im_hp` - mass with **K+ --> pi+**
  20. `m12` - two-body mass for products (1 and 2)
  21. `m13` - 1 and 3
  22. `m23` - 2 and 3
  23. `NNk` - var kaon to be kaon (neural network decision)
  24. `NN3` - K+ to be K+ (or pi+ to be pi+)
  25. `lgi` - **log10(Chi2IP)**

