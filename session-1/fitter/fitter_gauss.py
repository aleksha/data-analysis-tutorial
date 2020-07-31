#-------------------------------------------------------------------------------
import ostap.fitting.models as Models
from   ostap.utils.timing import timing
from   ostap.histos.histos  import h1_axis
from Functions import *
#-------------------------------------------------------------------------------
rfile = ROOT.TFile("test_file.root","READ")
#ds = rfile["ds_pi"]
ds    = rfile["ds_k"]
#-------------------------------------------------------------------------------
im = ROOT.RooRealVar ('im'   , 'im'                 ,  2.240 , 2.330 )
pk = ROOT.RooRealVar ('pk'   , 'peak   '   , 2.2875 ,  2.286 , 2.289 )
sg = ROOT.RooRealVar ('sg'   , 'sigma'     , 0.0045 ,  0.003 , 0.010 )
#-------------------------------------------------------------------------------
sig_ga = Models.Gauss_pdf( 'sig_ga', xvar=im,   mean=pk, sigma=sg )
bkg0 = Models.Bkg_pdf ( 'bkg0' , xvar = im , power = 0 )
#-------------------------------------------------------------------------------
model= Models.Fit1D   ( signal = sig_ga , background = bkg0 )
#-------------------------------------------------------------------------------
dh = ( ds.reduce( ROOT.RooArgSet( im ) , "im>0" ) ).binnedClone()
#-------------------------------------------------------------------------------
with timing():
    r, w = model.fitTo( dh , draw=True , silent=True)
#    r, w = model.fitTo(ds, draw=True, nbins=100, ncpu=1)
#-------------------------------------------------------------------------------
print(r)
#-------------------------------------------------------------------------------
#h = w.pullHist()
#draw_param( r, w, h, 90, im, 0.06*ds.sumEntries(), name="Lc", XTitle ="Mass",
#                Prefix="Gauss" , Type="png", var_Units = "GeV/c^{2}")
#-------------------------------------------------------------------------------
