#!/usr/bin/env bash

python Templates_4cat.py
python rebin_Combine.py  

python createpdftemplates_CR1.py
python createpdftemplates_CR2.py
python createpdftemplates_SR0T.py
python createpdftemplates_SR1T.py
python createq2templates_CR1.py
python createq2templates_CR2.py
python createq2templates_SR0T.py
python createq2templates_SR1T.py

python rebin_Combine_pdfCR1.py
python rebin_Combine_pdfCR2.py
python rebin_Combine_pdfSR0T.py
python rebin_Combine_pdfSR1T.py
python rebin_Combine_q2CR1.py
python rebin_Combine_q2CR2.py
python rebin_Combine_q2SR0T.py
python rebin_Combine_q2SR1T.py

python New_PDF_CR1.py
python New_PDF_CR2.py
python New_PDF_SR0T.py
python New_PDF_SR1T.py
python New_q2_CR1.py
python New_q2_CR2.py
python New_q2_SR0T.py
python New_q2_SR1T.py

python Full_sys.py

combineCards.py SR1T_muon=SR1T_muon.txt SR0T_muon=SR0T_muon.txt CR1_muon=CR1_muon.txt CR2_muon=CR2_muon.txt > Combined_muon.txt
text2workspace.py Combined_muon.txt
combine -M MultiDimFit -d Combined_muon.txt --robustFit 1 -v 2 --saveFitResult --freezeParameters r --setParameters r=0
PostFitShapesFromWorkspace -d Combined_muon.txt -w Combined_muon.root -o MDF_shapes.root -f multidimfit.root:fit_mdf --postfit --sampling --print --freeze r=0


combineTool.py -M Impacts -d Combined_muon.root -m 121 --doInitialFit --robustFit 1 --freezeParameters r --setParameters r=0 -t -1 --expectSignal 1
combineTool.py -M Impacts -d Combined_muon.root -m 121 --doFits --robustFit 1 --freezeParameters r --setParameters r=0 -t -1 --expectSignal 1
combineTool.py -M Impacts -d Combined_muon.root -m 121 -o impacts.json
plotImpacts.py -i impacts.json -o impacts




