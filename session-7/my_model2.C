#include "TStyle.h"
#include "TSystem.h"
#include "TRandom.h"
#include "TH1F.h"

TH1F* h;

void my_model2(double bias_low=0.02, double bias_high=0.04, double s=0.03, int N=10000){

  gStyle->SetOptFit(1111);

  h = new TH1F("my_model2",";difference, a.u; events",3000,-1.,2.);

  double r1,r2;

  for(int i=0;i<N;i++){
    r1 = gRandom->Gaus(0,s);
    r2 = gRandom->Gaus(0,s) + gRandom->Rndm()*(bias_high-bias_low) + bias_low;
    h->Fill( r2 -r1 );
  }


  h->Draw("E1");
  h->Fit("gaus");
}
