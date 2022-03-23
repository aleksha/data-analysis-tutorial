#-------------------------------------------------------------------------------
import ostap.fitting.models as Models
from   ostap.utils.timing import timing
from   ostap.histos.histos  import h1_axis
from Functions import *
#-------------------------------------------------------------------------------
rfile = ROOT.TFile("test_file.root","READ")
ds = rfile["ds_k"]
#-------------------------------------------------------------------------------
im = ROOT.RooRealVar ('im'   , 'im'                 ,  2.240 , 2.330 )
pk = ROOT.RooRealVar ('pk'   , 'peak   '   , 2.2875 ,  2.286 , 2.289 )
sg = ROOT.RooRealVar ('sg'   , 'sigma'     , 0.0045 ,  0.003 , 0.010 )
rl = ROOT.RooRealVar ('rl' , 'rhoL'        , 0.0000 ,  0.000 , 2.000 )
rr = ROOT.RooRealVar ('rr' , 'rhoR'        , 0.0000 ,  0.000 , 2.000 )
xi = ROOT.RooRealVar ('xi' , 'xi'          , 0.0000 , -0.010 , 0.010 )
#-------------------------------------------------------------------------------
sig_bu = Models.Bukin_pdf( 'sig_bu', xvar=im, mean=pk, sigma=sg, xi=xi,
                            rhoL=rl, rhoR=rr)
bkg0   = Models.Bkg_pdf ( 'bkg0' , xvar = im , power = 0 )
model  = Models.Fit1D   ( signal = sig_bu , background = bkg0 )
#-------------------------------------------------------------------------------
dh = ( ds.reduce( ROOT.RooArgSet( im ) , "im>0" ) ).binnedClone()
with timing():
    r, w = model.fitTo( dh, draw=True )
#    r, w = model.fitTo(ds, draw=True, nbins=100, ncpu=4)
#-------------------------------------------------------------------------------
print(r)
#-------------------------------------------------------------------------------
h = w.pullHist()
draw_param( r, w, h, 90, im, 0.06*ds.sumEntries(), name="Lc", XTitle ="Mass",
                Prefix="Bukin" , Type="png", var_Units = "GeV/c^{2}")
#-------------------------------------------------------------------------------
