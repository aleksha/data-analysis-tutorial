
# --- Prepare dataset
rfile = ROOT.TFile("test_file.root","READ")
ds = rfile["ds_k"]
im  = ROOT.RooRealVar( "im"    ,"im"  , 2.240, 2.330 )
m23 = ROOT.RooRealVar( "m23"   ,"m23" , 1.006, 1.065 )
phi_ds = ds.reduce( ROOT.RooArgSet( im, m23 ), "im>2.24 && im<2.33 && m23>1.006 && m23<1.065" )
#--- Prepare a composite model
import ostap.fitting.models as Models
sig = Models.Voigt_pdf( "sig", xvar=m23, m0=(1.02,1.015,1.025)      ,
                                       gamma=(0.0042,0.0004,0.0044) ,
                                       sigma=(0.001,0.0001,0.003)  )
bkg = Models.PS2_pdf("bkg",xvar=m23, m1 = 0.493272, m2=0.493272 )

bw = Ostap.Math.BreitWigner( 1.019 , 0.0042 , 0.493272 , 0.493272 , 1 )
breit = Models.BreitWigner_pdf ( 'BW' , bw, xvar=m23, m0 = (1.019,1.016,1.022),  gamma = 0.0042   )

reso = ROOT.RooRealVar("reso","reso",0.001,0.0001,0.003)
cnv_pdf = Models.Convolution_pdf ( pdf = breit , xvar=m23, resolution = reso , useFFT = True )
model1 = Models.Fit1D ( signal = sig , background = bkg )
model2 = Models.Fit1D ( signal = breit , background = bkg )
model3 = Models.Fit1D ( signal = cnv_pdf , background = bkg )

# ---- Fit and Draw
r,w = model3.fitTo(phi_ds,draw=True,silent=True)
canv = ROOT.TCanvas("canv","canv",900,900)
ROOT.gPad.SetLogy()
w.Draw()
canv.Print("TEMP.png")

