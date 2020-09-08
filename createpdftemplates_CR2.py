from ROOT import *
import sys
import numpy

ct_top = '(weight_sfmu_ID)*(weight_pu)*(weight_sfmu_TRK)*(weight_sfmu_HLT)*(wgtMC__ttagSF_ct)*(weight_csv_central)*(wgtMC__topptREWGT_ct)'
systematic_direction_ttbar={'nominal':ct_top}
systematic_direction_wjets={'nominal':ct_top}

for i in range(0,100):
    pdfstring  = '*(wgtMC__PDF['+str(i)+'])'
    systematic_direction_ttbar['wgtMC__PDF_'+str(i)] = ct_top+pdfstring
    systematic_direction_wjets['wgtMC__PDF_'+str(i)] = ct_top+pdfstring

samplelist = {
'ttbar':'uhh2.AnalysisModuleRunner.MC.TTbar.root',
'wjets_l':'uhh2.AnalysisModuleRunner.MC.WJets__L.root'
}

categories=['NT1']
fout = TFile('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/mu_Test_4cat_PDF_CR2.root', 'recreate')

fout.mkdir("CR2")
fout.mkdir("CR2/ttbar")
fout.mkdir("CR2/singletop")
fout.mkdir("CR2/data_obs")
fout.mkdir("CR2/wjets_l")
fout.mkdir("CR2/ZprimeNarrow3000")
fout.mkdir("CR2/ZprimeNarrow1500")
fout.mkdir("CR2/DY")
fout.mkdir("CR2/wjets_c")
fout.mkdir("CR2/wjets_b")


gROOT.SetBatch(kTRUE)

for cat in categories:
    cut_string_GL='(muoN==1 & Mttbar<2000 & Mttbar>200 &'
    if cat == 'NT1':
        a=0
        cut_string = cut_string_GL+' WJets_TMVA_response < 0.5 & WJets_TMVA_response > 0 & rec_chi2<30  '
        for key_sample in samplelist:
            if key_sample == 'QCD':
                continue
            myfile = TFile(samplelist[key_sample])
            mytree = myfile.Get("AnalysisTree")
            mytree.SetAlias("invmass","Mttbar")
            gDirectory.cd('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/mu_Test_4cat_PDF_CR2.root:/CR2/'+key_sample)
            if key_sample == 'DATA':
                gDirectory.cd('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/mu_Test_4cat_PDF_CR2.root:/CR2/data_obs')
                print("--------------------------------------")
                cut = str(cut_string+' & ttagN==0 & btagN>=0)')
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
                        temp2sys = TH1F("temp2sys","temp2sys",20,200,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(syst)
                        gDirectory.WriteObject(temp2sys,syst)
                        del temp2sys
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
                        temp2sys = TH1F("temp2sys","temp2sys",20,200,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(syst)
                        gDirectory.WriteObject(temp2sys,syst)
                        del temp2sys
            elif 'wjets_l' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_wjets[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",20,200,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(syst)
                        gDirectory.WriteObject(temp2,syst)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",20,200,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(syst)
                        gDirectory.WriteObject(temp2sys,syst)
                        del temp2sys
            elif 'singletop' or 'DY' or 'wjets_b' or 'wjets_c' in key_sample:
                for syst in systematic_direction_wjets:
                    cut = str(cut_string+' & ttagN==0 & btagN>=0)*(wgtMC__GEN)*'+systematic_direction_otherbkgs[syst])
                    print "Processing: ",key_sample
                    print "Applying cut:",cut
                    if syst == 'nominal':
                        temp2 = TH1F("temp2","temp2",20,200,2000)
                        mytree.Draw("invmass>>temp2",cut)
                        temp2.SetName(syst)
                        gDirectory.WriteObject(temp2,syst)
                        del temp2
                    elif 'nominal' not in syst:
                        temp2sys = TH1F("temp2sys","temp2sys",20,200,2000)
                        mytree.Draw("invmass>>temp2sys",cut)
                        temp2sys.SetName(syst)
                        gDirectory.WriteObject(temp2sys,syst)
                        del temp2sys
