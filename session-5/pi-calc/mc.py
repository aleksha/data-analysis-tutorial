N = 10000000 
        
from ostap.histos.graphs import makeGraph, hToGraph, hToGraph2, hToGraph3, lw_graph
canvas.Close()

def int2name( number ):
    if number>0:
        if number<10:
            return ("0000000"+str(number))
        if number<100:
            return ("000000"+str(number))
        if number<1000:
            return ("00000"+str(number))
        if number<10000:
            return ("0000"+str(number))
        if number<100000:
            return ("000"+str(number))
        if number<1000000:
            return ("00"+str(number))
        if number<10000000:
            return ("0"+str(number))
    return str(number)

canv = ROOT.TCanvas("canv","canv",500,600)

rand1 = ROOT.TRandom3()
rand2 = ROOT.TRandom3()
rand1.SetSeed(187468734)
rand2.SetSeed(296587262)

arc = ROOT.TArc(0,0,1,0,90)
arc.SetLineColor(2)
arc.SetLineWidth(2)

x_in  = []
y_in  = []
x_out = []
y_out = []

n_in  = 0
n_out = 0

pi_num = 0

from math import sqrt

h_dummy = ROOT.TH2F("h_dummy",";;",100,0,1,120,0,1.2)
h_dummy.GetYaxis().SetRangeUser(0,1.2)

div=4
for ev in range(1,N):
    x = rand1.Rndm()    
    y = rand2.Rndm()
    if x**2+y**2<=1:
        n_in += 1
        x_in.append( x )
        y_in.append( y )
    else:
        n_out += 1
        x_out.append( x )
        y_out.append( y )
    pi_num = 4.*n_in/(n_in+n_out)
    if not ev%div :
        gr_in  = makeGraph(x_in, y_in)
        gr_out = makeGraph(x_out, y_out)
        gr_in.SetMarkerSize(0.5)
        gr_out.SetMarkerSize(0.5)
        gr_in.SetMarkerColor(2)
        gr_out.SetMarkerColor(1)
        gr_in.SetMarkerStyle(24)
        gr_out.SetMarkerStyle(24)
        h_dummy.Draw()
        gr_in.Draw("P same")
        gr_out.Draw("P same")
        lab = ROOT.TLatex(0.05,1.05,"#pi#approx"+"{0:5.4f}".format(pi_num)+"  N="+str(ev))
        arc.SetFillStyle(0)
        arc.Draw()
        lab.Draw()
        canv.Print("fig_"+int2name(ev)+".png")
        if ev<1000000:
            div*=2
        else:
            div=500000







