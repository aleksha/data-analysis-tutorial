Histogram parameterization

Often one needs to parameterize the historgam in terms of some predefined function or expansion - e.g. parameterize the efficiency.
Ostap offers a wide range of embedded parameterization

    in terms of Bernstein polynomials
        simple Bernstein sum, aka Bezier sum
        even Bernstein sum, such as f(x)=f(2*x0-x), where x0=0.5*(xmin+xmax)
        non-negative Bernstein sum
        non-negative monothonic Bernstein sum
        non-negative monothonic convex or concave Bernstein sum
        non-negative convex or concave Bernstein sum
    in term of Legendre polynomials
    in term of Chebyshev polynomials
    in terms of Fourier series
    in terms of Fourier cosine series
    in terms of Basic splines
        non-negative B-spline
        non-negative monothonic B-spline
        non-negative monothonic convex or concave B-spline
        non-negative convex or concave B-spline

From technical side, there are three branches of methods

    methods that uses only histogram values:
        these are safe, robust but they ignore the uncertainties
    methods that relies on ROOT.THF1.Fit
        typically not very good CPU performance
        sometimes fragile
    methods that relies on RooFit
        often the best series of methods

Simple parameterization

This group of methods allows to make easy and robust histogram parameterization, ignooring histogram unncertainties

histo  = ...
b1 = histo.bernstein_sum     (  6 ) ## parameterize as degree-6 Bernstein sum
b2 = histo.bernsteineven_sum (  6 ) ## parameterize as degree-6 Bernstein "even"-sum
l  = histo.legendre_sum      (  6 ) ## parameterize as degree-6 Legendre sum
ch = histo.chebyshev_sum     (  6 ) ## parameterize as degree-6 Chebyshev sum
f  = histo.fourier_sum       ( 12 ) ## parameterize as order-12 Fourier sum
c  = histo.cosine_sum        ( 12 ) ## parameterize as order-12 Fourier Cosine sum

ROOT.TH1.Fit-based parameterizations

These methods typically have not very good CPU performance, and sometiems are fragile, but they allow more accurate treatment of parameteriztaions, in particular them takes into account the uncertainties in the historgam.

histo  = ...
b1  = histo.bernstein     (  6 ) ## parameterize as degree-6 Bernstein sum
b2  = histo.bernsteineven (  6 ) ## parameterize as degree-6 Bernstein "even"-sum
l   = histo.legendre      (  6 ) ## parameterize as degree-6 Legendre sum
ch  = histo.chebyshev     (  6 ) ## parameterize as degree-6 Chebyshev sum
f   = histo.fourier       ( 12 ) ## parameterize as order-12 Fourier sum
c   = histo.cosine        ( 12 ) ## parameterize as order-12 Fourier Cosine sum
m   = histo.polynomial    (  6 ) ## parameterize as simple degree-6 monomial sum
p1  = histo.positive      (  6 ) ## parameterize as degree-6 non-negative Bernstein sum 
p2  = histo.positiveeven  (  6 ) ## parameterize as degree-6 non-negative even Bernstein sum 
m1  = histo.monothonic    ( 6 , increasing = False ) ## parameterize as degree-6 non-negative decreasing Bernstein sum 
m2  = histo.monothonic    ( 6 , increasing = True  ) ## parameterize as degree-6 non-negative increasing Bernstein sum
c1  = histo.convex        ( 6 , increasing = False , convex = True  ) ## parameterize as degree-6 non-negative decreasing convex  Bernstein sum 
c2  = histo.convex        ( 6 , increasing = False , convex = False ) ## parameterize as degree-6 non-negative decreasing concave Bernstein sum 
c3  = histo.convex        ( 6 , increasing = True  , convex = True  ) ## parameterize as degree-6 non-negative increasing convex  Bernstein sum 
c4  = histo.convex        ( 6 , increasing = True  , convex = False ) ## parameterize as degree-6 non-negative increasing concave Bernstein sum 
cc1 = histo.convexpoly    ( 6 ) #  parameterize as degree-6 non-negative convex  Bernstein sum 
cc2 = histo.concavepoly   ( 6 ) #  parameterize as degree-6 non-negative concave Bernstein sum

Various types of splines are also provided

s1 = histo.bSpline ( degree=3 , knots = 2 ) ## parameterize as 3d order spline with 2 inner (uniform) knots 
s2 = histo.bSpline ( degree=2 , knots = [0.1,0.4,0.8,0.9] ) ## parameterize as 3d order spline with 4 inner (non-uniform) knots

and similarly for

    non-negative spline pSpline,
    non-negative monothonic spline mSpline,
    non-negative monothonic convex or concave spline cSpline,
    non-negative convex spline convexSpline,
    non-negative concave spline concaveSpline.

RooFit-based parameterizations

r1  = histo.pdf_positive           ( 5 ) ## parameterize and non-negative degree-5 Bernstein sum
r2  = histo.pdf_positiveeven       ( 5 ) ## parameterize and non-negative degree-5 even Bernstein polynomial 
r3  = histo.pdf_increasing         ( 5 ) ## parameterize and non-negative degree-5 increasing Bernstein polynomial 
r4  = histo.pdf_decreasing         ( 5 ) ## parameterize and non-negative degree-5 decreasing Bernstein polynomial 
r5  = histo.pdf_convex_increasing  ( 5 ) ## parameterize and non-negative degree-5 convex  increasing Bernstein polynomial 
r6  = histo.pdf_convex_decreasing  ( 5 ) ## parameterize and non-negative degree-5 convex  decreasing Bernstein polynomial 
r7  = histo.pdf_concave_increasing ( 5 ) ## parameterize and non-negative degree-5 concave increasing Bernstein polynomial 
r8  = histo.pdf_concave_decreasing ( 5 ) ## parameterize and non-negative degree-5 concave decreasing Bernstein polynomial 
r9  = histo.pdf_concavepoly        ( 5 ) ## parameterize and non-negative degree-5 concave Bernstein polynomial 
r10 = histo.pdf_convexpoly         ( 5 ) ## parameterize and non-negative degree-5 convex  Bernstein polynomial

Similarly there are methods that provdies the parameterization in terms of splines :

    pdf_pSpline : non-negative b-spline
    pdf_mSpline : non-negative monothonic b-spline
    pdf_cSpline : non-negative monothonic concave or convex b-spline
    pdf_convexSpline : non-negative monothonic convex b-spline 


