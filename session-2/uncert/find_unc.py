import ROOT
import ostap.fixes.fixes
from ostap.core.core import cpp, Ostap
from ostap.core.core import pwd, cwd, ROOTCWD
from ostap.core.core import rootID, funcID, funID, fID, histoID, hID, dsID
from ostap.core.core import VE
from ostap.histos.histos import h1_axis, h2_axes, h3_axes
from ostap.histos.graphs import makeGraph, hToGraph, hToGraph2, hToGraph3, lw_graph
import ostap.trees.trees
import ostap.trees.cuts
import ostap.histos.param
import ostap.histos.compare
import ostap.io.root_file
import ostap.math.models
import ostap.fitting.roofit
import ostap.fitting.models as Models

from statistics import mean, stdev

x = []; y = [];
with open("Book1.txt","r") as f:
    for line in f:
        w = line.split("\t")
        x.append(float(w[0]))
        y.append(float(w[7]))

gr = makeGraph(x,y)
gr.SetMarkerStyle(24)
#gr.Draw("AP")

N = len(x)
chunk_size = 20

def fit(xx,yy,order=2):
    gg = makeGraph(xx,yy)
    ff = ROOT.TF1("ff","pol"+str(order),min(xx)-0.1,max(xx)+0.1)
#    rr = gg.Fit(ff,"SQ")
    rr = gg.Fit(ff,"S")
    hh = []
    for i in range(len(xx)):
        hh.append( (ff.Eval(xx[i])-yy[i])/ ff.Eval( xx[i] ) )
    rel_sigma = stdev(hh)
    return rel_sigma

window = 3

ey = []; ex = []; er = []
for i in range(window):
    ex.append(0.)
    ey.append(0.)

for chan in range(window,len(x)-window):
    xx = []; yy = []
    for offset in range(-window,window+1):
        xx.append(x[ chan + offset ])
        yy.append(y[ chan + offset ])
    ex.append(0.)
    rel_err = fit(xx,yy)
    ey.append( rel_err*y[chan] )
    er.append( rel_err )

for i in range(window):
    ex.append(0.)
    ey.append(0.)

g_err = makeGraph(x,y,ex,ey)
g_err.Draw("AP")

hist = ROOT.TH1F("hist","hist",24*5,0,1)
for h in er:
    hist.Fill(h)


#hist.Draw()

