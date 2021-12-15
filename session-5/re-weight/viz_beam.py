import ROOT, time, numpy
from   ostap.core.core      import Ostap, std, VE, dsID
from   ostap.logger.utils   import rooSilent
import ostap.io.zipshelve   as     DBASE
from   ostap.utils.timing   import timing
from   ostap.histos.graphs  import makeGraph
from   ostap.histos.histos  import h1_axis, h2_axes
from   hep_ml.reweight      import GBReweighter
#===============================================================================
rfile = ROOT.TFile("beamfile_prm_mu100.root", "READ")
rfile.ls()
tree = rfile["BeamFile"]
print( "Entries: " + str( len( tree ) ) )
# tree.X, tree.Y, tree.dXdZ, tree.dYdZ, tree.P, particleFlag
#===============================================================================
h1X   = ROOT.TH1F( "h1X"  , "h1X;X, mm;Entries",  160, -40,  40 )
h1Y   = ROOT.TH1F( "h1Y"  , "h1Y;Y, mm;Entries",  160, -40,  40 )
h1x   = ROOT.TH1F( "h1x"  , "h1x;dXdZ, mrad;Entries",  300,  -3,   3 )
h1y   = ROOT.TH1F( "h1y"  , "h1y;dYdZ, mrad;Entries",  300,  -3,   3 )
h1P   = ROOT.TH1F( "h1P"  , "h1P;p, GeV/c;Entries",  300,  85, 115 )
h2XY  = ROOT.TH2F( "h2XY" , "h2XY;X, mm;Y, mm", 160, -40,  40,  160, -40,  40 )
h2Xx  = ROOT.TH2F( "h2Xx" , "h2Xx;X, mm;dXdZ, mrad", 160, -40,  40,  300,  -3,   3 )
h2Xy  = ROOT.TH2F( "h2Xy" , "h2Xy;X, mm;dYdZ, mrad", 160, -40,  40,  300,  -3,   3 )
h2XP  = ROOT.TH2F( "h2XP" , "h2XP;X, mm;p, GeV/c", 160, -40,  40,  300,  85, 115 )
h2Yx  = ROOT.TH2F( "h2Yx" , "h2Yx;Y, mm;dXdZ, mrad", 160, -40,  40,  300,  -3,   3 )
h2Yy  = ROOT.TH2F( "h2Yy" , "h2Yy;Y, mm;dYdZ, mrad", 160, -40,  40,  300,  -3,   3 )
h2YP  = ROOT.TH2F( "h2YP" , "h2YP;Y, mm;p, GeV/c", 160, -40,  40,  300,  85, 115 )
h2xy  = ROOT.TH2F( "h2xy" , "h2xy;dXdZ, mrad;dYdZ, mrad", 300,  -3,   3,  300,  -3,   3 )
h2xP  = ROOT.TH2F( "h2xP" , "h2xP;dXdZ, mrad;p, GeV/c", 300,  -3,   3,  300,  85, 115 )
h2yP  = ROOT.TH2F( "h2yP" , "h2yP;dYdZ, mrad;p, GeV/c", 300,  -3,   3,  300,  85, 115 )
h3XYP = ROOT.TH3F( "h3XYP" , "h3XYP;X, mm;Y, mm;p GeV/c", 160, -40,  40,  160, -40,  40, 300,  85, 115 )

hr1X   = ROOT.TH1F( "hr1X"  , "h1X;X, mm;Entries",  160, -40,  40 )
hr1Y   = ROOT.TH1F( "hr1Y"  , "h1Y;Y, mm;Entries",  160, -40,  40 )
hr1x   = ROOT.TH1F( "hr1x"  , "h1x;dXdZ, mrad;Entries",  300,  -3,   3 )
hr1y   = ROOT.TH1F( "hr1y"  , "h1y;dYdZ, mrad;Entries",  300,  -3,   3 )
hr1P   = ROOT.TH1F( "hr1P"  , "h1P;p, GeV/c;Entries",  300,  85, 115 )
hr2XY  = ROOT.TH2F( "hr2XY" , "h2XY;X, mm;Y, mm", 160, -40,  40,  160, -40,  40 )
hr2Xx  = ROOT.TH2F( "hr2Xx" , "h2Xx;X, mm;dXdZ, mrad", 160, -40,  40,  300,  -3,   3 )
hr2Xy  = ROOT.TH2F( "hr2Xy" , "h2Xy;X, mm;dYdZ, mrad", 160, -40,  40,  300,  -3,   3 )
hr2XP  = ROOT.TH2F( "hr2XP" , "h2XP;X, mm;p, GeV/c", 160, -40,  40,  300,  85, 115 )
hr2Yx  = ROOT.TH2F( "hr2Yx" , "h2Yx;Y, mm;dXdZ, mrad", 160, -40,  40,  300,  -3,   3 )
hr2Yy  = ROOT.TH2F( "hr2Yy" , "h2Yy;Y, mm;dYdZ, mrad", 160, -40,  40,  300,  -3,   3 )
hr2YP  = ROOT.TH2F( "hr2YP" , "h2YP;Y, mm;p, GeV/c", 160, -40,  40,  300,  85, 115 )
hr2xy  = ROOT.TH2F( "hr2xy" , "h2xy;dXdZ, mrad;dYdZ, mrad", 300,  -3,   3,  300,  -3,   3 )
hr2xP  = ROOT.TH2F( "hr2xP" , "h2xP;dXdZ, mrad;p, GeV/c", 300,  -3,   3,  300,  85, 115 )
hr2yP  = ROOT.TH2F( "hr2yP" , "h2yP;dYdZ, mrad;p, GeV/c", 300,  -3,   3,  300,  85, 115 )
hr3XYP = ROOT.TH3F( "hr3XYP" , "h3XYP;X, mm;Y, mm;p GeV/c", 160, -40,  40,  160, -40,  40, 300,  85, 115 )

hi1X = ROOT.TH1F( "hi1X", "h1X;X, mm;Entries",  160, -40,  40 )
hi1Y = ROOT.TH1F( "hi1Y", "h1Y;Y, mm;Entries",  160, -40,  40 )
hi1x = ROOT.TH1F( "hi1x", "h1x;dXdZ, mrad;Entries",  300,  -3,   3 )
hi1y = ROOT.TH1F( "hi1y", "h1y;dYdZ, mrad;Entries",  300,  -3,   3 )
hi1P = ROOT.TH1F( "hi1P", "h1P;p, GeV/c;Entries",  300,  85, 115 )
hi2XY = ROOT.TH2F( "hi2XY" , "h2XY;X, mm;Y, mm", 160, -40,  40,  160, -40,  40 )
hi2Xx = ROOT.TH2F( "hi2Xx" , "h2Xx;X, mm;dXdZ, mrad", 160, -40,  40,  300,  -3,   3 )
hi2Xy = ROOT.TH2F( "hi2Xy" , "h2Xy;X, mm;dYdZ, mrad", 160, -40,  40,  300,  -3,   3 )
hi2XP = ROOT.TH2F( "hi2XP" , "h2XP;X, mm;p, GeV/c", 160, -40,  40,  300,  85, 115 )
hi2Yx = ROOT.TH2F( "hi2Yx" , "h2Yx;Y, mm;dXdZ, mrad", 160, -40,  40,  300,  -3,   3 )
hi2Yy = ROOT.TH2F( "hi2Yy" , "h2Yy;Y, mm;dYdZ, mrad", 160, -40,  40,  300,  -3,   3 )
hi2YP = ROOT.TH2F( "hi2YP" , "h2YP;Y, mm;p, GeV/c", 160, -40,  40,  300,  85, 115 )
hi2xy = ROOT.TH2F( "hi2xy" , "h2xy;dXdZ, mrad;dYdZ, mrad", 300,  -3,   3,  300,  -3,   3 )
hi2xP = ROOT.TH2F( "hi2xP" , "h2xP;dXdZ, mrad;p, GeV/c", 300,  -3,   3,  300,  85, 115 )
hi2yP = ROOT.TH2F( "hi2yP" , "h2yP;dYdZ, mrad;p, GeV/c", 300,  -3,   3,  300,  85, 115 )
hi3XYP = ROOT.TH3F( "hi3XYP" , "h3XYP;X, mm;Y, mm;p GeV/c", 160, -40,  40,  160, -40,  40, 300,  85, 115 )

cntr = 0
data_list = []
w_list    = []
mc_list   = []
for ev in tree:
    if ev.particleFlag==2 :
        cntr +=1
        h1X.Fill( ev.X    )
        h1Y.Fill( ev.Y    )
        h1x.Fill( ev.dXdZ )
        h1y.Fill( ev.dYdZ )
        h1P.Fill( ev.P    )

        h2XY.Fill( ev.X    , ev.Y    )
        h2Xx.Fill( ev.X    , ev.dXdZ )
        h2Xy.Fill( ev.X    , ev.dYdZ )
        h2XP.Fill( ev.X    , ev.P    )

        h2Yx.Fill( ev.Y    , ev.dXdZ )
        h2Yy.Fill( ev.Y    , ev.dYdZ )
        h2YP.Fill( ev.Y    , ev.P    )

        h2xy.Fill( ev.dXdZ , ev.dYdZ )
        h2xP.Fill( ev.dXdZ , ev.P    )

        h2yP.Fill( ev.dYdZ , ev.P    )

        h3XYP.Fill( ev.X , ev.Y , ev.P )
        data_list.append( [ev.X, ev.Y , ev.dXdZ, ev.dYdZ, ev.P] )
        w_list.append( 1. )

for i in range(cntr):
    mc_list.append( [ h1X.GetRandom(), h1Y.GetRandom(), h1x.GetRandom(), h1y.GetRandom(), h1P.GetRandom() ] )

for ev in mc_list:
    hi1X.Fill( ev[0] )
    hi1Y.Fill( ev[1] )
    hi1x.Fill( ev[2] )
    hi1y.Fill( ev[3] )
    hi1P.Fill( ev[4] )
    hi2XY.Fill( ev[0] , ev[1] )
    hi2Xx.Fill( ev[0] , ev[2] )
    hi2Xy.Fill( ev[0] , ev[3] )
    hi2XP.Fill( ev[0] , ev[4] )
    hi2Yx.Fill( ev[1] , ev[2] )
    hi2Yy.Fill( ev[1] , ev[3] )
    hi2YP.Fill( ev[1] , ev[4] )
    hi2xy.Fill( ev[2] , ev[3] )
    hi2xP.Fill( ev[2] , ev[4] )
    hi2yP.Fill( ev[3] , ev[4] )
    hi3XYP.Fill( ev[0] , ev[1] , ev[4] )


print( "Core: " + str(cntr) )
data = numpy.array( data_list )
weit = numpy.array( w_list )
mc   = numpy.array( mc_list )
#===============================================================================
reweighter = GBReweighter( n_estimators=1000 , max_depth=3 )
reweighter.fit( original=mc, target=data, target_weight = weit)
mc_weights = reweighter.predict_weights( mc )
#===============================================================================
for i in range(len(mc_list)):
    if ROOT.gRandom.Rndm() < mc_weights[i]:
        hr1X  .Fill( mc_list[i][0] )
        hr1Y  .Fill( mc_list[i][1] )
        hr1x  .Fill( mc_list[i][2] )
        hr1y  .Fill( mc_list[i][3] )
        hr1P  .Fill( mc_list[i][4] )
        hr2XY .Fill( mc_list[i][0] , mc_list[i][1] )
        hr2Xx .Fill( mc_list[i][0] , mc_list[i][2] )
        hr2Xy .Fill( mc_list[i][0] , mc_list[i][3] )
        hr2XP .Fill( mc_list[i][0] , mc_list[i][4] )
        hr2Yx .Fill( mc_list[i][1] , mc_list[i][2] )
        hr2Yy .Fill( mc_list[i][1] , mc_list[i][3] )
        hr2YP .Fill( mc_list[i][1] , mc_list[i][4] )
        hr2xy .Fill( mc_list[i][2] , mc_list[i][3] )
        hr2xP .Fill( mc_list[i][2] , mc_list[i][4] )
        hr2yP .Fill( mc_list[i][3] , mc_list[i][4] )
#        hr1X  .Fill( mc_list[i][0] , mc_weights[i] )
#        hr1Y  .Fill( mc_list[i][1] , mc_weights[i] )
#        hr1x  .Fill( mc_list[i][2] , mc_weights[i] )
#        hr1y  .Fill( mc_list[i][3] , mc_weights[i] )
#        hr1P  .Fill( mc_list[i][4] , mc_weights[i] )
#        hr2XY .Fill( mc_list[i][0] , mc_list[i][1] , mc_weights[i] )
#        hr2Xx .Fill( mc_list[i][0] , mc_list[i][2] , mc_weights[i] )
#        hr2Xy .Fill( mc_list[i][0] , mc_list[i][3] , mc_weights[i] )
#        hr2XP .Fill( mc_list[i][0] , mc_list[i][4] , mc_weights[i] )
#        hr2Yx .Fill( mc_list[i][1] , mc_list[i][2] , mc_weights[i] )
#        hr2Yy .Fill( mc_list[i][1] , mc_list[i][3] , mc_weights[i] )
#        hr2YP .Fill( mc_list[i][1] , mc_list[i][4] , mc_weights[i] )
#        hr2xy .Fill( mc_list[i][2] , mc_list[i][3] , mc_weights[i] )
#        hr2xP .Fill( mc_list[i][2] , mc_list[i][4] , mc_weights[i] )
#        hr2yP .Fill( mc_list[i][3] , mc_list[i][4] , mc_weights[i] )
#        hr3XYP.Fill( mc_list[i][0] , mc_list[i][1] , mc_list[i][4] , mc_weights[i] )

#===============================================================================
canvas.Close()

canv = ROOT.TCanvas("canv", "beam" , 1500, 900)
canv.Divide( 5, 3 )
canv.cd(  1 ); h1X.Draw()
canv.cd(  2 ); h1Y.Draw()
canv.cd(  3 ); h1x.Draw()
canv.cd(  4 ); h1y.Draw()
canv.cd(  5 ); h1P.Draw()
canv.cd(  6 ); h2XY.Draw("col")
canv.cd(  7 ); h2Xx.Draw("col")
canv.cd(  8 ); h2Xy.Draw("col")
canv.cd(  9 ); h2XP.Draw("col")
canv.cd( 10 ); h2Yx.Draw("col")
canv.cd( 11 ); h2Yy.Draw("col")
canv.cd( 12 ); h2YP.Draw("col")
canv.cd( 13 ); h2xy.Draw("col")
canv.cd( 14 ); h2xP.Draw("col")
canv.cd( 15 ); h2yP.Draw("col")

#canvi = ROOT.TCanvas("canvi", "init mc" , 1500, 900)
#canvi.Divide( 5, 3 )
#canvi.cd(  1 ); hi1X.Draw()
#canvi.cd(  2 ); hi1Y.Draw()
#canvi.cd(  3 ); hi1x.Draw()
#canvi.cd(  4 ); hi1y.Draw()
#canvi.cd(  5 ); hi1P.Draw()
#canvi.cd(  6 ); hi2XY.Draw("col")
#canvi.cd(  7 ); hi2Xx.Draw("col")
#canvi.cd(  8 ); hi2Xy.Draw("col")
#canvi.cd(  9 ); hi2XP.Draw("col")
#canvi.cd( 10 ); hi2Yx.Draw("col")
#canvi.cd( 11 ); hi2Yy.Draw("col")
#canvi.cd( 12 ); hi2YP.Draw("col")
#canvi.cd( 13 ); hi2xy.Draw("col")
#canvi.cd( 14 ); hi2xP.Draw("col")
#canvi.cd( 15 ); hi2yP.Draw("col")

canvr = ROOT.TCanvas("canvr", "re-weighted mc" , 1500, 900)
canvr.Divide( 5, 3 )
canvr.cd(  1 ); hr1X.Draw()
canvr.cd(  2 ); hr1Y.Draw()
canvr.cd(  3 ); hr1x.Draw()
canvr.cd(  4 ); hr1y.Draw()
canvr.cd(  5 ); hr1P.Draw()
canvr.cd(  6 ); hr2XY.Draw("col")
canvr.cd(  7 ); hr2Xx.Draw("col")
canvr.cd(  8 ); hr2Xy.Draw("col")
canvr.cd(  9 ); hr2XP.Draw("col")
canvr.cd( 10 ); hr2Yx.Draw("col")
canvr.cd( 11 ); hr2Yy.Draw("col")
canvr.cd( 12 ); hr2YP.Draw("col")
canvr.cd( 13 ); hr2xy.Draw("col")
canvr.cd( 14 ); hr2xP.Draw("col")
canvr.cd( 15 ); hr2yP.Draw("col")


#rfile.Close()
#===============================================================================
