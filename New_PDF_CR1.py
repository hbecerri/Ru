
import ROOT as R
import sys
import numpy as np
import math

nbins = 140
file = R.TFile("rebin_PDF_CR1.root")
#file = R.TFile("mu_Test_4cat_PDF_CR1.root")
values_per_bin_ttbar = {}
sigmas = []
for i in range(140):
    values_per_bin_ttbar[str(i)]  = []
#get values per bin
proc = ['ttbar']
h_bkg = {}
h_tmp_PDF = {}
h_PDF = {}
file.cd('')
R.gDirectory.cd('CR1/ttbar')
dir = R.gDirectory.GetListOfKeys()

for key in dir:
    a = key.GetName()
    h_bkg[a] = file.Get('CR1/ttbar/'+a).Clone()

for i in range(1,h_bkg['wgtMC__PDF_0'].GetNbinsX()+1):
    h_tmp_PDF[str(i)]=R.TH1F("PDF"+str(i),"PDF"+str(i), 1000, 0., 1.)

for key1 in dir:
    b = key1.GetName()
    for i in range(1,h_bkg[b].GetNbinsX()+1):
        value = h_bkg[b].GetBinContent(i)
        normal = h_bkg['wgtMC__PDF_0'].GetBinContent(i)
        if value>0 and normal>0: 
            h_tmp_PDF[str(i)].Fill(value/normal)

bin = h_bkg['wgtMC__PDF_0'].GetNbinsX()+1
h_PDF["PDFUp"] = h_bkg['wgtMC__PDF_0'].Clone()
h_PDF["PDFUp"].SetName("PDFUp")
h_PDF["PDFUp"].SetTitle("PDFUp")
h_PDF["PDFDown"] = h_bkg['wgtMC__PDF_0'].Clone()
h_PDF["PDFDown"].SetName("PDFDown")
h_PDF["PDFDown"].SetTitle("PDFDown")
for i in range(1,bin):
    normal = h_bkg['nominal'].GetBinContent(i)
    h_PDF["PDFUp"].SetBinContent(i,normal*(h_tmp_PDF[str(i)].GetMean()+h_tmp_PDF[str(i)].GetRMS()))
    h_PDF["PDFDown"].SetBinContent(i,normal*(h_tmp_PDF[str(i)].GetMean()-h_tmp_PDF[str(i)].GetRMS()))
#h_PDF["PDFUp"].Draw()

fout = R.TFile("templates_pdf_CR1.root", 'recreate')
fout.mkdir('CR1/ttbar')
fout.cd("CR1/ttbar")
R.gDirectory.WriteObject(h_PDF["PDFUp"],"PDFUp" )
R.gDirectory.WriteObject(h_PDF["PDFDown"],"PDFDown" )
 

###########################################


proc2 = ['wjets_l']
h_bkg2 = {}
h_tmp_PDF2 = {}
h_PDF2 = {}
file.cd('')
R.gDirectory.cd('CR1/wjets_l')
dir = R.gDirectory.GetListOfKeys()

for key in dir:
    a = key.GetName()
    h_bkg2[a] = file.Get('CR1/wjets_l/'+a).Clone()

for i in range(1,h_bkg['wgtMC__PDF_0'].GetNbinsX()+1):
    h_tmp_PDF2[str(i)]=R.TH1F("PDF"+str(i),"PDF"+str(i), 1000, 0., 1.)

for key1 in dir:
    b = key1.GetName()
    for i in range(1,h_bkg2[b].GetNbinsX()+1):
        value = h_bkg2[b].GetBinContent(i)
        normal = h_bkg2['wgtMC__PDF_0'].GetBinContent(i)
        if value>0 and normal>0:
            h_tmp_PDF2[str(i)].Fill(value/normal)

bin = h_bkg2['wgtMC__PDF_0'].GetNbinsX()+1
h_PDF2["PDFUp"] = h_bkg2['wgtMC__PDF_0'].Clone()
h_PDF2["PDFUp"].SetName("PDFUp")
h_PDF2["PDFUp"].SetTitle("PDFUp")
h_PDF2["PDFDown"] = h_bkg2['wgtMC__PDF_0'].Clone()
h_PDF2["PDFDown"].SetName("PDFDown")
h_PDF2["PDFDown"].SetTitle("PDFDown")
for i in range(1,bin):
    normal = h_bkg2['nominal'].GetBinContent(i)
    h_PDF2["PDFUp"].SetBinContent(i,normal*(h_tmp_PDF2[str(i)].GetMean()+h_tmp_PDF2[str(i)].GetRMS()))
    h_PDF2["PDFDown"].SetBinContent(i,normal*(h_tmp_PDF2[str(i)].GetMean()-h_tmp_PDF2[str(i)].GetRMS()))
#h_PDF["PDFUp"].Draw()

fout.mkdir('CR1/wjets_l')
fout.cd("CR1/wjets_l")
R.gDirectory.WriteObject(h_PDF2["PDFUp"],"PDFUp" )
R.gDirectory.WriteObject(h_PDF2["PDFDown"],"PDFDown" )




