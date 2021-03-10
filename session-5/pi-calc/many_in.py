canvas.Close()

from math import sin, tan, cos, pi, sqrt

def int2name( number ):
    if number>0:
        if number<10:
            return ("0000000"+str(number))
        if number<100:
            return ("000000"+str(number))
        if number<1000:
            return ("00000"+str(number))
        if number<10000:
            return ("0000"+str(number))
        if number<100000:
            return ("000"+str(number))
        if number<1000000:
            return ("00"+str(number))
        if number<10000000:
            return ("0"+str(number))
    return str(number)

def inner( n , radius = 1. ):
    answer_list = []
    phi = 2.*pi/n
    ang = 0.
    xi = radius
    yi = 0.
    length = 0.
    for i in range(n):
        ang += phi
        xf, yf = radius*cos( ang ) , radius*sin( ang ) 
        answer_list.append( ROOT.TLine(xi,yi,xf,yf) )
        length += sqrt(pow(xf-xi,2)+pow(yf-yi,2))
        xi, yi = xf, yf
    return length , answer_list

def outer( n , radius = 1.):
    phi = 2.*pi/n
    new_radius = sqrt( 1.+ pow(tan(0.5*phi),2) )
    l, a = inner(n, new_radius)
    return l, a


def draw_lines( lst , color = 4, width = 2):
    for line in lst:
        line.SetLineColor( color )
        line.SetLineWidth( width )
        line.Draw()

canv = ROOT.TCanvas("canv","canv",900,900)
h_dummy = ROOT.TH2F("h_dummy",";;",140,-1.2,1.2,140,-1.2,1.2)

arc = ROOT.TArc(0,0,1,0,360)
arc.SetLineColor(2)
arc.SetLineWidth(2)

for a in range(6,250):
    canv.Clear()
    h_dummy.Draw()
    arc.Draw()
#    lgt, ans = inner( a )
    lgt, ans = outer( a )
    draw_lines( ans )
#    lab = ROOT.TLatex(0.5,1,"#pi>"+"{0:6.5f}".format(lgt/2.))
    lab = ROOT.TLatex(0.5,1,"#pi<"+"{0:6.5f}".format(lgt/2.))
    lab.SetTextSize(0.035)
    lab.Draw()
    llb = ROOT.TLatex(-1,1,"n="+str(a))
    llb.SetTextSize(0.035)
    llb.Draw()
    canv.Print("fig_"+int2name(a)+".png")
