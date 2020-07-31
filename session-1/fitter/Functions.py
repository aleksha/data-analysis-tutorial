import ostap.fitting.models as Models
from   ostap.utils.timing import timing
from   ostap.histos.histos  import h1_axis
import math 
import ROOT
from   ostap.math.ve         import VE
from   ostap.math.math_ve    import *  ## get functions 
#-------------------------------------------------------------------------------
# class for color output
#-------------------------------------------------------------------------------
# ss += bcolors.WARNING + it4d(int(num_submitted )) + bcolors.ENDC + "  "

class bcolors:
    HEADER  = '\033[95m'
    OKBLUE  = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL    = '\033[91m'
    ENDC    = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def message( msg , msg_color = "white"):
    color_msg = msg
    if msg_color == "header":
        color_msg = bcolors.HEADER  + msg + bcolors.ENDC
    if msg_color == "blue":
        color_msg = bcolors.OKBLUE  + msg + bcolors.ENDC
    if msg_color == "green":
        color_msg = bcolors.OKGREEN  + msg + bcolors.ENDC
    if msg_color == "fail":
        color_msg = bcolors.FAIL  + msg + bcolors.ENDC
    if msg_color == "warning":
        color_msg = bcolors.WARNING  + msg + bcolors.ENDC
    print( color_msg )

#-------------------------------------------------------------------------------

def make_dir( pth ):
    if not os.path.isdir(pth):
        os.system("mkdir " + pth)

#======= ROOFIT VARIABLES ======================================================

def make_var_limit_cut ( var_name, var ):
    cut = " && " + var_name + ">"+str(var.getMin()) + " && "+var_name+"<" + str(var.getMax())
    return cut

def draw_param(r_fit, w_fit, h_fit, N_BINS, var, W_max, name, XTitle, Prefix, Type, var_Units):

    var_list = []
    for idx in range(N_BINS+1):
        var_list.append(var.getMin()+idx*(var.getMax()-var.getMin())/N_BINS )
    h_pull = h1_axis(var_list)
    for idx in range(1,N_BINS):
        h_pull[idx]=VE(h_fit[idx-1][3],0**2)

    h_pull.GetYaxis().SetRangeUser(-4,4)
    h_pull.GetYaxis().SetTitle("#Delta / #sigma")
    h_pull.GetYaxis().SetTitle("#Delta / #sigma")
    h_pull.GetYaxis().SetTitleSize(0.2)
    h_pull.GetYaxis().SetTitleOffset(0.2)
    h_pull.GetYaxis().SetLabelSize(0.1)
    h_pull.GetXaxis().SetLabelSize(0.15)
    h_pull.SetFillColor(34)

    line_up   = ROOT.TLine(var.getMin(),  2, var.getMax(),  2)
    line_down = ROOT.TLine(var.getMin(), -2, var.getMax(), -2)
    line_up  .SetLineColor(2)
    line_down.SetLineColor(2)


    #-------------------------------------------------------------------
    # Prepare for drawing
    #-------------------------------------------------------------------

    Y_title = 0.92*W_max
    Y_step  = 0.05*W_max

    x_pos = var.getMin() + 0.05 * (var.getMax() - var.getMin())

    percentage = " ("+ "{:2.2f}".format( 100. * r_fit("S" )[0].error() / r_fit("S" )[0].value() ) + "%)"
    text_SIG  = "SIGNAL = " + "{:5.0f}".format(r_fit("S" )[0].value())
    text_SIG += " #pm" + "{:4.0f}".format(r_fit("S" )[0].error()) + percentage
    text_BKG  = "BKG = " + "{:5.0f}".format(r_fit("B" )[0].value())
    text_BKG += " #pm" + "{:4.0f}".format(r_fit("B" )[0].error())


    labels = []
    labels.append( ROOT.TLatex( x_pos, Y_title - 0.0*Y_step, text_SIG ) )
    labels.append( ROOT.TLatex( x_pos, Y_title - 1.5*Y_step, text_BKG ) )

    for lb in labels :
        lb.SetTextSize(0.04)

    w_fit.GetXaxis().SetTitle(XTitle+", "+var_Units)
    w_fit.GetXaxis().SetTitleSize(0.05)
    w_fit.GetXaxis().SetTitleOffset(0.9)
    w_fit.GetYaxis().SetRangeUser(0.01, W_max)
    w_fit.GetYaxis().SetTitleOffset(0.9)
    w_fit.GetYaxis().SetTitle("Candidates per "+str((var.getMax()-var.getMin())/N_BINS)+" "+var_Units)
    w_fit.GetYaxis().SetLabelSize(0.025)

    #-------------------------------------------------------------------
    # Draw it!
    #-------------------------------------------------------------------

    canv = ROOT.TCanvas("canv","canv",700,800)
    canv.Divide(1,2)

    pad1 = canv.GetListOfPrimitives().FindObject("canv_1")
    pad2 = canv.GetListOfPrimitives().FindObject("canv_2")
    pad1.SetPad(0.00, 0.11, 1.00, 1.00)
    pad2.SetPad(0.00, 0.00, 1.00, 0.10)

    canv.cd(1)
    w_fit.Draw()
    for lb in labels: lb.Draw()
    canv.cd(2)
    h_pull.Draw("HIST")
    line_up  .Draw()
    line_down.Draw()

    canv.Print(Prefix+"_"+name+"."+Type) 
    canv.Close()

