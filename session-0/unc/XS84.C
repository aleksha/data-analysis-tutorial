//----------------------------------------------------------------
//
// Goal   : Rosenbluth's cross section for mu p-scattering
// Author : Alexey Dzyuba, PNPI
// E-Mail : a.dzyuba@gmail.com
// Date   : 2017-07-14
//
// Tested with CERN ROOT v5.34/32
//
//----------------------------------------------------------------


//----------------------------------------------------------------
// Proton electric form factor squared as a function of
// Mandelstam t-invariant and effective radius of proton
//
double GE2(double t, double r = 0.84){
    double GeV2fm = 0.19733 ; // inverse GeV to fm  : 0.19733 fm = 1/GeV
    double Ge = 1. + pow(r/GeV2fm,2)*t/6.; // as t = -Q^2
    return pow(Ge,2) ;
}

//----------------------------------------------------------------
// Proton magnetic form factor squared as a function of
// Mandelstam t-invariant and effective radius of proton
//
double GM2(double t, double r = 0.84){
    // Dipole paramettrization for G_m
    return pow(sqrt(GE2(t,r))*2.79,2);
}

//----------------------------------------------------------------
// Rosenbluth cross section (Landau, Lifshits IV, Eq 139.9, p.685)
//
double epXS( double E, double t, double r = 0.84 ){

    double PI = TMath::Pi()  ; // pi constant.
    double alpha  = 1./137.  ; // fine structure constatn.
    //double m      = 0.1056584; // mass of electron (not needed fere in fact).
    double M      = 0.938272 ; // mass of proton.
    double M2 = M*M          ; // squared mass of proton.
    double GeV2mb = 0.389379  ; // inverse GeV^2 to mb  : 0.38939 mb = 1/GeV^2
    
    //-------------------------------------------------------
    // Proton electric and magnetic form factors squared
    //
    double Ge2,Gm2;
    Ge2 = GE2( t, r );
    Gm2 = GM2( t, r );

    double sig_ns ; // no structure cross section from Ref. Eq.2
    sig_ns = PI* pow( alpha / (t*E) , 2 ) ;

    double Rm, Re;
    Re = Ge2 * ( pow( 4.*M*E + t ,2)/( 4.*M2 - t ) + t )           ;
    Rm = Gm2 * ( pow( 4.*M*E + t ,2)/( 4.*M2 - t ) - t ) * t / (4.*M2) ;

    double sig = GeV2mb * sig_ns * ( Re - Rm ) ;
    return sig;
}

//----------------------------------------------------------------
// main function
void XS84(){

 const int N = 220   ; // number of poins.
 double t            ; // running t-invariant GeV^2.
 double T            ; // running recoil proton kinetic energy GeV.
 double E = 0.720    ; // Energy of el beam.
 double M = 0.938272 ; // mass of proton, GeV.

 double x[N], y1[N]; //arrays for TGraph.

 // loop to fill arrays
 for(int i=0 ; i<N; i++){
     T = 0.0001 + 0.0001 * i ;
     t = - 2. * M * T        ;
     x[i] = T*1000. ; // Recoil kinetic energy, MeV.
     y1[i] = epXS( E , t , 0.84 ) ; // XS with R_proton = 0.84 fm.
 }

//----------------------------------------------------------------
// TGraph definition and some polishing
//
 TGraph *gr1 = new TGraph( N, x, y1 );
 gr1->SetLineWidth(3);
 gr1->SetLineColor(2);
 gr1->SetTitle("");
 gr1->GetXaxis()->SetRangeUser(0.03,22.9);
 gr1->GetYaxis()->SetRangeUser(0.09,1010);
 gr1->GetYaxis()->SetTitle(" d#sigma / dt , mb / (GeV c)^{2}");
 gr1->GetYaxis()->SetTitleFont( 2 );
 gr1->GetXaxis()->SetTitleFont( 2 );
 gr1->GetYaxis()->SetLabelFont( 2 );
 gr1->GetXaxis()->SetLabelFont( 2 );

//----------------------------------------------------------------
// Additional x-axis on top of figure
//
 TGaxis *axis = new TGaxis(0.1, 1010 , 22.5 ,1010, 0.0001*2.*M , 0.0225*2.*M ,510,"-");
 axis->SetLabelSize(0.035);
 axis->SetTitleFont(2);
 axis->SetTitleOffset(1);

//----------------------------------------------------------------
// TLateX labels
//
 TLatex *tl = new TLatex(14,400,"Electrons 720 MeV");
 TLatex *tr = new TLatex(14,170,"R_{p} = 0.84 fm");
 tr->SetTextColor(2);
 TLatex *tf = new TLatex(10,6,"#frac{d#sigma}{dt} ~ 1 / t^{2},  #minus t = 2MT_{R}");
 TLatex *tu = new TLatex(22.7,1300,"#minus t, GeV^{2}");
 tu->SetTextSize(0.04);
 TLatex *td = new TLatex(23.0,0.05,"T_{R}, MeV");
 td->SetTextSize(0.04);

//----------------------------------------------------------------
// Drawing TGraphs, labels and saving of Figure
//
 TCanvas *canv = new TCanvas("canv","fig1",900,600);
 canv->SetLogy();

 gr1->Draw("AL");
 axis->Draw();
 tl->Draw();
 tr->Draw();
 tf->Draw();
 tu->Draw();
 td->Draw();

// canv->Print("Fig1_epXS_0.84fm.png");
// canv->Print("Fig1_epXS_0.84fm.eps");


 double xs_el = 0;
 double dtt = 0.0000518/1.5;
 double mtt = 0.353282;
 for(double tt=1.5*dtt ; tt<mtt; tt = tt + dtt ){
     xs_el = xs_el + dtt * epXS( 0.720, tt , 0.84 ) ; // XS with R_proton = 0.84 fm.
 }
 cout << "xs elastic ( " << 1.5*dtt << " < t < " << mtt << " GeV^2) : " << xs_el << " mb\n\n\n";

 cout << "xs NSxs : " << epXS(0.72,-18765.44*0.001*0.001,0.00) << "\n";
 cout << "xs 0.84 : " << epXS(0.72,-18765.44*0.001*0.001,0.84) << "\n";
 cout << "xs 0.88w: " << epXS(0.72,-1.0005*18765.44*0.001*0.001,0.88) << "\n";
 cout << "xs 0.88 : " << epXS(0.72,-18765.44*0.001*0.001,0.88) << "\n";
 
 double xs_84  = epXS(0.72,-18765.44*0.001*0.001,0.84);
 double xs_88  = epXS(0.72,-18765.44*0.001*0.001,0.88);
 double xs_88w = epXS(0.72,-1.0005*18765.44*0.001*0.001,0.88);
 cout << 2.*(xs_88-xs_84)/(xs_88+xs_84) << "\n";
 cout << 2.*(xs_88w-xs_84)/(xs_88w+xs_84) << "\n";
//----------------------------------------------------------------
// END OF MACRO
//----------------------------------------------------------------
}
