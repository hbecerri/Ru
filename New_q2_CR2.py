import ROOT as R
import sys
import numpy as np
import math

nbins = 140
file = R.TFile("rebin_q2_CR2.root")
#file = R.TFile("mu_Test_4cat_q2_CR2.root")
values_per_bin_ttbar = {}
sigmas = []
for i in range(20):
    values_per_bin_ttbar[str(i)]  = []
#get values per bin
proc = ['ttbar']
h_bkg = {}
h_tmp_q2 = {}
h_q2 = {}
file.cd('')
R.gDirectory.cd('CR2/ttbar')
dir = R.gDirectory.GetListOfKeys()

for key in dir:
    a = key.GetName()
    h_bkg[a] = file.Get('CR2/ttbar/'+a).Clone()

for i in range(1,h_bkg['nominal'].GetNbinsX()+1):
    h_tmp_q2[str(i)]=R.TH1F("q2"+str(i),"q2"+str(i), 8000, 0., 40000.)

for key1 in dir:
    b = key1.GetName()
    print(b)
    if b == 'nominal':
	continue
    for i in range(1,h_bkg[b].GetNbinsX()+1):
        value = h_bkg[b].GetBinContent(i)
        h_tmp_q2[str(i)].Fill(value)

bin = h_bkg['nominal'].GetNbinsX()+1
h_q2["q2Up"] = h_bkg['q2ttbarMuRdnMuFdn__plus'].Clone()
h_q2["q2Up"].SetName("q2Up")
h_q2["q2Up"].SetTitle("q2Up")
h_q2["q2Down"] = h_bkg['q2ttbarMuRdnMuFdn__plus'].Clone()
h_q2["q2Down"].SetName("q2Down")
h_q2["q2Down"].SetTitle("q2Down")

for i in range(1,bin):
    h_q2["q2Up"].SetBinContent(i,h_tmp_q2[str(i)].GetMean()+h_tmp_q2[str(i)].GetRMS())
    h_q2["q2Down"].SetBinContent(i,h_tmp_q2[str(i)].GetMean()-h_tmp_q2[str(i)].GetRMS())

fout = R.TFile("templates_q2_CR2.root", 'recreate')
fout.mkdir('CR2/ttbar')
fout.cd("CR2/ttbar")
R.gDirectory.WriteObject(h_q2["q2Up"],"q2ttbarUp" )
R.gDirectory.WriteObject(h_q2["q2Down"],"q2ttbarDown" )


proc2 = ['wjets_l']
h_bkg2 = {}
h_tmp_q22 = {}
h_q22 = {}
file.cd('')
R.gDirectory.cd('CR2/wjets_l')
dir = R.gDirectory.GetListOfKeys()

for key in dir:
    a = key.GetName()
    h_bkg2[a] = file.Get('CR2/wjets_l/'+a).Clone()

for i in range(1,h_bkg2['nominal'].GetNbinsX()+1):
    h_tmp_q22[str(i)]=R.TH1F("q2"+str(i),"q2"+str(i), 8000, 0., 40000.)

for key1 in dir:
    b = key1.GetName()
    print(b)
    if b == 'nominal':
        continue
    for i in range(1,h_bkg2[b].GetNbinsX()+1):
        value = h_bkg2[b].GetBinContent(i)
        h_tmp_q22[str(i)].Fill(value)

bin = h_bkg2['nominal'].GetNbinsX()+1
h_q22["q2Up"] = h_bkg2['q2wjetsMuRdnMuFdn__plus'].Clone()
h_q22["q2Up"].SetName("q2Up")
h_q22["q2Up"].SetTitle("q2Up")
h_q22["q2Down"] = h_bkg2['q2wjetsMuRdnMuFdn__plus'].Clone()
h_q22["q2Down"].SetName("q2Down")
h_q22["q2Down"].SetTitle("q2Down")

for i in range(1,bin):
    h_q22["q2Up"].SetBinContent(i,h_tmp_q22[str(i)].GetMean()+h_tmp_q22[str(i)].GetRMS())
    h_q22["q2Down"].SetBinContent(i,h_tmp_q22[str(i)].GetMean()-h_tmp_q22[str(i)].GetRMS())

fout.mkdir('CR2/wjets_l')
fout.cd("CR2/wjets_l")
R.gDirectory.WriteObject(h_q22["q2Up"],"q2wjetsUp" )
R.gDirectory.WriteObject(h_q22["q2Down"],"q2wjetsDown" )
