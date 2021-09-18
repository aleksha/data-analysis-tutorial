from math import sqrt, pow

def std_asym_ostap(n1,n2):
    return (VE(n1,n1).asym(VE(n2,n2))).error()

def std_asym_calc(n1,n2):
    return 2.*n1*sqrt(1./n1+1./n2) /( n2*pow(n1/n2+1.,2))


print("n=100")
print("  ostap = " + str(std_asym_ostap(100,100)))
print("  calc. = " + str(std_asym_calc (100,100)))
