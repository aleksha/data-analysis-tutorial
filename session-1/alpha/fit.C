{

  std::ifstream fOUT("./DUMP.txt" , std::ios::in);
  double x;
  TH1F *h = new TH1F("h","h",120,2.0,3.2);


  double max_x=0;
  while(fOUT >> x){
    if(x>2) h->Fill(x);
    if(x>max_x) max_x=x;
  }

  TF1 *func = new TF1("func","gaus(0)+pol1(3)", 2.0, 2.85);

  func->SetParameter(0,10);
  func->SetParameter(1,2.75);
  func->SetParameter(2,0.03);
  func->SetParameter(3,2);

  h->Fit(func);
  h->Draw();

}
