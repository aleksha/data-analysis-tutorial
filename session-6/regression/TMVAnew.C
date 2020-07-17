#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include "TChain.h"
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TObjString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TMVA/Tools.h"
#include "TMVA/Factory.h"
#include "TMVA/DataLoader.h"
#include "TMVA/TMVARegGui.h"
using namespace TMVA;
void TMVAnew( TString myMethodList = "" )
{
   TMVA::Tools::Instance();

   std::cout << std::endl;
   std::cout << "==> Start TMVAnew (aregression)" << std::endl;

   TFile* outputFile = TFile::Open( "TMVARegNew.root", "RECREATE" );

   TMVA::Factory *factory = new TMVA::Factory( "TMVAnew", outputFile,
                                               "!V:!Silent:Color:DrawProgressBar:AnalysisType=Regression" );

   TMVA::DataLoader *dataloader=new TMVA::DataLoader("tree");

   dataloader->AddVariable( "peak0", "Peak pad0", "ns", 'F' );
   dataloader->AddVariable( "peak1", "Peak pad1", "ns", 'F' );
   dataloader->AddVariable( "peak2", "Peak pad2", "ns", 'F' );
//   dataloader->AddVariable( "peak3", "Peak pad3", "ns", 'F' );

//   dataloader->AddVariable( "energy0", "Energy pad0", "ns", 'F' );
   dataloader->AddVariable( "energy1", "Energy pad1", "au", 'F' );
   dataloader->AddVariable( "energy2", "Energy pad2", "au", 'F' );
//   dataloader->AddVariable( "energy3", "Energy pad3", "ns", 'F' );

   dataloader->AddVariable( "start1", "Start pad1", "ns", 'F' );
   dataloader->AddVariable( "start2", "Start pad2", "ns", 'F' );

   dataloader->AddVariable( "end1", "End pad1", "ns", 'F' );
   dataloader->AddVariable( "end2", "End pad2", "ns", 'F' );

   // Add the variable carrying the regression target
//   dataloader->AddTarget( "angle" );
   dataloader->AddTarget( "zpos" );



   TFile *input(0);
   input = TFile::Open( "./new.root" ); // check if file in local directory exists

   if (!input) {
      std::cout << "ERROR: could not open data file" << std::endl;
      exit(1);
   }
   std::cout << "--- TMVARegression           : Using input file: " << input->GetName() << std::endl;

   // Register the regression tree
   TTree *regTree = (TTree*)input->Get("tree");
   Double_t regWeight  = 1.0;

   dataloader->AddRegressionTree( regTree, regWeight );
   // This would set individual event weights (the variables defined in the
   // expression need to exist in the original TTree)
   //dataloader->SetWeightExpression( "var1", "Regression" );

   // Apply additional cuts on the signal and background samples (can be different)
   TCut mycut = ""; // for example: TCut mycut = "abs(var1)<0.5 && abs(var2-0.5)<1";
   // tell the DataLoader to use all remaining events in the trees after training for testing:
   dataloader->PrepareTrainingAndTestTree( mycut,
                                         "nTrain_Regression=400:nTest_Regression=0:SplitMode=Random:NormMode=NumEvents:!V" );

   factory->BookMethod( dataloader,  TMVA::Types::kMLP, "MLP", "!H:!V:VarTransform=Norm:NeuronType=tanh:NCycles=20000:HiddenLayers=N+20:TestRate=6:TrainingMethod=BFGS:Sampling=0.3:SamplingEpoch=0.8:ConvergenceImprove=1e-6:ConvergenceTests=15:!UseRegulator" );

   // Train MVAs using the set of training events
   factory->TrainAllMethods();
   // Evaluate all MVAs using the set of test events
   factory->TestAllMethods();
   // Evaluate and compare performance of all configured MVAs
   factory->EvaluateAllMethods();
   // --------------------------------------------------------------
   // Save the output
   outputFile->Close();
   std::cout << "==> Wrote root file: " << outputFile->GetName() << std::endl;
   std::cout << "==> TMVARegression is done!" << std::endl;
   delete factory;
   delete dataloader;
   // Launch the GUI for the root macros
//   if (!gROOT->IsBatch()) TMVA::TMVARegGui( outfileName );
}


