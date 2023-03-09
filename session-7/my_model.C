#include "TStyle.h"
#include "TSystem.h"
#include "TRandom.h"
#include "TH1F.h"

TH1F* h;

void my_model(double bias=0.027, double s=0.03, double sb=0.0, int N=10000){

  gStyle->SetOptFit(1111);

  h = new TH1F("my_model",";difference, a.u; events",3000,-1.,2.);

  double r1,r2;

  for(int i=0;i<N;i++){
    r1 = gRandom->Gaus(0,s);
    r2 = gRandom->Gaus(0,s) + gRandom->Gaus(bias,sb);
    h->Fill( r2 -r1 );
  }


  h->Draw("E1");
  h->Fit("gaus");
}
