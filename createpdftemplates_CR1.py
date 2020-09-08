from ROOT import *
import sys
import numpy

ct_top = '(wgtMC__topptREWGT_ct)*(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)'
systematic_direction_ttbar={'nominal':ct_top}
systematic_direction_wjets={'nominal':ct_top}

for i in range(0,100):
    pdfstring  = '*(wgtMC__PDF['+str(i)+'])'
    systematic_direction_ttbar['wgtMC__PDF_'+str(i)] = ct_top+pdfstring
    systematic_direction_wjets['wgtMC__PDF_'+str(i)] = ct_top+pdfstring

samplelist = {
#'singletop':'uhh2.AnalysisModuleRunner.MC.ST.root',
#'QCD':'uhh2.AnalysisModuleRunner.MC.QCD_Pt.root',
#'DY':'uhh2.AnalysisModuleRunner.MC.DY.root',
'wjets_l':'uhh2.AnalysisModuleRunner.MC.WJets__L.root',
#'wjets_b':'uhh2.AnalysisModuleRunner.MC.WJets__B.root',
#'wjets_c':'uhh2.AnalysisModuleRunner.MC.WJets__C.root',
'ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root'
#'ZprimeNarrow1500':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M1500.root',
#'ZprimeNarrow3000':'uhh2.AnalysisModuleRunner.MC.ZprimeToTT_01w_M3000.root'
}

categories=['NT0']
fout = TFile('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/mu_Test_4cat_PDF_CR1.root', 'recreate')

fout.mkdir("CR1")
fout.mkdir("CR1/singletop")
fout.mkdir("CR1/data_obs")
fout.mkdir("CR1/wjets_l")
fout.mkdir("CR1/ZprimeNarrow3000")
fout.mkdir("CR1/ZprimeNarrow1500")
fout.mkdir("CR1/ttbar")
fout.mkdir("CR1/wjets_b")
fout.mkdir("CR1/wjets_c")
gROOT.SetBatch(kTRUE)
                               
for cat in categories:
    cut_string_GL='(muoN==1 & Mttbar<2000 & Mttbar>200 &'
    if cat == 'NT0':
        a=0
        cut_string = cut_string_GL+' WJets_TMVA_response < -0.75 & rec_chi2<30  '
        for key_sample in samplelist:
            if key_sample == 'QCD':
                continue
            myfile = TFile(samplelist[key_sample])
            mytree = myfile.Get("AnalysisTree")
            mytree.SetAlias("invmass","Mttbar")
            gDirectory.cd('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/mu_Test_4cat_PDF_CR1.root:/CR1/'+key_sample)
            if key_sample == 'DATA':
                gDirectory.cd('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/mu_Test_4cat_PDF_CR1.root:/CR1/data_obs')
                cut = str(cut_string+' & ttagN==0 & btagN>=0)')
                print("--------------------------------------")
                print "Processing: ",key_sample
                print "Applying cut:",cut
                temp2data = TH1F("temp2data","temp2data",20,200,2000)
                mytree.Draw("invmass>>temp2data",cut)
                temp2data.SetName(key_sample)
                gDirectory.WriteObject(temp2data,'nominal')
                del temp2data
            elif 'Zprime'in key_sample:
                for syst in systematic_direction_signal:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_signal[syst])
                    print("--------------------------------------")
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",20,200,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(syst)
                        gDirectory.WriteObject(temp2,syst)
                        del temp2
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",20,200,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(syst)
                        gDirectory.WriteObject(tempsys,syst)
                        del tempsys
            elif 'ttbar' in key_sample:
                for syst in systematic_direction_ttbar:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)*1.00*(wgtMC__GEN)*'+systematic_direction_ttbar[syst])
                    print("--------------------------------------")
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",20,200,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(syst)
                        gDirectory.WriteObject(temp2,syst)
                        del temp2
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",20,200,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(syst)
                        gDirectory.WriteObject(tempsys,syst)
                        del tempsys
            elif 'wjets_l' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print("--------------------------------------")
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",20,200,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(syst)
                        gDirectory.WriteObject(temp2,syst)
                        del temp2
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",20,200,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(syst)
                        gDirectory.WriteObject(tempsys,syst)
                        del tempsys
            elif 'singletop' or 'DY' or 'wjets_b' or 'wjets_c' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print("--------------------------------------")
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",20,200,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(syst)
                        gDirectory.WriteObject(temp2,syst)
                        del temp2
                    elif 'nominal' not in syst:
                        tempsys = TH1F("tempsys","tempsys",20,200,2000)
                        mytree.Draw("invmass>>tempsys",cut)
                        tempsys.SetName(syst)
                        gDirectory.WriteObject(tempsys,syst)
                        del tempsys
