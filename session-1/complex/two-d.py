
# Prepare dataset and datahist
rfile = ROOT.TFile("test_file.root","READ")
ds = rfile["ds_pi"]
im  = ROOT.RooRealVar( "im" ,"im" , 2.24, 2.33 )
m12 = ROOT.RooRealVar( "m12","m12", 1.47, 1.57 )
my_cut  = "im>"       + str( im.getMin() )
my_cut += "&& im<"    + str( im.getMax() )
my_cut += "&& m12>" + str( m12.getMin() )
my_cut += "&& m12<" + str( m12.getMax() )
small_ds = ds.reduce( ROOT.RooArgSet( im,m12 ), my_cut )
# Prepare a composite model
import ostap.fitting.models as Models
sig_x = Models.Apollonios2_pdf( 'sig_x', xvar=im,
                                mean      = (2.288, 2.287, 2.289) ,
                                sigma     = (0.0045,0.003, 0.01) ,
                                asymmetry = (0,-0.1, 0.1)      ,
                                beta      = (1, 0.1, 50)       )
#
sig_y = Models.Gauss_pdf( 'sig_y', xvar=m12,
                                mean      = (1.517, 1.513, 1.521) ,
                                sigma     = (0.0045,0.003, 0.01) )
#
bkg_1x   = Models.Bkg_pdf ( 'bkg_1x' , xvar = im , power = 0 )
bkg_1y   = Models.Bkg_pdf ( 'bkg_1y' , xvar = m12, power = 1 )
bkg_2x   = Models.Bkg_pdf ( 'bkg_2x' , xvar = im , power = 0 )
bkg_2y   = Models.Bkg_pdf ( 'bkg_2y' , xvar = m12, power = 1 )
model_x = Models.Fit1D   ( signal = sig_x , background = bkg_1x)
model_y = Models.Fit1D   ( signal = sig_y , background = bkg_1y)

#help(Models.Fit2D)
# |  Arguments:
# |
# |  - signal_x        : PDF for the S(x)-signal component
# |  - signal_y        : PDF for the S(y)-signal component
# |  - suffix          : the suffix to be used for the PDF and variable names
# |  - bkg_1x          : x-background component for B(x)*S(y) term
# |  - bkg_1y          : y-background component for S(x)*B(y) term
# |  - bkg_2x          : x-background component for B(x)*B(y) term, if bkg2D is not specified
# |  - bkg_2y          : y-background component for B(x)*B(y) term, if bkg2D is not specified
# |  - bkg_2D          : PDF for 2D-background component for B(x,y)    term
# |  - sig_2D          : PDF for 2D-signal component S(x,y) term
# |  - ss              : the yield of  S(x,y)    component
# |  - sb              : the yield of  S(x)*B(y) component
# |  - bs              : the yield of  B(x)*S(y) component
# |  - bb              : the yield of  B(x,y)    component
# |  - components      : the list of other 2D-components
# |  - xvar            : the x-variable
# |  - yvar            : the y-variable
# |  - name            : the name of PDF
model_xy = Models.Fit2D( signal_x = sig_x , signal_y = sig_y ,
                         bkg_1x = bkg_1x , bkg_1y = bkg_1y, bkg_2x=bkg_2x, bkg_2y=bkg_2y)
small_dh = ( small_ds.reduce( ROOT.RooArgSet( im ,m12 ) , "im>0" ) ).binnedClone()

# Fit
#r, w = model_x.fitTo( small_ds , draw=True, silent=True)
#r, w = model_y.fitTo( small_ds , draw=True, silent=True)
r, w = model_xy.fitTo( small_dh , draw=True, silent=True)
r, w = model_xy.fitTo( small_ds , draw=True, silent=True)

fx  = model_xy.draw1 ( small_ds , nbins = 90 )
fx.Draw()
canvas >> "TEMP"
fy  = model_xy.draw2 ( small_ds , nbins = 50  )
fy.Draw()
canvas >> "TEMPy"
print(r)
