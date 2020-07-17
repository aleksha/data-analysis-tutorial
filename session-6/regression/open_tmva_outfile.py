tfile = ROOT.TFile.Open("tmva.root","READ")
tree = tfile["tree/TestTree"]
tree.Draw("MLP-zpos")
my_stat = tree.statVar("MLP-zpos")
print( my_stat.rms() )
