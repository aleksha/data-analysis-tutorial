# Cut-based techique.
  * How good is your fit?
    - Pull distributions;
    - Toys to obtain likelihood distributions;
  * How to find best requirements?
  * Significance
  * Are requirements optimal?
    - Fluctuations
    - Look elswhere effect
    - When to use signal for background rejection optimisations?

## Goodness-of-fit

### Nice pull plots

For large number of events it's good to produce a pull-plots, deviation 
(in **sqrt(n)**for **n** events in bin) for each bin.  This plot should
not contain so-called wiggles ofintervalse of large deviation. An example 
of f function, which draw nice plots:

```python
def draw_param(r_fit, w_fit, h_fit, N_BINS, var, W_max, name, XTitle, Prefix, Type, var_Units):

    var_list = []
    for idx in range(N_BINS+1):
        var_list.append(var.getMin()+idx*(var.getMax()-var.getMin())/N_BINS )
    h_pull = h1_axis(var_list)
    for idx in range(1,N_BINS):
        h_pull[idx]=VE(h_fit[idx-1][3],0**2)

    h_pull.GetYaxis().SetRangeUser(-4,4)
    h_pull.GetYaxis().SetTitle("#Delta / #sigma")
    h_pull.GetYaxis().SetTitle("#Delta / #sigma")
    h_pull.GetYaxis().SetTitleSize(0.2)
    h_pull.GetYaxis().SetTitleOffset(0.2)
    h_pull.GetYaxis().SetLabelSize(0.1)
    h_pull.GetXaxis().SetLabelSize(0.15)
    h_pull.SetFillColor(34)

    line_up   = ROOT.TLine(var.getMin(),  2, var.getMax(),  2)
    line_down = ROOT.TLine(var.getMin(), -2, var.getMax(), -2)
    line_up  .SetLineColor(2)
    line_down.SetLineColor(2)


    #-------------------------------------------------------------------
    # Prepare for drawing
    #-------------------------------------------------------------------

    Y_title = 0.92*W_max
    Y_step  = 0.05*W_max

    x_pos = var.getMin() + 0.05 * (var.getMax() - var.getMin())

    percentage = " ("+ "{:2.2f}".format( 100. * r_fit("S" )[0].error() / r_fit("S" )[0].value() ) + "%)"
    text_SIG  = "SIGNAL = " + "{:5.0f}".format(r_fit("S" )[0].value())
    text_SIG += " #pm" + "{:4.0f}".format(r_fit("S" )[0].error()) + percentage
    text_BKG  = "BKG = " + "{:5.0f}".format(r_fit("B" )[0].value())
    text_BKG += " #pm" + "{:4.0f}".format(r_fit("B" )[0].error())


    labels = []
    labels.append( ROOT.TLatex( x_pos, Y_title - 0.0*Y_step, text_SIG ) )
    labels.append( ROOT.TLatex( x_pos, Y_title - 1.5*Y_step, text_BKG ) )

    for lb in labels :
        lb.SetTextSize(0.04)

    w_fit.GetXaxis().SetTitle(XTitle+", "+var_Units)
    w_fit.GetXaxis().SetTitleSize(0.05)
    w_fit.GetXaxis().SetTitleOffset(0.9)
    w_fit.GetYaxis().SetRangeUser(0.01, W_max)
    w_fit.GetYaxis().SetTitleOffset(0.9)
    w_fit.GetYaxis().SetTitle("Candidates per "+str((var.getMax()-var.getMin())/N_BINS)+" "+var_Units)
    w_fit.GetYaxis().SetLabelSize(0.025)

    #-------------------------------------------------------------------
    # Draw it!
    #-------------------------------------------------------------------

    canv = ROOT.TCanvas("canv","canv",700,800)
    canv.Divide(1,2)

    pad1 = canv.GetListOfPrimitives().FindObject("canv_1")
    pad2 = canv.GetListOfPrimitives().FindObject("canv_2")
    pad1.SetPad(0.00, 0.11, 1.00, 1.00)
    pad2.SetPad(0.00, 0.00, 1.00, 0.10)

    canv.cd(1)
    w_fit.Draw()
    for lb in labels: lb.Draw()
    canv.cd(2)
    h_pull.Draw("HIST")
    line_up  .Draw()
    line_down.Draw()

    canv.Print(Prefix+"_"+name+"."+Type) 
    canv.Close()
```

### Chi-squared test

The chi2 method uses a statement that for the true model a chi2-value 
foloows analysitaccly known cho2-distribution. Let's devie a 
**p-value** as a quantile of the chi2-sistribution for the observed chi2.
Let also choose some significance level **alpha**.
Three cases are possible:
 * **p<alpha** - model discribes data impossibly well
 * **p>1-alpha** - model doesn't discribe data
 * overwise model is consuistent with data

For the chi2-fits a minimale chi2 per degrees of freedom shoul be close to unity.
Quantiles can be found in [Review of Particle Physics](http://pdg.lbl.gov/2018/reviews/rpp2018-rev-statistics.pdf).

### Toys for MLE

For MLE method a shape of the likelihood distribution isn't known analitically.
It could be generated using toys:
 - toy samples are generated according fitted model
 - they are re-fitted with the model (at each re-fit a likelihood is computed)
 - compare observed value of likelihood (from main fit) with obtained distribution
  (same ideology as for the chi2 case).

## Significance

A result has **statistical significance** when it is very unlikely to have occurred 
given the null (background only) hypothesis.

Let's follow [slides of Pietro Vischia](https://indico.cern.ch/event/648004/contributions/3032092/attachments/1696821/2731727/2018-08-01_pseudosignificancesAtQCHSXIII_vischia.pdf).

One have to quote what he means by significance.

### Figire-of-merit in Ostap

If figure-of-merit is natural and equals to **sigma(S)/S** (note that it is equal to **sqrt(S+B)/S**):
Note that no explicit knowledge of background is needed here - it enters indireclty via the 
uncertainties in signal determination.
```python
signal = ...  ## distribition for signal
fom1   = signal.FoM2 () ## FoM for var<x cut 
fom2   = signal.FoM2 ( False ) ## FoM for var>x cut
```

If figure-of-merit is defined as **S/sqrt(S+alpha*B)**:
```python
signal = ... 
background = ... 
alpha = ... 
fom1  = signal.FoM1 ( background , alpha ) ## FoM for var<x cut 
fom2  = signal.FoM1  ( background , alpha , False ) ## FoM for var>x cut
```


## Traps

### Fluctuations or something else

If you see in your data some unexpected features, think a bit:
 * if it's smaller than your resolution but significant, when 
  something probably gows wrong
 * are the any peaking backgrounds / contributions?
   - miss identified tracks
   - clones (my favorite Theta+ signal out of K0S-->pi+pi- reqion with clonned pi+ as proton track )
   - different sources of signal (Sigma_c--> Lambda_c pi spectrum at LHCb has clearly visible 
     Lambda_c(2595)-->Sigma_c pi contribution due to limited phase space)
   - feed-downs (see Omega_c* analysis)
   - cusps at the threshold of coupled channel ( K+K- <--> K0K0bar)
   - ...
 * just statistical fluctuation?

### Look-elsewhere effect

The look-elsewhere effect is a phenomenon in the statistical analysis of scientific experiments 
where an apparently statistically significant observation may have actually arisen by chance because 
of the sheer size of the parameter space to be searched.

The problem is in how to define "elsewhere".

Usually experimentalists quotes a local and a global significane for the search region.
Latest accounts the probability to have a fluctuation with a local significance for the spectum of interest.

Toy Monte-Carlo ubde background only assumption later fitted with the full model
is usually used to find this probability.

## When to use signal for background rejection optimisations?

Soon, we'll meet a problem of classification for the background suppression.

A typical workflow is to use asimulated signal sample and sidebands as a 
background proxy to build a classifier.

Results of the __sPlot__ techiques can be used as a signal proxy, but
only when signal is known and clearly visible and all its features is undersood. 
One should always remember that the statistical fluctuations will affect such
studies.

## Homework

### Tasks
  1. For the Lambda_c dataset find an optimar requirements.
  2. Create a bunch of a thousand toy background only datasets of three variables: one a discriminating and two for selection. Find a dataset with a lagrest gaussian-like fluctuation on a discriminating variable.
  3. Detrmine a local and a global significance of the "signal".
  4. "Optimize" requirements on two control variable to reach a besl local significance.

### Expected outcome
 1. A PDF report
 2. Code in git repository
