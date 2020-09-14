#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLatex.h>
#include <TGraphAsymmErrors.h>
#include "RooRealVar.h"
#include "TLegend.h"
#include "RooDataSet.h"
#include "RooDataHist.h"
#include "RooGaussian.h"
#include "TCanvas.h"

#include "RooPlot.h"
#include "TTree.h"
#include "TH1D.h"
#include "TRandom.h"
using namespace RooFit ;
using namespace std;
void Brazil()
{

    std::fstream myfile("ZprimeNarrow_limits.txt", std::ios_base::in);
Float_t Y[14];
Float_t twosd[14];
Float_t onesd[14];
Float_t exp[14];
Float_t onesu[14];
Float_t twosu[14];

    Float_t a;
    Int_t c1 = 0;
    Int_t c2 = 0;
    Int_t c3 = 0;
    Int_t c4 = 0;
    Int_t c5 = 0;
    Int_t c6 = 0;

    Int_t c = 0;
    while (myfile >> a)
    {
    c = c + 1;

    if (c % 6 == 1){
    Y[c1] = a;
    c1 = c1 + 1;
    }

    if (c % 6 == 2){
    twosd[c2] = a;
    c2 = c2 + 1;
    }

    if (c % 6 == 3){
    onesd[c3] = a;
    c3 = c3 + 1;
    }

    if (c % 6 == 4){
    exp[c4] = a;
    c4 = c4 + 1;
    }

    if (c % 6 == 5){
    onesu[c5] = a;
    c5 = c5 + 1;
    }

    if (c % 6 == 0){
    twosu[c6] = a;
    c6 = c6 + 1;
    }

    }



Float_t X[] = {500,750,1000,1250,1500,2000,2500,3000,4000,4500,5000,6000,6500,7000};
Float_t Zero[] = {0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0};
//Float_t Y[] = {48.0959,2.4252,0.6526,0.8091,0.1845,0.0867,0.0183,0.0128,0.0096,0.0085,0.0078,0.0060,0.0043,0.0035,0.0028};
//Float_t twosd[] = {32.8164,1.5791,0.3517,0.1608,0.0791,0.0290,0.0142,0.0083,0.0039,0.0028,0.0013,0.0013,0.0009,0.0009,0.0009};
//Float_t onesd[] = {45.6436,2.1354,0.4743,0.2166,0.1072,0.0391,0.0190,0.0113,0.0058,0.0041,0.0021,0.0015,0.0013,0.0013,0.0013};
//Float_t exp[] = {67.75,3.0625,0.6719,0.3096,0.1523,0.0571,0.0283,0.0171,0.0083,0.0063,0.0034,0.0034,0.0024,0.0024,0.0024};
//Float_t onesu[] = {101.5068,4.5030,0.9718,0.4515,0.2222,0.0858,0.0432,0.0272,0.0139,0.0100,0.0065,0.0056,0.0046,0.0046,0.0040};
//Float_t twosu[] = {146.4139,6.4381,1.3694,0.6486,0.3267,0.1298,0.0663,0.0423,0.0220,0.0167,0.0099,0.0095,0.0071,0.0071,0.0070};
 
 Float_t oneD[14]; 
 Float_t oneU[14]; 
 Float_t twoD[14]; 
 Float_t twoU[14];

 int i;
 for(i=0;i<14;i++){                
 oneD[i]=exp[i]-onesd[i];
 oneU[i]=onesu[i]-exp[i];
 twoD[i]=exp[i]-twosd[i];
 twoU[i]=twosu[i]-exp[i];
 }

    TCanvas* cc = new TCanvas("Scatter","Scatter",2400,1200) ;
     cc->Divide(1,1) ;
     cc->cd(1) ;
     gPad->SetLogy();

     auto mg  = new TMultiGraph();

     auto ge2 = new TGraphAsymmErrors(14, X, exp, Zero, Zero,twoD,twoU);
     ge2->SetFillColor(kYellow);
     ge2->GetXaxis()->SetTitle("Mttbar [GeV]");
     ge2->Draw("AP");
     mg->Add(ge2,"3l ALP");
   
     auto ge = new TGraphAsymmErrors(14, X, exp, Zero, Zero,oneD,oneU);
     ge->SetFillColor(kGreen);
     mg->Add(ge,"SAME 3l ALP");    

     auto ge3 = new TGraph(14,X,exp);
     ge3->SetLineStyle(2);
     mg->Add(ge3,"SAME L");	

     auto ge4 = new TGraph(14,X,Y);
     ge4->SetLineStyle(1);
     mg->Add(ge4,"SAME L");

    mg->Draw("aL");  
    mg->GetXaxis()->SetTitle("M_{Z'} [GeV]");
    mg->GetYaxis()->SetTitle("Upper limit on #sigma_{Z'} x B(Z' #rightarrow t#bar{t}) [pb]");

    auto legend = new TLegend(0.58,0.7,0.9,0.9);
    legend->AddEntry(ge4,"Observed (95% CL)","l");
    legend->AddEntry("ge3","Expected (95% CL)","l");
    legend->AddEntry("ge","#pm 1#sigma Expected","f");
    legend->AddEntry("ge2","#pm 2#sigma Expected","f");
//    legend->AddEntry("gr","Graph with error bars:);
    legend->Draw("same");
//    cc->BuildLegend();
    cc->Print("Brazil.pdf");

    ofstream latex;
    latex.open("Brazil_table.tex");
    latex << "\\documentclass{article}\n\n \\usepackage{rotating} \n \\begin{document} \n \\begin{sidewaystable} \n \\begin{tabular}{c c c c c} \n  \\hline \\hline\n";
    latex << "Signal Process & Expected limit & Expected limit (1 sigma) & Expected limit (2 sigma) & Observed limit \\\\ \\hline \n";  

    for(int q=0;q<14;q++){
    latex << X[q]; latex << "&"; latex << exp[q]; latex << "&" ; latex << onesd[q]; latex << " - "; latex << onesu[q]; latex << "&" ; latex << twosd[q]; latex << " - "; latex << twosu[q]; latex << "&" ; latex << Y[q]; latex << "\\\\ \n" ; 
    }
    latex << "\\hline \n";
    latex <<  "\\end{tabular} \n \\end{sidewaystable} \n \\end{document}";

    



}
