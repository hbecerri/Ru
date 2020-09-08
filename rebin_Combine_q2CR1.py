import sys
sys.argv.append('-b')

import ROOT
from ROOT import *
import math
import array

def createCanvasPads():
    c = TCanvas("c", "canvas", 800, 800)
     # Upper histogram plot is pad1
    pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0)  # joins upper and lower plot
    pad1.SetGridx()
    pad1.Draw()
    # Lower ratio plot is pad2
    c.cd()  # returns to main canvas before defining pad2
    pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0)  # joins upper and lower plot
    pad2.SetBottomMargin(0.2)
    pad2.SetGridx()
    pad2.Draw()
    return c, pad1, pad2

def findMaximum(histogram):
    index = 1
    maximum = 0
    for i in range(1,histogram.GetNbinsX()+1):
        if histogram.GetBinContent(i) > maximum:
            maximum = histogram.GetBinContent(i)
            index = i
    return index, maximum


def findLowIndex(histogram, rerror):
    value = 0.0
    error = 0.0
    index, maximum = findMaximum(histogram)
    for i in range(1,histogram.GetNbinsX()+1):
        value = value + histogram.GetBinContent(i)
        error = math.sqrt(error**2+histogram.GetBinError(i)**2)
        if value > maximum and i > 1:
            return i-1
        elif value > maximum and i < 1:
            return 1
        ratio = 1.0
        if value != 0: ratio = error/value
        if ratio < rerror:
            return i


def findBinSize(histogram, highindexes, rerror, minvalue, maxbinsize, start, stop):

    value = 0.0
    error = 0.0
    for i in range(start, stop, -1):
        value = value + histogram.GetBinContent(i)
        error = math.sqrt(error**2+histogram.GetBinError(i)**2)
        ratio = 1.0
        binsize = start - i + 1
        if value != 0: ratio = error/value
        # if ratio < rerror and value*(1+ratio) >= minvalue:
        if ratio < rerror:
            if binsize <= maxbinsize:
                highindexes.append(i)
                if not findBinSize(histogram, highindexes, rerror, value, binsize, i-1, stop):
                    highindexes.pop()
                    continue
                return True
            else:
                return False
    # highindexes.append(stop+1)
    return True


def computeBinning(histogram, rerror):
    highindexes = []
    lowindex = findLowIndex(histogram, rerror)
    maxindex, maximum = findMaximum(histogram)
    findBinSize(histogram, highindexes, rerror, 0, histogram.GetNbinsX(), histogram.GetNbinsX(), lowindex)
    highindexes = sorted(highindexes)
    binning = [histogram.GetBinLowEdge(0), histogram.GetBinLowEdge(lowindex)+histogram.GetBinWidth(lowindex)]
    for i in highindexes[1:]:
        binning.append(histogram.GetBinLowEdge(i))
    binning.append(histogram.GetBinLowEdge(histogram.GetNbinsX())+histogram.GetBinWidth(histogram.GetNbinsX()))
    return binning

channel = ['CR1']
proc = ['ttbar','wjets_l']
channel2 = ['SR1T','SR0T','CR1','CR2']
proc2 = ['ZprimeNarrow3000', 'singletop', 'ttbar', 'wjets_l','data_obs','ZprimeNarrow1500','QCD','wjets_b','wjets_c','DY']
fout = TFile('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/rebin_q2_CR1.root', 'recreate')

for t in channel2:
    for p in proc2:
        fout.mkdir(t+'/'+p)

list_syst = {}
tempdata1 = TH1F("tempdata1","tempdata1",20,200,2000)
tempdata2 = TH1F("tempdata2","tempdata2",20,200,2000)
tempdata3 = TH1F("tempdata3","tempdata3",20,200,2000)
tempdata4 = TH1F("tempdata4","tempdata4",20,200,2000)
for ch in channel2:
    for pr in proc2:
	print(ch+'/'+pr)
        myfile = TFile('mu_Test_4cat.root')
        gDirectory.cd('mu_Test_4cat.root:/'+ch+'/'+pr)
        dir = gDirectory.GetListOfKeys()
        a = 1
        for key_dir in dir:
		name  = key_dir.GetName()
                if a == 1:
			list_syst[ch+pr] = [name]
		else:
	                list_syst[ch+pr].append(name)
                a = a + 1  

        if pr == 'ZprimeNarrow3000' or pr == 'ZprimeNarrow1500':
                continue
        myhisto = gDirectory.Get('nominal').Clone()
        if pr == 'data_obs':
            continue
        else:
            if ch == 'SR1T':
                    tempdata1.Add(myhisto)
            elif ch == 'SR0T':
                    tempdata2.Add(myhisto)
            elif ch == 'CR1':
                    tempdata3.Add(myhisto)
            elif ch == 'CR2':
                    tempdata4.Add(myhisto)
    
    if ch == 'SR1T':
        binning1 = array.array('d', computeBinning(tempdata1, 0.10))
    elif ch == 'SR0T':
        binning2 = array.array('d', computeBinning(tempdata2, 0.10))
    elif ch == 'CR1':
        binning3 = array.array('d', computeBinning(tempdata3, 0.10))
    elif ch == 'CR2':
        binning4 = array.array('d', computeBinning(tempdata4, 0.10))


for ch in channel:
    for pr in proc:
        if ch == 'CR1':
                myfile = TFile('mu_Test_4cat_q2_CR1.root')
                gDirectory.cd('mu_Test_4cat_q2_CR1.root:/'+ch+'/'+pr)
                dir2 = gDirectory.GetListOfKeys()
		for key_2 in dir2:
                         n  = key_2.GetName()
		         print(ch+'/'+pr+'_'+n)
                         gDirectory.cd('mu_Test_4cat_q2_CR1.root:/'+ch+'/'+pr)
	                 myhisto = gDirectory.Get(n).Clone()
                    	 myhisto = myhisto.Rebin(len(binning3)-1, 'myhisto', binning3)
#                         myhisto = myhisto.Rebin(10, 'myhisto')
                         fout.cd(ch+'/'+pr)
                         myhisto.Write(n)
		         del myhisto

