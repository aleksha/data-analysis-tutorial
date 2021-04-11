#===============================================================================
# --- Massive imports
import ROOT
import ostap.fixes.fixes
from ostap.core.core import cpp, Ostap
from ostap.core.core import pwd, cwd, ROOTCWD
from ostap.core.core import rootID, funcID, funID, fID, histoID, hID, dsID
from ostap.core.core import VE
from ostap.histos.histos import h1_axis, h2_axes, h3_axes
from ostap.histos.graphs import makeGraph, hToGraph, hToGraph2, hToGraph3, lw_graph
import ostap.trees.trees
import ostap.trees.cuts
import ostap.histos.param
import ostap.histos.compare
import ostap.io.root_file
import ostap.math.models
import ostap.fitting.roofit
import ostap.fitting.models as Models
#
import itertools
from statistics import mean, stdev, quantiles
#===============================================================================
# --- get data and close canvas
from data import dataset, year
ban_list = ["PNR","OTIS","PPG","KO"]
#
#===============================================================================
# --- loop on companies
#
def get_stat( res ):
    idx = 0
    st = []
    for y in range(2021,2031):
        r_list = []
        for r in res:
            r_list.append( r[idx] )
        st.append(   ( y                                                  ,
                       quantiles( r_list, n=20, method='inclusive' ) [0]  ,
                       quantiles( r_list, n=20, method='inclusive' )[-1]  ) )
        idx = idx + 1
    return( st )
#
def jackknife( ds , years, sub_sample_length=8, fit_params = " "):
    res = []
    for s_ds in itertools.combinations( ds, sub_sample_length ):
#        print( s_ds )
        s_years = []
        for d in s_ds:
            s_years.append( years[ ds.index(d) ] )
        g = makeGraph( s_years, s_ds )
        fnc = ROOT.TF1("fnc","pol1", 2009, 2031 )
        r = g.Fit( fnc, "QS"+fit_params )
        s_res = []
        for y in range(2021,2031):
            s_res.append( fnc.Eval( float(y) ) )
        res.append( s_res )
    return get_stat( res )
#    return res
#===============================================================================
# --- loop on companies
fout = open("proj.csv","w")
fcon = open("cons.csv","w")
for d in dataset:
    lin = ROOT.TF1("lin","pol1", 2009, 2030 )
    rob = ROOT.TF1("rob","pol1", 2009, 2030 )
#    x2m = ROOT.TF1("x2m","[0]+[1]*x*x", 2009, 2030 )
    x2m = ROOT.TF1("x2m","expo", 2009, 2030 )
    rob.SetLineColor( 2 )
    g = makeGraph( year, d["data"] )
    rl = g.Fit( lin , "QS"         )
    r2 = g.Fit( x2m , "QS"         )
    rb = g.Fit( rob , "QS ROB=0.7" )

    stat  = jackknife( d["data"] , year )
    stat2 = jackknife( d["data"] , year , sub_sample_length=6 )
    y_high = []; y_low = [] ; yrs = []
    z_high = []; z_low = [] ;
    for s in stat:
        yrs   .append(s[0])
        y_low .append(s[1])
        y_high.append(s[2])
    for s in stat2:
        z_low .append(s[1])
        z_high.append(s[2])

    g_low  = makeGraph( yrs, y_low  )
    g_high = makeGraph( yrs, y_high )
    r_low  = makeGraph( yrs, z_low  )
    r_high = makeGraph( yrs, z_high )

    lin   .SetLineWidth(2)
    rob   .SetLineWidth(2)
    x2m   .SetLineWidth(2)
    g_low .SetLineWidth(2)
    g_high.SetLineWidth(2)
    r_low .SetLineWidth(3)
    r_high.SetLineWidth(3)

    lin   .SetLineStyle(7)
    rob   .SetLineStyle(7)
    x2m   .SetLineStyle(7)

    lin   .SetLineColor(4)
    rob   .SetLineColor(2)
    x2m   .SetLineColor(ROOT.kGreen+3)
    g_low .SetLineColor(4)
    g_high.SetLineColor(4)
    r_low .SetLineColor(4)
    r_high.SetLineColor(4)

    lin.GetYaxis().SetRangeUser( min( 0.9*min( d["data"] ), lin.Eval(2009) , rob.Eval(2009)                     ) ,
                                 max( 1.1*max( d["data"] ), lin.Eval(2030) , rob.Eval(2030) , g_high.Eval(2030) ,  r_high.Eval(2030) ) )
    ROOT.gPad.SetGridx();
    ROOT.gPad.SetGridy();
    lin.Draw()
    rob.Draw("same")
    x2m.Draw("same")
    g.SetMarkerStyle( 24 )
    g.Draw("P same")
    g_low .Draw("same L")
    g_high.Draw("same L")
    r_low .Draw("same L")
    r_high.Draw("same L")
    canvas.Print( d["ticker"] + ".png" )
    #===== write csv
    ss  = d["ticker"] + ","
    ss += d["name"]   + ",,"
    for v in d["data"]:
        ss += str(v) + ","
    for y in range( 2021, 2030 ):
        ss += '{:4.3f}'.format( lin.Eval( float(y) ) ) + ","
    ss += '{:4.3f}'.format( lin.Eval( float(2031.) ) ) + "\n"
    fout.write( ss )
    #===== write csv
    ss  = d["ticker"] + ","
    ss += d["name"]   + ",,"
    for v in d["data"]:
        ss += str(v) + ","
    for zz in z_low:
        ss += '{:4.3f}'.format(zz) + ","
    ss += "\n"
    fcon.write( ss )

fcon.close()
fout.close()
