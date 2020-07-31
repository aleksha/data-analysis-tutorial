#-------------------------------------------------------------------------------
import ostap.fitting.models as Models
from   ostap.histos.histos  import h1_axis
from math import log, sqrt, pi, exp
from ostap.histos.graphs import *
#-------------------------------------------------------------------------------
x  = ROOT.RooRealVar ('x'  , 'x'     , -100 , 100 )
pk = ROOT.RooRealVar ('pk' , 'peak'  , 0   )
sg = ROOT.RooRealVar ('sg' , 'sigma' , 1.5 )
sm = ROOT.RooRealVar ('sm' , 'sigma' , 1.5, 0.001, 10 )
#-------------------------------------------------------------------------------
sig = Models.Gauss_pdf( 'signal', xvar=x,  mean=pk, sigma=sg )
smm = Models.Gauss_pdf( 'signal', xvar=x,  mean=pk, sigma=sm )
#-------------------------------------------------------------------------------
data = sig.generate(25)
print(data)
#-------------------------------------------------------------------------------
#for event in data:
#    print( "--> " + str(event.x) + "\t" + str( event.x.value ) + "\t" + str(event.x.error ) )
#-------------------------------------------------------------------------------
def gauss(x, mean, sigma):
    return exp( -0.5*pow( (x-mean)/sigma,2 ) ) / (sigma*sqrt(2*pi))
#
def nll( dat , mean, sigma) :
    ll = 0.
    for d in dat:
        ll += log( gauss(d.x.value, mean, sigma) )
    return -2.*ll;
#-------------------------------------------------------------------------------
s_list = []
nll_list = []
for i in range(30):
    s = 0.4 + 0.1*(i+2)
    s_list.append(s)
    nll_list.append( nll(data,0,s) )
#-------------------------------------------------------------------------------
canv = ROOT.TCanvas("canv","my_canvas",800,800)
#-------------------------------------------------------------------------------
gr = makeGraph( s_list, nll_list)
gr.SetMarkerStyle(20)
gr.SetMarkerSize(2)
#gr.GetYaxis().SetRangeUser(-1.2,1.5)
gr.GetYaxis().SetTitle("#minus2log(L)")
gr.GetXaxis().SetTitle("#sigma")
gr.GetXaxis().SetTitleOffset( 1.4) ; gr.GetYaxis().SetTitleOffset( 1.1)
gr.GetXaxis().SetTitleSize(  0.04) ; gr.GetYaxis().SetTitleSize(  0.04)
gr.GetXaxis().CenterTitle()        ; gr.GetYaxis().CenterTitle()
gr.Draw("APL");
canv.Print( "TEMP.png" )
#===============================================================================
r,w = smm.fitTo( data, draw=True )
w.GetXaxis().SetRangeUser(-5,5)
w.Draw()
print(r)
canv.Print( "FITT.png" )
canv.Close()
