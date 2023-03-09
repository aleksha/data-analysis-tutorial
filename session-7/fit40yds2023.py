#-------------------------------------------------------------------------------
import ostap.fitting.models as Models
from   ostap.histos.histos  import h1_axis
#-------------------------------------------------------------------------------
im = ROOT.RooRealVar ('im'   , 'im'                 , -0.150 , 0.150 )
pk = ROOT.RooRealVar ('pk'   , 'peak   '    , 0.028 ,  0.000 , 0.050 )
sg = ROOT.RooRealVar ('sg'   , 'sigma rand' , 0.004 ,  0.000 , 0.100 )
sf = ROOT.RooRealVar ('sf'   , 'sigma shift', 0.005 ,  0.001 , 0.070 )
#-------------------------------------------------------------------------------
sig_ga = Models.Gauss_pdf( 'sig_ga', xvar=im,  mean=pk, sigma=sg)
#
#-------------------------------------------------------------------------------
#
if __name__=="__main__":
    #-------------------------------------------------------------------------------
    model = sig_ga
    #-------------------------------------------------------------------------------
    arg_set = ROOT.RooArgSet( im )
    ds = ROOT.RooDataSet( "ds", "ds", arg_set )
#    with open("WR2023-40yds.txt","r") as f:
    with open("RB2023-40yds.txt","r") as f:
        for line in f:
            if len(line)>5:
                w = line[:-1].split(",")
                im.setVal( float(w[2]) - float(w[1]) )
                ds.add( arg_set )
    #-------------------------------------------------------------------------------
    r, w = model.fitTo(ds, draw=True, nbins=18, ncpu=4)
    #-------------------------------------------------------------------------------
    print(r)
    #-------------------------------------------------------------------------------
    toy_ds = []
    for i in range(1000):
        pars = r.randomizePars()
        sig_gen = Models.Gauss_pdf( 'sig_gen', xvar=im, mean=pars[0].value, sigma=pars[1].value )
        toy_ds.append( sig_gen.generate(39) )

    nll_hist = ROOT.TH1F("nll_hist"," ",160,-80, 0)
    nll_list = []
    for dst in toy_ds:
        rt, wt = model.fitTo(dst, draw=False, silent=True )
        nll_list.append( rt.minNll() )
        nll_hist.Fill( rt.minNll() )
    nll_hist.Draw("hist")
    line = ROOT.TArrow(r.minNll(),60,r.minNll(),0)
    line.Draw()
