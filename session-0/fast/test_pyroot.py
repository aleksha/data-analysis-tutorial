import ROOT
from ROOT import gROOT, gRandom
import time

#c-part
start = time.time()
gROOT.ProcessLine(
"  TRandom r;\
   float carr[10000000];\
   for (Int_t i=0; i<10000000; i++)\
   {carr[i] = r.Gaus(0.00243, 0.00026);}\
");
stop = time.time()
c_time = stop - start


#python-part
start = time.time()
r = ROOT.TRandom()
pyarr = []
for i in range(10000000):
    pyarr.append(r.Gaus(0.00243, 0.00026))

stop = time.time()
py_time = stop - start


#arrays:
c_array = ROOT.carr
print(c_array[2])
print(pyarr[2])

#results
print("c- time = {}\npy-time = {}".format(c_time, py_time))
