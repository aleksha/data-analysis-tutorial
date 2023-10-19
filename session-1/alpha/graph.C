{
  double x[6] = {1,2,3,4,5,6};
  double y[6] = {1.1,1.9,3.2,4.2,4.8,6.1};
  double ex[6] = {0,0,0,0,0,0};
  double ey[6] = {0.1,0.1,0.1,0.1,0.1,0.1};

  gr = new TGraph(6,x,y);


  g2 = new TGraphErrors(6,x,y,ex,ey);
  g2->SetTitle("Dummy");
  g2->GetXaxis()->SetTitle("x title");

  g2->SetMarkerStyle(20);

  g2->Draw("AP");
  g2->Fit("pol2");

}
