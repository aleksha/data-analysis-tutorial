#===============================================================================
# --- prepare x-axis for TGraph
year = []
for xx in range(2010,2021):
    year.append( float(xx) )
#
#===============================================================================
# --- load data
dataset = []
with open("pred.csv","r") as dfile:
    for line in dfile:
        w =  line[:-1].split(",")
#        print( w[0] + "\t" + str(len( w )) )
        ticker = w[0]
        if len(w) == 25:
            name   = w[1]
            data   = []
            for i in range(3,14):
                data.append( float( w[i] ) )
        if len(w) == 26: # comma in name!
            name   = w[1]+w[2]
            data   = []
            for i in range(4,15):
                data.append( float( w[i] ) )
        dataset.append( { "ticker": ticker, "name": name, "data": data } )

