#===============================================================================
#DIR_PATH     = "../20230605-0005/"
LEFT_BORDER  = 2400
RIGHT_BORDER = 6000
Y_LOW        = 0.15
Y_HIGH       = 0.85
SHOW_SPEC    = 1
LEFT_ONLY    = True
#===============================================================================
last_res = None # global var with recent results
#===============================================================================

import os
import numpy as np
#import matplotlib.pyplot as plt
import statistics as stat
from scipy.stats import pearsonr as rho

import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename, asksaveasfilename

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_pdf import PdfPages

from datetime import datetime

window = tk.Tk()

start_path_to_folder = "./20230530-0001/"
path_to_folder = tk.StringVar(value=start_path_to_folder)

methods = ["slopes", "baseline"]
method_var = tk.StringVar(value=methods[1]) 
pdf_var = tk.StringVar(value="recalib") 

left_border_var  = tk.IntVar(value=LEFT_BORDER ) 
right_border_var = tk.IntVar(value=RIGHT_BORDER) 
low_threshold_var  = tk.IntVar(value=int(Y_LOW*100.) ) 
high_threshold_var = tk.IntVar(value=int(Y_HIGH*100.)) 

preamp_name_var = tk.StringVar(value="R23-") 
preamp_num_var = tk.StringVar(value="00") 

def get_files(dir_path,postfix=".txt"):
    res = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path,path)):
            if path.endswith(postfix):
                res.append(os.path.join(dir_path,path))
    return res

def process_file(file_name):
    x=[]; y_in=[]; y_out=[]
    with open(file_name, encoding="utf-8") as fl:
        #print(file_name)
        cnt=0
        for line in fl:
            if cnt>2 and len(line)>2:
                w=line[:-1].split("\t")
                x    .append( float( w[0] ) )
                if "∞" not in w[1]:
                    y_in .append( float( w[1] ) )
                else:
                    y_in .append( 0. )

                if "∞" not in w[2]:
                    y_out .append( float( w[2] ) )
                else:
                    y_out .append( 0. )
            cnt+=1
    return ( file_name, np.array(x), ( np.array(y_in), np.array(y_out) ) )


def get_data(dir_path,report=False):
    r = get_files(dir_path)
    super_r = []
    for f in r:
        if report:
            print(f)
        super_r.append( process_file(f) )
    if report:
        print( str(len(super_r)) + " files proceed")
    return super_r

def calc_energy_baseline(spec,chan,max,left_base,right_base, AB=1):

    if LEFT_ONLY:
        right_base = left_base
    
    energy = 0.
    i = chan
    while spec[2][AB][i-1]>left_base and i>-1:
        if i-1<0 or i-1>8000:
            break
        energy += ( (spec[1][i]-spec[1][i-1])*0.5*( spec[2][AB][i]+spec[2][AB][i+1] ) )
        i-=1
    i_min = i
    i = chan
    while ( spec[2][AB][i-1]>right_base and (i<len(spec[1])) ):
        if i+1>8003 or i<0:
            break
        energy += ( (spec[1][i+1]-spec[1][i])*0.5*( spec[2][AB][i]+spec[2][AB][i+1] ) )
        i+=1
    i_max = i
    return (energy, i_min, i_max, spec[1][i_min], spec[1][i_max])

def find_x(y,x1,y1,x2,y2):
    if x1==x2:
        print("ERROR: find_x() : x1==x2 ==> same x")
        return 0.
    if y1==y2:
        print("ERROR: find_x() : y1==y2 ==> any x possible")
        return 0.
    return x1 + (y-y1)*(x2-x1)/(y2-y1)

def calc_energy_slopes(spec,chan,max,left_base,right_base,y_low=Y_LOW,y_high=Y_HIGH, AB=1):

    if LEFT_ONLY:
        right_base = left_base
        
    y_low = low_threshold_var.get()/100.
    y_high= high_threshold_var.get()/100.
    y_low = spec[2][AB][chan]*y_low
    y_high= spec[2][AB][chan]*y_high
    energy = 0.

    # go left
    i = chan
    i_low = chan
    i_high = chan
    while spec[2][AB][i]>y_high:
        energy += ( (spec[1][i]-spec[1][i-1])*0.5*( spec[2][AB][i]+spec[2][AB][i+1] ) )
        if spec[2][AB][i-1]<y_high:
            i_high = i-1
        i-=1
    while spec[2][AB][i]>y_low:
        energy += ( (spec[1][i]-spec[1][i-1])*0.5*( spec[2][AB][i]+spec[2][AB][i+1] ) )
        if spec[2][AB][i-1]<y_low:
            i_low = i-1
        i-=1
    i_min = int( find_x(left_base,i_low,spec[2][AB][i_low],i_high,spec[2][AB][i_high]) )
    x_min = find_x(left_base,i_low,spec[2][AB][i_low],i_high,spec[2][AB][i_high])
    while i>i_min:
        energy += ( (spec[1][i]-spec[1][i-1])*0.5*( spec[2][AB][i]+spec[2][AB][i+1] ) )
        i-=1

    # go right
    i = chan
    while spec[2][AB][i]>y_high:
        energy += ( (spec[1][i+1]-spec[1][i])*0.5*( spec[2][AB][i]+spec[2][AB][i+1] ) )
        if spec[2][AB][i+1]<y_high:
            i_high = i+1
        i+=1
    while spec[2][AB][i]>y_low:
        energy += ( (spec[1][i+1]-spec[1][i])*0.5*( spec[2][AB][i]+spec[2][AB][i+1] ) )
        if spec[2][AB][i+1]<y_low:
            i_low = i+1
        i+=1
    i_max = int( find_x(left_base,i_low,spec[2][AB][i_low],i_high,spec[2][AB][i_high]) )
    x_max = find_x(left_base,i_low,spec[2][AB][i_low],i_high,spec[2][AB][i_high])
    while i<i_max:
        energy += ( (spec[1][i+1]-spec[1][i])*0.5*( spec[2][AB][i]+spec[2][AB][i+1] ) )
        i+=1

    return (energy, i_min, i_max, x_min, x_max )

def calc_energy(spec,chan,max,left_base,right_base,AB):
    method = method_var.get()
    if method=="slopes":
        return calc_energy_slopes(spec,chan,max,left_base,right_base,AB)
    if method=="baseline":
        return calc_energy_baseline(spec,chan,max,left_base,right_base, AB)
    return calc_energy_slopes(spec,chan,max,left_base,right_base)

def analyze_spectrum(spec,AB=1,left_border=LEFT_BORDER, right_border=RIGHT_BORDER):
    left_border = left_border_var.get()
    right_border = right_border_var.get()

    chan       = np.argmax ( spec[2][AB]        )
    val        = np.max    ( spec[2][AB]        )
    left_base  = np.average( spec[2][AB][0:left_border] )
    right_base = np.average( spec[2][AB][right_border:] )
    energy     = calc_energy(spec,chan,max,left_base,right_base,AB)


    return ( chan , val, left_base, right_base , energy)


def process_dir( path_to_dir , fig):
    r = get_data(path_to_dir)

    energiesT  = []
    energiesA  = []
##    startsA    = []
##    stopsA     = []
##    durationsA = []
##    ampA       = []

    energiesB  = []
##    startsB    = []
##    stopsB     = []
##    durationsB = []
##    ampB       = []

    for s in r:
        mA = analyze_spectrum(s,0)
        #print(r.index(s)+1)
        energiesA.append(mA[4][0])
##        startsA.append(mA[4][3])
##        stopsA.append(mA[4][4])
##        durationsA.append( mA[4][4]-mA[4][3])
##        ampA.append( mA[1])

        mB = analyze_spectrum(s,1)
        energiesB.append(mB[4][0])
        energiesT.append(mA[4][0]+mB[4][0])
##        startsB.append(mB[4][3])
##        stopsB.append(mB[4][4])
##        durationsB.append( mB[4][4]-mB[4][3])
##        ampB.append( mB[1])


    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    ss  = "================================================================================="
    ss += "\n  Date and time : " + dt_string
    ss += "\n------------------------------ CONDITIONS ---------------------------------------"
    ss += "\n  Folder  : " + path_to_dir
    ss += "\n  Method  : " + str(method_var.get())
    if str(method_var.get())=="slopes":
        ss += "    (linear part in [" + str(low_threshold_var.get()) + ","
        ss += str(high_threshold_var.get())+ "]% of spectrum height)"
    ss += "\n  Borders : [" + str(left_border_var.get()) + "," + str(right_border_var.get())+ "]"
    ss += "\n------------------------------ PREAMP. ------------------------------------------"
    ss += "\n  Lable   : " + str(preamp_name_var.get())
    ss += "\n  Channel : " + str(preamp_num_var.get())
    ss += "\n------------------------------ RESULTS ------------------------------------------"
    ss += "\n A:"
    ss += "\n  Mean  Energy            : " + str(stat.mean(energiesA))
    ss += "\n  StDev of Mean Energy    : " + str(stat.stdev(energiesA)/np.sqrt(float(len(energiesA))))
    ss += "\n  StDev of Energy         : " + str(stat.stdev(energiesA))
    ss += "\n B"
    ss += "\n  Mean  Energy            : " + str(stat.mean(energiesB))
    ss += "\n  StDev of Mean Energy    : " + str(stat.stdev(energiesB)/np.sqrt(float(len(energiesB))))
    ss += "\n  StDev of Energy         : " + str(stat.stdev(energiesB))
    ss += "\n Total:"
    ss += "\n  Mean  Energy            : " + str(stat.mean(energiesT))
    ss += "\n  StDev of Mean Energy    : " + str(stat.stdev(energiesT)/np.sqrt(float(len(energiesT))))
    ss += "\n  StDev of Energy         : " + str(stat.stdev(energiesT))
    ss += "\n=================================================================================\n\n"
    
    for idx in range(len(r)):
        if idx==0:
            avB  = r[idx][2][1]*float(1/len(r))
        else:
            avB += r[idx][2][1]*float(1/len(r))

    for idx in range(len(r)):
        if idx==0:
            avA  = r[idx][2][0]*float(1/len(r))
        else:
            avA += r[idx][2][0]*float(1/len(r))

    fig.clear()
    plt = fig.add_subplot(111)
    plt.clear()

#    plt.hist(energies)

#    plt.hist(starts)

#    plt = fig.add_subplot(111)
#    plt.clear()
    plt.plot(r[0][1],avA,"b-")
    plt.plot(r[0][1],avB,"r-")
    plt.set_xlabel("Time [us]")
    plt.set_ylabel("Signal [a.u.]")
##    rrA = {"energies":energiesA,"starts":startsA,"stops":stopsA,"durations":durations,"data":r,"av":av,"amp":amp}
##    rrB = {"energies":energiesB,"starts":starts,"stops":stops,"durations":durations,"data":r,"av":av,"amp":amp}
    rrA = {"energies":energiesA, "av":avA, "data":r}
    rrB = {"energies":energiesB, "av":avB, "data":r}
    rrT = {"energies":energiesT, "av":avA, "data":r}
    return (ss, rrA, rrB, rrT)

#===============================================================================
# GUI
#===============================================================================



def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


window.title("PicoScope's Spectra Analysis")


txt_edit = tk.Text(window, width=100)


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = tk.filedialog.askdirectory()
    path_to_folder.set(filename)

#scroll_bar = tk.Scrollbar(window)

fig_draw = Figure(figsize=(7,5), dpi=100)

canvas = FigureCanvasTkAgg(fig_draw, window)
canvas.draw()


def upd_result(txt=txt_edit,fig=fig_draw):
    folder=path_to_folder.get()
    print(folder)
    res = process_dir(folder,fig)
    last_ras = res
    canvas.draw()
    txt.insert(tk.END, res[0])
    global last_res
    last_res = res
    return res

xlab = {  "energies":"Energy [a.u.]",
          "starts":"Signal start [ch.]","stops":"Signal stop [ch.]",
          "durations":"Signal duration [ch.]","gen":"Input signal [a.u.]",
          "amp":"Amplitude [a.u.]"}

def draw_canv(what="energies",AB=0,txt=txt_edit,fig=fig_draw):
    global last_res
    if last_res==None:
        last_res = upd_result(txt,fig)
    fig.clear()
    plt = fig.add_subplot(111)
    plt.clear()
    plt.hist( last_res[AB+1][what] )
    plt.set_xlabel(xlab[what])
    plt.set_ylabel("Entries")
    canvas.draw()

def draw_env(what="energies",AB=0,txt=txt_edit,fig=fig_draw):
    global last_res
    if last_res==None:
        last_res = upd_result(txt,fig)
    fig.clear()
    plt = fig.add_subplot(111)
    plt.clear()
    xmax = max(last_res[AB+1][what])
    xbins = []
    for i in range(51):
        xbins.append( 0.6*xmax + 0.4*xmax*i/50. )
    plt.hist( last_res[AB+1][what] , xbins)
    with open("DUMP.txt","w") as fl:
        for my_x in last_res[AB+1][what]:
            fl.write( str(my_x)+"\n")
    plt.set_xlabel(xlab[what])
    plt.set_ylabel("Entries")
    canvas.draw()

def draw_energiesA(txt=txt_edit,fig=fig_draw):
    draw_env("energies",0,txt,fig)

def draw_energiesB(txt=txt_edit,fig=fig_draw):
    draw_env("energies",1,txt,fig)
    
def draw_energiesT(txt=txt_edit,fig=fig_draw):
    draw_env("energies",2,txt,fig)

def draw_starts(txt=txt_edit,fig=fig_draw):
    draw_canv("starts",txt,fig)

def draw_stops(txt=txt_edit,fig=fig_draw):
    draw_canv("stops",txt,fig)

def draw_durations(txt=txt_edit,fig=fig_draw):
    draw_canv("durations",txt,fig)

def draw_input(txt=txt_edit,fig=fig_draw):
    draw_canv("gen",txt,fig)

def draw_amp(txt=txt_edit,fig=fig_draw):
    draw_canv("amp",txt,fig)

def draw_spectra(txt=txt_edit,fig=fig_draw):
    global last_res
    if last_res==None:
        last_res = upd_result(txt,fig)
    fig.clear()
    plt = fig.add_subplot(111)
    plt.clear()
    plt.plot(last_res[1]["data"][0][1],last_res[1]["av"],"b-")
    plt.plot(last_res[1]["data"][0][1],last_res[2]["av"],"r-")
    plt.set_xlabel("Time [us]")
    plt.set_ylabel("Signal [a.u.]")
    canvas.draw()

def draw_scatter(txt=txt_edit,fig=fig_draw):
    global last_res
    if last_res==None:
        last_res = upd_result(txt,fig)
    fig.clear()
    plt = fig.add_subplot(111)
    plt.clear()
    plt.scatter(last_res[1]["gen"],last_res[1]["energies"])
    plt.set_xlabel("Input signal [a.u]")
    plt.set_ylabel('Energy [a.u.]')
    canvas.draw()


def create_pdf(pdf_name="output.pdf",txt=txt_edit,fig=fig_draw):
    global last_res
    if last_res==None:
        last_res = upd_result(txt,fig)

    pdf_name = str(pdf_var.get())+"_" +str(preamp_name_var.get()) + "_"+str(preamp_num_var.get()) +".pdf"
    pdf = PdfPages( pdf_name)

    fig.clear()
    plt = fig.add_subplot(111)
    plt.clear()
#    plt.plot([0,1],[0,1],"b")
    plt.text(0.0, 0.0, last_res[0], fontsize = 6)
    plt.axis('off')
    pdf.savefig( fig )

    fig.clear()
    plt = fig.add_subplot(111)
    plt.clear()
    plt.scatter(last_res[1]["gen"],last_res[1]["energies"])
    plt.set_xlabel("Input signal [a.u]")
    plt.set_ylabel('Energy [a.u.]')
    pdf.savefig( fig )

    fig.clear()
    plt = fig.add_subplot(111)
    plt.clear()
    plt.plot(last_res[1]["data"][0][1],last_res[1]["av"],"b-")
    plt.plot(last_res[1]["data"][SHOW_SPEC][1],last_res[1]["data"][SHOW_SPEC][2][1],"r-")
    plt.set_xlabel("Time [us]")
    pdf.savefig( fig )


    lst_pdf = ["energies", "starts", "stops", "durations", "gen","amp"]
    for what in lst_pdf:
        fig.clear()
        plt = fig.add_subplot(111)
        plt.clear()
        plt.hist( last_res[1][what] )
        plt.set_xlabel(xlab[what])
        plt.set_ylabel("Entries")
        pdf.savefig( fig )

    pdf.close()
    print("PDF file " + pdf_name + " has been created")


    
def dummy():
    print("Dummy function has been called")
    
frame_input = tk.Frame(window)
#frame_input = tk.Frame(window, relief=tk.RAISED, bd=2)

#lbl_open = tk.Label(window, text="Open", command=open_file)
lbl_open = tk.Label(frame_input, text="Folder with data: ")
lbl_open.grid(row=0,column=0)
txt_input = tk.Entry(frame_input, textvariable=path_to_folder, width=50)
txt_input.grid(row=0,column=1)
btn_browse = tk.Button(frame_input, text="Browse", command=browse_button)
btn_open = tk.Button(frame_input, text="Analyse", command=upd_result )
#btn_save = tk.Button(frame_input, text="Analyse", command=upd_result( txt_edit, path_to_folder.get() ) )
#btn_save = tk.Button(frame_input, text="Analyse", command=dummy )
btn_save = tk.Button(frame_input, text="Save log as...", command=save_file )
lbl_pdf = tk.Label(frame_input, text="PDF file prefix: ")
ent_pdf = tk.Entry(frame_input, textvariable=pdf_var, width=15)
btn_pdf  = tk.Button(frame_input, text="PDF", command=create_pdf )
btn_browse.grid(row=0, column=2)
btn_open.grid(row=0,column=3)
btn_save.grid(row=0,column=4)
lbl_pdf.grid(row=0,column=5)
ent_pdf.grid(row=0,column=6)
btn_pdf.grid(row=0,column=7)

frame_input.grid(row=0,column=0)



frame_control = tk.Frame(window)
lbl_method = tk.Label(frame_control, text="Method: ")
cbx_method = Combobox(frame_control, textvariable=method_var, values=methods)

lbl_left = tk.Label(frame_control, text="Left border [ch]: ")
ent_left = tk.Entry(frame_control, textvariable=left_border_var, width=5)
lbl_right= tk.Label(frame_control, text="Right border [ch]: ")
ent_right= tk.Entry(frame_control, textvariable=right_border_var, width=5)

lbl_low  = tk.Label(frame_control, text="Low threshold [%]: ")
ent_low  = tk.Entry(frame_control, textvariable=low_threshold_var, width=4)
lbl_high = tk.Label(frame_control, text="High threshold [%]: ")
ent_high = tk.Entry(frame_control, textvariable=high_threshold_var, width=4)

lbl_method.grid(row=0,column=0)
cbx_method.grid(row=0,column=1)
lbl_left.grid(row=0,column=2)
ent_left.grid(row=0,column=3)
lbl_right.grid(row=0,column=4)
ent_right.grid(row=0,column=5)
lbl_low.grid(row=0,column=6)
ent_low.grid(row=0,column=7)
lbl_high.grid(row=0,column=8)
ent_high.grid(row=0,column=9)

frame_control.grid(row=1,column=0)

frame_draw = tk.Frame(window)
lbl_draw = tk.Label(frame_draw, text="\tDraw buttons: ")
btn_energies  = tk.Button(frame_draw, text="Energies A", command=draw_energiesA)
btn_energiesB = tk.Button(frame_draw, text="Energies B", command=draw_energiesB )
btn_energiesT = tk.Button(frame_draw, text="Total E", command=draw_energiesT )
btn_spectra   = tk.Button(frame_draw, text="Spectra", command=draw_spectra  )
btn_starts    = tk.Button(frame_draw, text="Starts", command=dummy )
btn_stops     = tk.Button(frame_draw, text="Stops", command=dummy  )
btn_durations = tk.Button(frame_draw, text="Durations", command=dummy )
btn_input     = tk.Button(frame_draw, text="Input", command=dummy )
btn_scatter   = tk.Button(frame_draw, text="Scatter", command=dummy )
btn_amp       = tk.Button(frame_draw, text="Amplitude", command=dummy )
##btn_starts    = tk.Button(frame_draw, text="Starts", command=draw_starts )
##btn_stops     = tk.Button(frame_draw, text="Stops", command=draw_stops  )
##btn_durations = tk.Button(frame_draw, text="Durations", command=draw_durations  )
##btn_input     = tk.Button(frame_draw, text="Input", command=draw_input )
##btn_scatter   = tk.Button(frame_draw, text="Scatter", command=draw_scatter )
##btn_amp       = tk.Button(frame_draw, text="Amplitude", command=draw_amp )
lbl_name = tk.Label(frame_draw, text="Preamp: ")
ent_name = tk.Entry(frame_draw, textvariable=preamp_name_var, width=8)
lbl_num  = tk.Label(frame_draw, text="Ch: ")
ent_num  = tk.Entry(frame_draw, textvariable=preamp_num_var, width=2)


lbl_name.grid(row=0,column=0)
ent_name.grid(row=0,column=1)
lbl_num.grid(row=0,column=2)
ent_num.grid(row=0,column=3)
lbl_draw.grid(row=0,column=4)
btn_energies.grid(row=0,column=5)
btn_energiesB.grid(row=0,column=6)
btn_energiesT.grid(row=0,column=7)
btn_spectra.grid(row=0,column=8)
##btn_starts.grid(row=0,column=8)
##btn_stops.grid(row=0,column=8)
##btn_durations.grid(row=0,column=9)
##btn_input.grid(row=0,column=11)
##btn_scatter.grid(row=0,column=12)
##btn_amp.grid(row=0,column=13)

frame_draw.grid(row=2,column=0)


#canvas.get_tk_widget().grid(row=2,column=0,side=tk.BOTTOM, fill=tk.BOTH, expand=True)
canvas.get_tk_widget().grid(row=3,column=0)


txt_edit.grid(row=4,column=0)
v=tk.Scrollbar(window, orient='vertical', command=txt_edit.yview)
v.grid(row=4,column=1,sticky='nsew')

txt_edit['yscrollcommand'] = v.set
#v.config(command=txt_edit.yview)

window.mainloop()
