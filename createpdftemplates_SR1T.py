from ROOT import *
import sys
import numpy

ct_top = '(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)*(wgtMC__topptREWGT_ct)'
systematic_direction_ttbar={'nominal':ct_top}

for i in range(0,100):
    pdfstring  = '*(wgtMC__PDF['+str(i)+'])'
    systematic_direction_ttbar['wgtMC__PDF_'+str(i)] = ct_top+pdfstring

samplelist = {
'ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root',
}

categories=['T1']
fout = TFile('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/mu_Test_4cat_PDF_SR1T.root', 'recreate')

fout.mkdir("SR1T")
fout.mkdir("SR1T/data_obs")
fout.mkdir("SR1T/ttbar")
fout.mkdir("SR1T/wjets_c")
fout.mkdir("SR1T/wjets_b")
fout.mkdir("SR1T/singletop")
fout.mkdir("SR1T/wjets_l")
fout.mkdir("SR1T/ZprimeNarrow3000")
fout.mkdir("SR1T/ZprimeNarrow1500")
gROOT.SetBatch(kTRUE)
                               
for cat in categories:
    cut_string_GL='(muoN==1 & Mttbar<2000 & Mttbar>200 &'
    if cat == 'T1':
        cut_string = cut_string_GL+' WJets_TMVA_response>=0.5 & rec_chi2<30  '
        a=0
        for key_sample in samplelist:
            if key_sample == 'QCD':
                continue
            myfile = TFile(samplelist[key_sample])
            mytree = myfile.Get("AnalysisTree")
            mytree.SetAlias("invmass","Mttbar")
            gDirectory.cd('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/mu_Test_4cat_PDF_SR1T.root:/SR1T/'+key_sample)
            if key_sample == 'DATA':
                gDirectory.cd('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/mu_Test_4cat_PDF_SR1T.root:/SR1T/data_obs')
                cut = str(cut_string+' & ttagN==1 & btagN>=0)')
                print("--------------------------------------")
                print "Processing: ",key_sample
                print "Applying cut:",cut
                tempdata = TH1F("tempdata","tempdata",20,200,2000)
                mytree.Draw("invmass>>tempdata",cut)
                tempdata.SetName(key_sample)
                gDirectory.WriteObject(tempdata,'nominal')
                del tempdata
            elif 'Zprime'in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print("--------------------------------------")
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",20,200,2000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(syst)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        gDirectory.WriteObject(temp,syst)
                        del temp
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",20,200,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(syst)
                        gDirectory.WriteObject(temp2sys,syst)
                        del temp2sys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==1 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print("--------------------------------------")
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",20,200,2000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(syst)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        gDirectory.WriteObject(temp,syst)
                        del temp
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",20,200,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(syst)
                        gDirectory.WriteObject(temp2sys,syst)
                        del temp2sys
            elif 'wjets_l' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' &  ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print("--------------------------------------")
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",140,200,7000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(syst)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        gDirectory.WriteObject(temp,syst)
                        del temp
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",140,200,7000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(syst)
                        gDirectory.WriteObject(temp2sys,syst)
                        del temp2sys
            elif 'singletop' or 'DY' or 'wjets_c' or 'wjets_b' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' &  ttagN==1 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print("--------------------------------------")
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp = TH1F("temp","temp",140,200,7000)
                        mytree.Draw("invmass>>temp",cut)
                        temp.SetName(syst)
                        print "Rebinning T1 nom:", str(temp.GetNbinsX())
                        gDirectory.WriteObject(temp,syst)
                        del temp
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",140,200,7000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(syst)
                        gDirectory.WriteObject(temp2sys,syst)
                        del temp2sys


