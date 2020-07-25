Operations with trees/chains
General

tree = ...
print tree.branches() 
print tree.leaves() 
print 'Number of entries %s' % len ( tree )

For large number of bracnhes...

For trees with very large number of bracnhes (feature of LHCb) one can improves printout:

from   Ostap.Logger import multicolumn
print 'Branches: \n%s' % muhlticolumn ( tree.branches() )

Statistic for the given variable/expression

st1 = tree.statVar('m')
st2 = tree.statVar('m','pt>10')
st3 = tree.statVar('m/eff','(pt>10)*trg_eff')

The results are in a form of WStatEntity, weighted StatEntity)

ncorr = tree.sumVar('S_sw/eff','pt>10')

Also one can get statistics and covariances for the pair of variables/expressions:

s1 , s2 , cov2 = tree.statCov ( 'pt' , 'p' , 'pt>10' )

Or just simple

mn , mx = tree.minmax('1/eff')

Explicit loops

Explicit loops over the entries in tree/chain are trivial :

for i in  range(len(tree)) : 
    tree.GetEntry(i)
    if tree.pt <  10 : continue 
    print tree.m

But the direct looping looks a bit nicer:

for entry in tree : 
    if entry.pt <  10 : continue 
    print entry.m

Note that explciit loops are rather CPU-inefficient and slow. One can drastically improve performance by e.g embedding the cuts in iterator

for entry in tree.withCuts('pt>10') : 
    print entry.m

One can also specify first and last entries and display the progress bar

for entry in tree.withCuts('pt>10', last = 10000 , progress =  True ) : 
    print entry.m

Projections

h1 = ...
r  = tree.project ( h1 , 'mass' , 'pt>10' )

For loooong chains or huge trees...

The module Ostap.Kisa provides nice functionality for parallell processing of large chains or huge trees for projections

h1 = ...
long_chain =  ...
huge_tree   =  ...
import Ostap.Kisa
r1 = long_chain.pproject ( h1 , 'mass' , 'pt>10' ) 
r2 = huge_tree .pproject ( h1 , 'mass' , 'pt>10' ) 

For long chains it makes parallelizaion on per-tree level, and for huge trees it split the tree into chunks and parallelization is applied on per-chunk level.

