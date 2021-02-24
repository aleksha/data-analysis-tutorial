#===============================================================================
alpha_level  = 0.0455 # 2sigma
#alpha_level = 0.0027 # 3sigma
#===============================================================================
canvas.Close()
import numpy as np
import scipy.stats as stats
import statistics as py_stat
#===============================================================================
def proj2hist( sample , tname, bins = 100, low = 163, high = 173):
    """This funcion projects a sample into TH1F"""
    hist = ROOT.TH1F(tname,tname+";E, a.u.;N",bins,low,high)
    for ev in sample:
        hist.Fill( ev )
    return hist
#
def ch2str( ch ):
    if ch<10:
        return ( "0"+str(ch) )
    return str(ch)
#===============================================================================
# Read data into numpy arrays
#
E = []
for ch in range(1,17):
    energy = []
    file_name = "data/20210218-ch" + ch2str(ch) + ".e.txt"
    with open(file_name,"r") as fl:
        for line in fl:
            energy.append(float(line))

    E.append( np.array(energy) )
#===============================================================================
# Print stat for channel and produce data with median equal 160.
# (no rescaling so far)
#
SE = []
for i in range( 16 ):
    ss = "ch.: "
    if i<10:
        ss += "0"
    ss += str(i) + "  "
    ss += "min/max: " + str( min( E[i] ) ) + "/" + str( max( E[i] ) ) + "  "
    ss += "mean: " + str( py_stat.mean( E[i] ) ) + "  "
    ss += "rms: " + str( py_stat.stdev( E[i] ) ) + "  "
    ss += "median: " + str( py_stat.median( E[i] ) )
    print( ss )
    median = py_stat.median( E[i] )
    SE.append( E[i] - median + 160. )

#===============================================================================
# Draw shifted samples
#
hh = []
ll = []
for i in range( 16 ):
    hh.append( proj2hist( SE[i], tname = "h_"+str(i), bins = 230, low=150, high=173 ) )
    hh[i].GetYaxis().SetRangeUser(0,100)
    ll.append( ROOT.TLatex(153,90,"ch. : "+ch2str(i)) )

#===============================================================================
# Perform Kolmogorov-Smirnov tests for shifted samples
#
canv = ROOT.TCanvas("canv","canv",1100,1100)
canv.Divide(4,4)

for ch1 in range(16):
    dec = []
    # Paint all blacks except current one, which should be red
    for i in range(16):
        hh[i].SetLineColor(1)
        hh[i].SetFillColor(1)
        hh[i].SetFillStyle(0)
    #
    for ch2 in range(16):
        answer =  stats.ks_2samp(SE[ch1],SE[ch2])
        if answer.pvalue > alpha_level:
            dec.append( ROOT.TLatex(153,80,"GOOD wrt  ch."+ch2str(ch1)) )
        else:
            dec.append( ROOT.TLatex(153,80,"BAD  wrt. ch."+ch2str(ch1)) )
            hh[ch2].SetLineColor(2)
            hh[ch2].SetFillColor(2)
            hh[ch2].SetFillStyle(3004)

        canv.cd( ch2+1 )

        hh[ch1].SetLineColor(4)
        hh[ch1].SetLineColor(4)
        hh[ch1].SetLineStyle(3005)

        hh[ch1].Draw()
        hh[ch2].Draw("same")
        ll[ch2].Draw()
        dec[ch2].Draw()

    canv.Print("fig_ks_wrt_ch" + ch2str(ch1) + ".png")
