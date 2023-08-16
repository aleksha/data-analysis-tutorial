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

x=[]; y=[]
with open("data.txt") as fl:
    for line in fl:
        w = line[:-1].split(" ")
        x.append( VE( float(w[0]), 0           ) )
        y.append( VE( float(w[1]), float(w[1]) ) )
gr = makeGraph(x,y)
gr.SetMarkerStyle(20)
gr.GetYaxis().SetRangeUser(0,450)
gr.Draw("AP")
r = gr.Fit("pol2","S")
print(r)

x1=[]; y1=[]
for i in range(len(x)):
    if i not in [41,42,43]:
        x1.append(x[i])
        y1.append(y[i])
gr1 = makeGraph(x1,y1)
gr1.SetMarkerStyle(24)
gr1.GetYaxis().SetRangeUser(0,450)
gr1.Draw("AP")
r = gr1.Fit("pol2","S")
print(r)


tf1 = ROOT.TF1("tf1","gaus(0)+pol2(3)",3700,4000)
tf1.FixParameter(1,3874)
tf1.FixParameter(2,9./2.35)
rg = gr.Fit(tf1,"S")
print(rg)
gr.Draw("AP")


bins = []
for i in range(56):
    bins.append(3704.+i*4.)
h = h1_axis(bins)
for i in range(len(y)):
    h[i+1]=y[i]
h.Draw()
gr.SetLineColor(4)
gr.Draw("same")
h.SetMinimum(0)


im = ROOT.RooRealVar ('im'   , 'im'    ,  3700. , 4000. )
pk = ROOT.RooRealVar ('pk'   , 'peak'  , 3874.)
sg = ROOT.RooRealVar ('sg'   , 'sigma' ,  9./2.35)
#-------------------------------------------------------------------------------
sig_ga = Models.Gauss_pdf( 'sig_ga', xvar=im,   mean=pk, sigma=sg )
bkg0 = Models.PolyPos_pdf ( 'bkg0' , xvar = im , power = 2 )
#-------------------------------------------------------------------------------
model= Models.Fit1D   ( signal = sig_ga , background = bkg0 )
#-------------------------------------------------------------------------------
ro,wo = model.fitHisto(h, draw=True,silent=True,sumw2=True)
ro,wo = model.fitHisto(h, draw=True,silent=True,sumw2=True)
ro,wo = model.fitHisto(h, draw=True,silent=True,sumw2=True)
print(ro.minNll())
print(wo.chiSquare(4))
print(wo.chiSquare(4)*(55-4))
print(122.4231/37.8788 )
print(ro)
wo.Draw()


rn,wn = bkg0.fitHisto(h, draw=True,silent=True,sumw2=True)
print(rn.minNll())
print(wn.chiSquare(2))
print(wn.chiSquare(2)*(55-2))
print(rn)
wn.Draw()

rn,wn = bkg0.fitTo(h, draw=True,silent=True,sumw2=True,nbins=55)
wn.Draw()

# ds = bkg0.histo_data
#rr,ww = model.fitTo ( ds , sumw2 = True , nbins = 55, draw = True) 
#ww.Draw()

