# Cut-based techique.
  * How good is your fit?
    - Pull distributions;
    - Toys to obtain likelihood distributions;
  * How to find best requirements?
  * Are requirements optimal?
    - Fluctuations
    - Look elswhere effect
    - When to use signal for background rejection optimisations?

## Goodess-of-fit

### Nice pull plots

An example of the function, which draw nice plots.

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

## Homework

### Tasks
  1. For the Lambda_c dataset find an optimar requirements.
  2. Create a bunch of a thousand toy background only datasets of three variables: one a discriminating and two for selection. Find a dataset with a lagrest gaussian-like fluctuation on a discriminating variable.
  3. Detrmine a local and a global significance of the "signal".
  4. "Optimize" requirements on two control variable to reach a besl local significance.

### Expected outcome
 1. A PDF report
 2. Code in git repository
