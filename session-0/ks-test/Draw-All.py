canvas.Close()

import numpy as np
import scipy.stats as stats
import statistics as py_stat

E = []
for ch in range(1,17):
    energy = []
    if ch<10:
        file_name = "data/20210218-ch0" + str(ch) + ".e.txt"
    else:
        file_name = "data/20210218-ch"  + str(ch) + ".e.txt"
    with open(file_name,"r") as fl:
        for line in fl:
            energy.append(float(line))

    E.append( np.array(energy) )

def proj2hist( sample , tname, bins = 100, low = 163, high = 173):
    hist = ROOT.TH1F(tname,tname+";E, a.u.;N",bins,low,high)
    for ev in sample:
        hist.Fill( ev )
    return hist

for i in range( 16 ):
    ss = "ch.: "
    if i<10:
        ss += "0"
    ss += str(i) + "  "
    ss += "min/max: " + str( min( E[i] ) ) + "/" + str( max( E[i] ) ) + "  "
    ss += "mean: " + str( py_stat.mean( E[i] ) ) + "  "
    ss += "rms: " + str( py_stat.stdev( E[i] ) )
    print( ss )

canv = ROOT.TCanvas("canv","canv",1100,1100)
canv.Divide(4,4)
hh = []
ll = []
for i in range( 16 ):
    hh.append( proj2hist( E[i], tname = "h_"+str(i), bins = 230, low=150, high=173 ) )
    canv.cd(i+1)
    hh[i].GetYaxis().SetRangeUser(0,100)
    hh[i].Draw("hist")
    ll.append( ROOT.TLatex(153,90,"ch.: "+str(i)) )
    ll[i].Draw()

canv.Print("fig_raw.png")
