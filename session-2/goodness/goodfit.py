
# Prepare dataset and datahist
# Prepare a composite model
import ostap.fitting.models as Models
from   ostap.utils.progress_bar import progress_bar
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
nll_obs = r.minNll()
#help(r)
print(r)
print(r("mean_sig"))
w.Draw()
canvas >> "MAIN"
#
Ntoys = 1000
toy_ds_list = []
for toy in range(Ntoys):
    toy_ds_list.append( model.generate(250) )
#
nll_list = []
less = 0.
more = 0.
for toy in progress_bar( range(Ntoys) ):
    r, w = model.fitTo( toy_ds_list[toy] , draw=True, silent=True)
    nll_list.append( r.minNll() )
    if r.minNll()<nll_obs:
        less += 1.
    else:
        more += 1.
#
w.Draw()
canvas >> "TEMP"
#
print("Less: " + str(100.*less/Ntoys) + " %")
print("More: " + str(100.*more/Ntoys) + " %")
