

#! /usr/bin/env python

import sys
#sys.argv.append('-b')

import ROOT
import array
ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetOptStat(000000000)
ROOT.gStyle.SetOptTitle(0)

from ROOT import TCanvas, TFile, TH1, THStack, TLegend

list_files = {}
list_textfiles = {}
list_syst = {}


Rootfile = TFile("Limit_template.root")
keys = Rootfile.GetListOfKeys()

channels = []
cnst = 0
for key in keys:
        a = key.GetName()
	channels.append(a)
        list_textfiles[cnst] = a+"_muon.txt"
        cnst = cnst + 1

dir = Rootfile.GetDirectory(channels[0])
dirs = dir.GetListOfKeys()


proc = []

for di in dirs:
       b = di.GetName()
       if b == 'data_obs':
		 continue
       if b[0:2] == 'Zp':
           if b == sys.argv[1]:
	       proc.append(b)
           else:
	       continue 
       else:
           proc.append(b)
       

proc.sort()
proc = list(dict.fromkeys(proc))
proc.sort()
'''
proc.remove("ZprimeNarrow0500")
proc.remove("ZprimeNarrow0750")
proc.remove("ZprimeNarrow1000")
proc.remove("ZprimeNarrow1250")
proc.remove("ZprimeNarrow1500")
proc.remove("ZprimeNarrow2000")
proc.remove("ZprimeNarrow2500")
proc.remove("ZprimeNarrow3000")
proc.remove("ZprimeNarrow3500")
proc.remove("ZprimeNarrow4000")
proc.remove("ZprimeNarrow4500")
proc.remove("ZprimeNarrow5000")
proc.remove("ZprimeNarrow6000")
proc.remove("ZprimeNarrow6500")
proc.remove("ZprimeNarrow7000")

proc.remove("ZprimeWide0500")
proc.remove("ZprimeWide0750")
proc.remove("ZprimeWide1000")
proc.remove("ZprimeWide1250")
proc.remove("ZprimeWide1500")
proc.remove("ZprimeWide2000")
proc.remove("ZprimeWide2500")
proc.remove("ZprimeWide3000")
proc.remove("ZprimeWide3500")
proc.remove("ZprimeWide4000")
proc.remove("ZprimeWide4500")
proc.remove("ZprimeWide5000")
proc.remove("ZprimeWide6000")
proc.remove("ZprimeWide6500")
proc.remove("ZprimeWide7000")

proc.remove("ZprimeUltraWide1000")
proc.remove("ZprimeUltraWide2000")
proc.remove("ZprimeUltraWide3000")
proc.remove("ZprimeUltraWide4000")
proc.remove("ZprimeUltraWide5000")
proc.remove("ZprimeUltraWide6000")
proc.remove("ZprimeUltraWide6500")
proc.remove("ZprimeUltraWide7000")

proc.remove("ZprimeJets0500")
proc.remove("ZprimeJets0750")
proc.remove("ZprimeJets1000")
proc.remove("ZprimeJets1250")
proc.remove("ZprimeJets1500")
proc.remove("ZprimeJets2000")
proc.remove("ZprimeJets2500")
proc.remove("ZprimeJets3000")
proc.remove("ZprimeJets3500")
proc.remove("ZprimeJets4000")
'''
print(proc)

for element in proc:
	if element.islower():
		index = proc.index(element)
		break


syst = []
for i_c in range(len(channels)): 
	for i_p in range(len(proc)):
		sys1 = Rootfile.GetDirectory(channels[i_c]+'/'+proc[i_p])
		syst1 = sys1.GetListOfKeys()
#		print(syst1)
		temp_sys = []
		for obj in syst1:
			objN = obj.GetName()
			if objN.endswith('Down'):
				continue
			objN = objN[:-2]
        		syst.append(objN)
			temp_sys.append(objN)
			list_syst[len(proc)*i_c + i_p] = temp_sys
		del sys1	
		del syst1
		del temp_sys

#print(syst)
syst = list(dict.fromkeys(syst))
syst.remove('nomin') 
#print(syst)
#for www in range(len(list_syst)):
#	print(list_syst[www])
#print(list_syst)


for x in range(len(channels)):
	list_files["file_{0}".format(x)] = open(list_textfiles[x],"w+")
	list_files["file_{0}".format(x)].write("imax 1 number of categories\n")
	list_files["file_{0}".format(x)].write("jmax * number of samples minus one\n")
	list_files["file_{0}".format(x)].write("kmax * number of nuisance parameters\n")
	list_files["file_{0}".format(x)].write("---------------------------------------------------\n")
	list_files["file_{0}".format(x)].write("shapes * * Limit_template.root $CHANNEL/$PROCESS/nominal $CHANNEL/$PROCESS/$SYSTEMATIC\n")
	list_files["file_{0}".format(x)].write("---------------------------------------------------\n")
	list_files["file_{0}".format(x)].write('bin '+channels[x]+'\n')
	list_files["file_{0}".format(x)].write('observation -1\n')
	list_files["file_{0}".format(x)].write("---------------------------------------------------\n")
	list_files["file_{0}".format(x)].write('bin ')
	for y in range(len(proc)):
		list_files["file_{0}".format(x)].write(channels[x]+' ')
	list_files["file_{0}".format(x)].write('\nprocess ')
	for z in range(-1*index+1,len(proc)-index+1):
		list_files["file_{0}".format(x)].write(str(z)+' ')
	list_files["file_{0}".format(x)].write('\nprocess ')   
	for v in range(len(proc)):
       		list_files["file_{0}".format(x)].write(proc[v]+' ')
	list_files["file_{0}".format(x)].write('\nrate ')
	for w in range(-1*index+1,len(proc)-index+1):
        	list_files["file_{0}".format(x)].write('-1 ')
        list_files["file_{0}".format(x)].write("\n---------------------------------------------------\n")

        list_files["file_{0}".format(x)].write('lumi lnN ')

	for xx in range(len(proc)):
                list_files["file_{0}".format(x)].write('1.025 ')

        list_files["file_{0}".format(x)].write("\n---------------------------------------------------\n")

	for el in syst:
                if el == 'toptag':
			continue
		list_files["file_{0}".format(x)].write(el+' shape ')
        	for xxx in range(len(proc)):
			if el in list_syst[len(proc)*x + xxx]:
				list_files["file_{0}".format(x)].write('1 ')
			else: 
                                list_files["file_{0}".format(x)].write('0 ')				
		list_files["file_{0}".format(x)].write('\n')
	list_files["file_{0}".format(x)].write("---------------------------------------------------\n")
	list_files["file_{0}".format(x)].write("ttbar_rate rateParam * ttbar 1\n")
	list_files["file_{0}".format(x)].write("ttbar_rate param 1.0 0.20\n")
        list_files["file_{0}".format(x)].write("wl_rate rateParam * wjets_l 1\n")
        list_files["file_{0}".format(x)].write("wl_rate param 1.0 0.25\n")
        list_files["file_{0}".format(x)].write("ST_rate rateParam * singletop 1\n")
        list_files["file_{0}".format(x)].write("ST_rate param 1.0 0.50\n")	

        list_files["file_{0}".format(x)].write("other_rate rateParam * wjets_b 1\n")
        list_files["file_{0}".format(x)].write("other_rate param 1.0 0.50\n")

        list_files["file_{0}".format(x)].write("other_rate rateParam * wjets_c 1\n")
        list_files["file_{0}".format(x)].write("other_rate param 1.0 0.50\n")

        list_files["file_{0}".format(x)].write("other_rate rateParam * dy 1\n")
        list_files["file_{0}".format(x)].write("other_rate param 1.0 0.50\n")

        list_files["file_{0}".format(x)].write("other_rate rateParam * qcd 1\n")
        list_files["file_{0}".format(x)].write("other_rate param 1.0 0.50\n")
  
        list_files["file_{0}".format(x)].write("toptag rateParam * * 1 [0,5]\n")

