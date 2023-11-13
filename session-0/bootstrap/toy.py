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


from math import sqrt
from random import choice
from statistics import mean, stdev, median

N = 100

sample = []
f1 = ROOT.TF1("f1","gaus(0)",0,1)
f1.SetParameter(0,1)
f1.SetParameter(1,0.5) # mu
f1.SetParameter(2,0.1) # sigma

h = ROOT.TH1F("h"," ",100,0,1)

for i in range(N):
    x = f1.GetRandom()
    sample.append(x)
    h.Fill(x)

h.Draw()

print("H Mean  " + str( h.GetMean()   ) + " +/- " + str(h.GetMeanError() ) )
print("H StDev " + str( h.GetStdDev() ) + " +/- " + str(h.GetStdDevError() ) )

h.Fit("gaus")


b_mean = []; b_sigma = []; b_median = []
for t in range(1000):
    toy_sample = []
    for b in range(N):
        toy_sample.append( choice(sample) )
    b_mean  .append(   mean( toy_sample ) )
    b_median.append( median( toy_sample ) )
    b_sigma .append(  stdev( toy_sample ) )


print("MEAN  " + str(  mean(sample) ) )
print("      " + str(  mean(b_mean) ) )
print("      " + str( stdev(b_mean) ) )
print("   -- " + str( stdev(sample)/sqrt(N) ) )

print("SIGMA " + str( stdev(sample ) ) )
print("      " + str(  mean(b_sigma) ) )
print("      " + str( stdev(b_sigma) ) )

print("MEDIAN " + str(  median(sample) ) )
print("       " + str(  mean(b_median) ) )
print("       " + str( stdev(b_median) ) )
