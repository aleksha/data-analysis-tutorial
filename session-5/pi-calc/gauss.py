N = 10000
M = 5000
        
from ostap.histos.graphs import makeGraph, hToGraph, hToGraph2, hToGraph3, lw_graph
canvas.Close()
from math import sqrt

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
hist = ROOT.TH1F("hist","#hat{#pi};Entries",200,3.14-0.50,3.14+0.50)

rand1 = ROOT.TRandom3()
rand2 = ROOT.TRandom3()
rand1.SetSeed(62575834)
rand2.SetSeed(34203456)

div=2
#ROOT.gPad.SetLogy()

for toy in range(1,N+1):
    x_in  = []
    y_in  = []
    x_out = []
    y_out = []

    n_in  = 0
    n_out = 0

    pi_num = 0.
    for ev in range(M):
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
    hist.Fill(pi_num)
    if not toy%div :
        hist.Draw()
        hm = hist.GetMaximum()
        ll1 = ROOT.TLatex(3.24,hm*0.9,"N="+str(toy))
        ll1.SetTextSize(0.04)
        ll1.Draw()
        ll2 = ROOT.TLatex(3.24,hm*0.8,"#pi in "+"{0:5.4f}".format(hist.mean().value())+" #pm "+"{0:5.4f}".format(2.*hist.mean().error()))
        ll2.SetTextSize(0.035)
        ll2.Draw()
        ll3 = ROOT.TLatex(3.24,hm*0.75,"   CL=0.95")
        ll3.SetTextSize(0.035)
        ll3.Draw()
        if toy>1000:
            div=500
        else:
            div*=2
        canv.Print("fig_"+int2name(toy)+".png")


toy=N+1
canv.Print("fig_"+int2name(toy)+".png")

toy+=1
ROOT.gPad.SetLogy(0)
canv.Print("fig_"+int2name(toy)+".png")

toy+=1
tf1 = ROOT.TF1("tf1","gaus(0)",3.14-0.50,3.14+0.50)
tf1.SetLineColor(2)
tf1.SetLineWidth(3)
r = hist.Fit("tf1","S")
canv.Print("fig_"+int2name(toy)+".png")

for i in range(10):
    toy+=1
    canv.Print("fig_"+int2name(toy)+".png")