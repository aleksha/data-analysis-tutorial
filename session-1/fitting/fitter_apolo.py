#-------------------------------------------------------------------------------
import ostap.fitting.models as Models
from   ostap.utils.timing import timing
from   ostap.histos.histos  import h1_axis
from Functions import *
#-------------------------------------------------------------------------------
im = ROOT.RooRealVar ('im'   , 'im'                 ,  2.240 , 2.330 )
pk = ROOT.RooRealVar ('pk'   , 'peak   '   , 2.2875 ,  2.287 , 2.288 )
sg = ROOT.RooRealVar ('sg'   , 'sigma'     , 0.0045 ,  0.003 , 0.070 )
am = ROOT.RooRealVar ('am'   , 'asymmetry' , 0.0000 , -0.300 , 0.300 )
bt = ROOT.RooRealVar ('bt'   , 'beta'      , 1.0000 ,  0.500 , 9.999 )
#-------------------------------------------------------------------------------
sig_ap = Models.Apollonios2_pdf( 'sig_ap', xvar=im,   mean=pk, sigma=sg, asymmetry=am, beta=bt)
bkg0  = Models.Bkg_pdf ( 'bkg0' , xvar = im , power = 0 )
#
#-------------------------------------------------------------------------------
#
if __name__=="__main__":
    #-------------------------------------------------------------------------------
    model = Models.Fit1D   ( signal = sig_ap , background = bkg0 )
    #-------------------------------------------------------------------------------
    rfile = ROOT.TFile("test_file.root","READ")
    ds = rfile["ds_pi"]
    dh = ( ds.reduce( ROOT.RooArgSet( im ) , "im>0" ) ).binnedClone()
    with timing():
        r, w = model.fitTo( dh , draw=True, silent=True)
        r, w = model.fitTo( dh , draw=True, silent=True)
#        r, w = model.fitTo(ds, draw=True, nbins=100, ncpu=4)
    #-------------------------------------------------------------------------------
    print(r)
    #-------------------------------------------------------------------------------
    h = w.pullHist()
    draw_param( r, w, h, 90, im, 0.06*ds.sumEntries(), name="Lc", XTitle ="Mass",
                    Prefix="Apolo2" , Type="png", var_Units = "GeV/c^{2}")
    #-------------------------------------------------------------------------------
