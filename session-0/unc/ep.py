T_R =  10.000
M_p = 938.272
#E_e = 720.000
E_e = 500.000


from math import cos as COS
from math import asin as ASIN
from math import sqrt as SQRT

def E_scat(E,theta,M):
    return 1./( (1.-COS(theta))/M + 1/E )

def theta_T(T,E,M):
    return 2.*ASIN( SQRT( 0.5*M*T/(E*E-E*T) ) )

Q2_fixed =  2.*M_p*T_R
t_fixed  = -2.*M_p*T_R
theta_a = 2.0*ASIN( SQRT( Q2_fixed /(4.*E_e**2) ) )

print( "Q^2            : " + str( Q2_fixed ) )
print( "t/(4*M^2)      : " + str( Q2_fixed/(4.*M_p**2) ) )
print( "theta (approx) : " + str( theta_a  ) )
print( "theta (true)   : " + str( theta_T(T_R,E_e,M_p)  ) )

theta_e = theta_T(T_R,E_e,M_p)

from sympy import *
theta, E, M, t = symbols("theta E M t")
s1, s2 = symbols("s1 s2")

#Q2 = pow(E*theta,2) / (1+E*pow(theta,2)/2)
#Q2 = 4*E**2*((theta/2)**2) / (1+2*E*((theta/2)**2)/M)
Q2 = -4*E**2*(sin(theta/2)**2) / (1+2*E*(sin(theta/2)**2)/M)
#Q2 = 4*E**2*(sin(theta/2)**2)

d1 = diff(Q2, E)
d2 = diff(Q2, theta)
d1_2 = d1**2
d2_2 = d2**2
s = sqrt( d1_2*s1**2 + d2_2*s2**2 )
answer = s / Q2

#print( Q2.evalf(subs={ theta:theta_e, E:E_e, M:M_p}) )
#print( s.evalf( subs={ theta:theta_e, E:E_e, M:M_p, s2: 0.002*theta_e, s1:0.120} ) )
#print( answer.evalf(subs={ theta:theta_e, E:E_e, M:M_p, s2: 0.002*theta_e, s1:0.120}) )
#print( answer.evalf(subs={ theta:theta_e, E:E_e, M:M_p, s2: 0.00002, s1:0.120}) )

print( Q2.evalf(subs={ theta:theta_e, E:E_e, M:M_p}) )
print( s.evalf( subs={ theta:theta_e, E:E_e, M:M_p, s2: 0.0002*theta_e, s1:0.150} ) )
print( answer.evalf(subs={ theta:theta_e, E:E_e, M:M_p, s2: 0.0002*theta_e, s1:0.150}) )
print( answer.evalf(subs={ theta:theta_e, E:E_e, M:M_p, s2: 0.00002, s1:0.150}) )
print( answer.evalf(subs={ theta:theta_e, E:E_e, M:M_p, s2: 0.00002, s1:1.50}) )

def epXS( E, t, r = 0.84 ):
    from math import pow
    PI = 3.14159365   # pi constant.
    alpha  = 1./137.  # fine structure constatn.
    M      = 0.938272 #  mass of proton.
    M2     = M*M      # squared mass of proton.
    GeV2mb = 0.389379 # inverse GeV^2 to mb  : 0.38939 mb = 1/GeV^2
    GeV2fm = 0.19733  # inverse GeV to fm  : 0.19733 fm = 1/GeV

    Ge = 1. + pow(r/GeV2fm,2)*t/6. # as t = -Q^2
    Ge2 = pow(Ge,2) ;
    Gm2 = pow(sqrt(Ge2)*2.79,2);
    sig_ns = PI* pow( alpha / (t*E) , 2 ) # no structure cross section from Ref. Eq.2

    Re = Ge2 * ( pow( 4.*M*E + t ,2)/( 4.*M2 - t ) + t )               #
    Rm = Gm2 * ( pow( 4.*M*E + t ,2)/( 4.*M2 - t ) - t ) * t / (4.*M2) #

    sig = GeV2mb * sig_ns * ( Re - Rm ) ;
    return sig;

print( epXS(E_e*0.001,t_fixed*0.001*0.001) )

small = 1.+answer.evalf(subs={ theta:theta_e, E:E_e, M:M_p, s2: 0.00002, s1:0.150})
large = 1.+answer.evalf(subs={ theta:theta_e, E:E_e, M:M_p, s2: 0.00002, s1:1.500})

xx = []; yy = []; zz = [] ; ww=[]
for i in range(100):
    x_val =  0.82+0.001*i
    xx.append( x_val )
    yy.append(  epXS(E_e*0.001,t_fixed*0.001*0.001,x_val))
    ww.append(  epXS(E_e*0.001,small*t_fixed*0.001*0.001,x_val))
    zz.append(  epXS(E_e*0.001,large*t_fixed*0.001*0.001,x_val))

import matplotlib.pyplot as plt
plt.plot(yy,xx)
plt.plot(ww,xx,"g")
plt.plot(zz,xx,"r")
plt.grid(True)
plt.show()

