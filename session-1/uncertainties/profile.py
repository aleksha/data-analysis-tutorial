
# Prepare dataset and datahist
# Prepare a composite model
import ostap.fitting.models as Models
x = ROOT.RooRealVar("x","x",-12,12)
#
sig = Models.Gauss_pdf( 'sig', xvar=x,
                              mean      = (0, -1, 1) ,
                              sigma     = (1,0.001, 3.) )
#
bkg = Models.Gauss_pdf( 'bkg', xvar=x,
                              mean      = (0, -1, 1) ,
                              sigma     = (4,3.5, 10.) )
#
model = Models.Fit1D   ( signal = sig , background = bkg , extended = False )
#
ds = sig.generate(100)
ds = ds + bkg.generate(150)
# Fit
r, w = model.fitTo( ds , draw=True, silent=True)
print(r)
w.Draw()
canvas >> "TEMP"
nll , f1 = model.draw_nll ( 'sigma_sig' ,  ds )
f1.Draw()
canvas >> "TEMP"
nllp , f2 = model.draw_nll ( 'sigma_sig' ,  ds, profile = True )
f1.Draw()
f2.Draw("same")
canvas >> "TEMP"
