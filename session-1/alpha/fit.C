{

  // https://root.cern/manual/fitting/
  // https://root.cern/doc/master/classTH1.html#a63eb028df86bc86c8e20c989eb23fb2a
  // https://root.cern/doc/master/classTFitResult.html

  gStyle->SetOptFit(1011);

  std::ifstream fOUT("./DUMP.txt" , std::ios::in);
  double x;
  TH1F *h = new TH1F("h","Cathode;Total energy, a.u.; Events",90,2.0,2.9);

  //h->GetXaxis()->SetTitle("x title");

  double max_x=0;
  while(fOUT >> x){
    if(x>2) h->Fill(x);
    if(x>max_x) max_x=x;
  }

  TF1 *func = new TF1("func","gaus(0)+pol0(3)", 2.0, 2.9);

  func->SetParameter(0,10);
  func->SetParameter(1,2.75);
  func->SetParameter(2,0.03);
  func->SetParameter(3,2);

  auto r = h->Fit(func,"SQ");
  h->Draw("E1");

  r->Print();

  auto rr  = r.Get();

  cout << "\n\n FCN  " << rr->MinFcnValue()  << "\n";
  cout << "\n\n Prob " << TMath::Prob(rr->MinFcnValue(), rr->Ndf())  << "\n";
}
