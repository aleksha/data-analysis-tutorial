
# Prepare dataset and datahist
rfile = ROOT.TFile("test_file.root","READ")
ds = rfile["ds_pi"]
im    = ROOT.RooRealVar( "im"   ,"im"   , 2.31, 2.33 )
im_kp = ROOT.RooRealVar( "im_kp","im_kp", 1.80, 2.10 )
my_cut  = "im>"       + str( im.getMin() )
my_cut += "&& im<"    + str( im.getMax() )
my_cut += "&& im_kp>" + str( im_kp.getMin() )
my_cut += "&& im_kp<" + str( im_kp.getMax() )
small_ds = ds.reduce( ROOT.RooArgSet( im_kp ), my_cut )
dh = small_ds.binnedClone()
# Prepare a composite model
import ostap.fitting.models as Models
sig_1 = Models.Apollonios2_pdf( 'sig_1', xvar=im_kp,
                                mean      = (1.87, 1.86, 1.88) ,
                                sigma     = (0.0045,0.003, 0.01) ,
                                asymmetry = (0,-0.1, 0.1)      ,
                                beta      = (1, 0.1, 50)       )
#
sig_2 = Models.Apollonios2_pdf( 'sig_2', xvar=im_kp,
                                mean      = (1.97, 1.96, 1.98) ,
                                sigma     = (0.0045,0.003, 0.01) ,
                                asymmetry = (0,-0.1, 0.1)      ,
                                beta      = (1, 0.1, 50)       )
#
sig_3 = Models.Apollonios2_pdf( 'sig_3', xvar=im_kp,
                                mean      = (1.995, 1.990, 2.005) ,
                                sigma     = (0.0045,0.003, 0.01) ,
                                asymmetry = (0,-0.1, 0.1)      ,
                                beta      = (1, 0.1, 50)       )
#
bkg   = Models.Bkg_pdf ( 'bkg' , xvar = im_kp , power = 1 )
model = Models.Fit1D   ( signal = sig_1 , background = bkg , 
        othersignals = [sig_2], otherbackgrounds = [sig_3],
        combine_signals = True, combine_backgrounds = True, extended = False )
# Fit
r, w = model.fitTo( dh , draw=True, silent=True)
r, w = model.fitTo( dh , draw=True, silent=True)
w.Draw()
canvas >> "TEMP"
