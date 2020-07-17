instance = ROOT.TMVA.Tools.Instance()
out_file = ROOT.TFile.Open("tmva.root","RECREATE")
factory = ROOT.TMVA.Factory("TMVAnew",out_file,"!V:!Silent:Color:DrawProgressBar:AnalysisType=Regression" )
dataloader = ROOT.TMVA.DataLoader("tree")
dataloader.AddVariable("peak1", "Peak pad1", "ns", 'F' )
dataloader.AddVariable("peak2", "Peak pad2", "ns", 'F' )
dataloader.AddTarget( "zpos" )
input = ROOT.TFile.Open( "new.root" )
regTree = input["tree"]
dataloader.AddRegressionTree( regTree, 1.0 )
mycut = ROOT.TCut("")
dataloader.PrepareTrainingAndTestTree(mycut,"nTrain_Regression=400:nTest_Regression=0:SplitMode=Random:NormMode=NumEvents:!V" )
factory.BookMethod( dataloader, ROOT.TMVA.Types.kMLP , "MLP", "!H:!V:VarTransform=Norm:NeuronType=tanh:NCycles=20000:HiddenLayers=N+20:TestRate=6:TrainingMethod=BFGS:Sampling=0.3:SamplingEpoch=0.8:ConvergenceImprove=1e-6:ConvergenceTests=15:!UseRegulator")
factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()
out_file.Close()