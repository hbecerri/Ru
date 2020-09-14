import array
import ROOT as R
import sys
import numpy as np

samplelist = {
'MDF':'MDF_shapes.root'
}

proc = ['ttbar', 'wjets_l','data_obs','singletop','wjets_c','dy','qcd']
proc2 = ['ZprimeNarrow0500','ZprimeNarrow0750','ZprimeNarrow1000','ZprimeNarrow1250','ZprimeNarrow1500','ZprimeNarrow2000','ZprimeNarrow2500','ZprimeNarrow3000','ZprimeNarrow3500','ZprimeNarrow4000','ZprimeNarrow4500','ZprimeNarrow5000','ZprimeNarrow6000','ZprimeNarrow6500','ZprimeNarrow7000',
            'ZprimeWide0500','ZprimeWide0750','ZprimeWide1000','ZprimeWide1250','ZprimeWide1500','ZprimeWide2000','ZprimeWide2500','ZprimeWide3000','ZprimeWide3500','ZprimeWide4000','ZprimeWide4500','ZprimeWide5000','ZprimeWide6000','ZprimeWide6500','ZprimeWide7000',
            'ZprimeUltraWide1000','ZprimeUltraWide2000','ZprimeUltraWide3000','ZprimeUltraWide4000','ZprimeUltraWide5000','ZprimeUltraWide6000','ZprimeUltraWide6500','ZprimeUltraWide7000',
            'ZprimeJets0500','ZprimeJets0750','ZprimeJets1000','ZprimeJets1250','ZprimeJets1500','ZprimeJets2000','ZprimeJets2500','ZprimeJets3000','ZprimeJets3500','ZprimeJets4000']
cat = ['SR1T_muon_postfit','SR0T_muon_postfit','CR1_muon_postfit','CR2_muon_postfit']
fout = R.TFile('/afs/desy.de/user/h/hugobg/public/theta/CMSSW_8_0_24/src/Combine_Limits/muon_mle/Limit_template.root', 'recreate')

for t in cat:
    for p in proc:
        if t[0:2] == 'SR':  
	        fout.mkdir(t[0:4]+'/'+p)
	else: 
		fout.mkdir(t[0:3]+'/'+p)

for key_sample in samplelist:
	fin = R.TFile(samplelist[key_sample])
        for key_c in cat:
		fin.cd(key_c)
       	        for key_p in proc:
                	temp = fin.Get(key_c+'/'+key_p)
                	fout.cd('')
 	                if key_c[0:2] == 'SR':
	                        fout.cd(key_c[0:4]+'/'+key_p)
        		else:
	                        fout.cd(key_c[0:3]+'/'+key_p)
                  	R.gDirectory.WriteObject(temp,'nominal')
                  	del temp

samplelist2 = {
'Full':'Full_sys_4cat_muon_7TeV.root'
}
for t2 in cat:
    for p2 in proc2:
        if t2[0:2] == 'SR':
                fout.mkdir(t2[0:4]+'/'+p2)
        else:
             	fout.mkdir(t2[0:3]+'/'+p2)

for key_sample2 in samplelist2:
	fin = R.TFile(samplelist2[key_sample2])
        for key_c2 in cat:
                for key_p2 in proc2:
                        if key_c2[0:2] == 'SR':
                            fin.cd(key_c2[0:4]+'/'+key_p2)
                        else:
                       	    fin.cd(key_c2[0:3]+'/'+key_p2)
			dir = R.gDirectory.GetListOfKeys()			#new
                        for key_dir in dir:
				name = key_dir.GetName()
                                if key_c2[0:2] == 'SR':
          	                	temp = fin.Get(key_c2[0:4]+'/'+key_p2+'/'+name)	
				else:
                                        temp = fin.Get(key_c2[0:3]+'/'+key_p2+'/'+name)
        	          	fout.cd('')
                                if key_c2[0:2] == 'SR':
                                    fout.cd(key_c2[0:4]+'/'+key_p2)
                                else:
                                    fout.cd(key_c2[0:3]+'/'+key_p2)
                	  	R.gDirectory.WriteObject(temp,name)
                  		del temp
samplelist3 = {
'Full':'Full_sys_4cat_muon.root'
}
for key_sample3 in samplelist3:
        fin = R.TFile(samplelist2[key_sample3])
        for key_c3 in cat:
                for key_p3 in proc:
                        if key_c3[0:2] == 'SR':
                            fin.cd(key_c3[0:4]+'/'+key_p3)
                        else:
                            fin.cd(key_c3[0:3]+'/'+key_p3)
                        dir2 = R.gDirectory.GetListOfKeys()                      #new
                        for key_dir2 in dir2:
                                name = key_dir2.GetName()
				if name == 'nominal':
					continue
                                if key_c3[0:2] == 'SR':
	                                temp = fin.Get(key_c3[0:4]+'/'+key_p3+'/'+name)
				else: 
                                        temp = fin.Get(key_c3[0:3]+'/'+key_p3+'/'+name)
                                fout.cd('')
                                if key_c3[0:2] == 'SR':
                                    fout.cd(key_c3[0:4]+'/'+key_p3)
                                else:
                                    fout.cd(key_c3[0:3]+'/'+key_p3)
                                R.gDirectory.WriteObject(temp,name)
                                del temp
