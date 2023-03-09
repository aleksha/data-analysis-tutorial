from statistics import mean, stdev
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
from scipy.stats import wilcoxon
from scipy.stats import t

bins = []
for i in range(11):
    bins.append(-0.1+i*0.02)


diff   = []
diff2  = []
a1 = []; a2 = []
better = 0

with open("WR2023-40yds.txt","r") as f:
#with open("RB2023-40yds.txt","r") as f:
    for line in f:
        if len(line)>5:
            w = line[:-1].split(",")
            diff.append( float(w[1]) - float(w[2]) )
            diff2.append( float(w[2]) - float(w[1]) )
            a1.append( float(w[1]) )
            a2.append( float(w[2]) )
            if float(w[1]) - float(w[2])>0:
                better += 1

print("Mean  : " + str(  mean(diff) ) + " +/- " + str( mean(diff)/sqrt( float(len(diff)) ) ) )
print("Stdev : " + str( stdev(diff) ) )

print( str(better) + " out of " + str(len(diff)) + " (" + str(100.*better/len(diff)) + ") improved at 2nd attempt" )

res1 = wilcoxon( np.array(a1), np.array(a2) )
res2 = wilcoxon( np.array(a1), np.array(a2), alternative='greater')
res3 = wilcoxon( np.array(a1), np.array(a2), alternative='less')
print("Wilcoxon (difference) p-value : " + str( res1.pvalue ) )
print("Wilcoxon (positive  ) p-value : " + str( res2.pvalue ) )
print("Wilcoxon (negative  ) p-value : " + str( res3.pvalue ) )


sample_mean = np.mean(diff2)
sample_variance = np.var(diff2, ddof=1)  # Note: set ddof to calculate sample var
t_statistic = sample_mean / np.sqrt(sample_variance / len(diff2) )
pvalue = 1 - t.cdf(df=len(diff2) - 1, x=abs(t_statistic))
print("t test                p-value : " + str(pvalue) )

#plt.hist(diff, bins)
#plt.show()
