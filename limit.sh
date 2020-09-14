
#!/usr/bin/env bash

export TERM=linux
rm -f ZprimeNarrow_limits.txt
rm -f ZprimeWide_limits.txt
rm -f ZprimeUltraWide_limits.txt

declare -a arr=("ZprimeNarrow0500" "ZprimeNarrow0750" "ZprimeNarrow1000" "ZprimeNarrow1250" "ZprimeNarrow1500" "ZprimeNarrow2000" "ZprimeNarrow2500" "ZprimeNarrow3000" "ZprimeNarrow4000" "ZprimeNarrow4500" "ZprimeNarrow5000" "ZprimeNarrow6000" "ZprimeNarrow6500" "ZprimeNarrow7000")
#declare -a arr=("ZprimeNarrow2000")
for i in "${arr[@]}"
do
	python TxtDC_limits.py ${i}
	combineCards.py SR1T_muon=SR1T_muon.txt SR0T_muon=SR0T_muon.txt > Signal_Region.txt
        combineCards.py SR1T_muon=SR1T_muon.txt SR0T_muon=SR0T_muon.txt CR1_muon=CR1_muon.txt CR2_muon=CR2_muon.txt > Signal_Region.txt
        combine -M AsymptoticLimits Signal_Region.txt --noFitAsimov >> ZprimeNarrow_limits.txt
        sed -i 's/Done.*//g' ZprimeNarrow_limits.txt
        sed -i 's/Will.*//g' ZprimeNarrow_limits.txt
        sed -i 's/ <<<.*//g' ZprimeNarrow_limits.txt
        sed -i 's/--.*//g' ZprimeNarrow_limits.txt
        sed -i 's/>>.*//g' ZprimeNarrow_limits.txt
        sed -i 's/Observed Limit: r <//g' ZprimeNarrow_limits.txt
        sed -i 's/Expected  2.5%: r <//g' ZprimeNarrow_limits.txt
        sed -i 's/Expected 16.0%: r <//g' ZprimeNarrow_limits.txt
        sed -i 's/Expected 50.0%: r <//g' ZprimeNarrow_limits.txt
        sed -i 's/Expected 97.5%: r <//g' ZprimeNarrow_limits.txt
        sed -i 's/Expected 84.0%: r <//g' ZprimeNarrow_limits.txt
        sed -i '/^$/d' ZprimeNarrow_limits.txt
done

root -l -b -q Brazil.C

declare -a arrWide=("ZprimeWide0500" "ZprimeWide0750" "ZprimeWide1000" "ZprimeWide1250" "ZprimeWide1500" "ZprimeWide2000" "ZprimeWide2500" "ZprimeWide3000" "ZprimeWide3500" "ZprimeWide4000" "ZprimeWide4500" "ZprimeWide5000" "ZprimeWide6000" "ZprimeWide6500" "ZprimeWide7000")
for i in "${arrWide[@]}"
do
  	python TxtDC_limits.py ${i}
        combineCards.py SR1T_muon=SR1T_muon.txt SR0T_muon=SR0T_muon.txt CR1_muon=CR1_muon.txt CR2_muon=CR2_muon.txt > Signal_Region.txt
        combine -M AsymptoticLimits Signal_Region.txt --noFitAsimov >> ZprimeWide_limits.txt
        sed -i 's/Done.*//g' ZprimeWide_limits.txt
        sed -i 's/Will.*//g' ZprimeWide_limits.txt
        sed -i 's/ <<<.*//g' ZprimeWide_limits.txt
        sed -i 's/--.*//g' ZprimeWide_limits.txt
        sed -i 's/>>.*//g' ZprimeWide_limits.txt
        sed -i 's/Observed Limit: r <//g' ZprimeWide_limits.txt
        sed -i 's/Expected  2.5%: r <//g' ZprimeWide_limits.txt
        sed -i 's/Expected 16.0%: r <//g' ZprimeWide_limits.txt
        sed -i 's/Expected 50.0%: r <//g' ZprimeWide_limits.txt
        sed -i 's/Expected 97.5%: r <//g' ZprimeWide_limits.txt
        sed -i 's/Expected 84.0%: r <//g' ZprimeWide_limits.txt
        sed -i '/^$/d' ZprimeWide_limits.txt
done
root -l -b -q Brazil_Wide.C

declare -a arrUWide=("ZprimeUltraWide1000" "ZprimeUltraWide2000" "ZprimeUltraWide3000" "ZprimeUltraWide4000" "ZprimeUltraWide5000" "ZprimeUltraWide6000" "ZprimeUltraWide6500" "ZprimeUltraWide7000")
for i in "${arrUWide[@]}"
do
  	python TxtDC_limits.py ${i}
        combineCards.py SR1T_muon=SR1T_muon.txt SR0T_muon=SR0T_muon.txt CR1_muon=CR1_muon.txt CR2_muon=CR2_muon.txt > Signal_Region.txt
        combine -M AsymptoticLimits Signal_Region.txt --noFitAsimov >> ZprimeUltraWide_limits.txt
        sed -i 's/Done.*//g' ZprimeUltraWide_limits.txt
        sed -i 's/Will.*//g' ZprimeUltraWide_limits.txt
        sed -i 's/ <<<.*//g' ZprimeUltraWide_limits.txt
        sed -i 's/--.*//g' ZprimeUltraWide_limits.txt
        sed -i 's/>>.*//g' ZprimeUltraWide_limits.txt
        sed -i 's/Observed Limit: r <//g' ZprimeUltraWide_limits.txt
        sed -i 's/Expected  2.5%: r <//g' ZprimeUltraWide_limits.txt
        sed -i 's/Expected 16.0%: r <//g' ZprimeUltraWide_limits.txt
        sed -i 's/Expected 50.0%: r <//g' ZprimeUltraWide_limits.txt
        sed -i 's/Expected 97.5%: r <//g' ZprimeUltraWide_limits.txt
        sed -i 's/Expected 84.0%: r <//g' ZprimeUltraWide_limits.txt
        sed -i '/^$/d' ZprimeUltraWide_limits.txt
done
root -l -b -q Brazil_UltraWide.C

declare -a arrJets=("ZprimeWide0500" "ZprimeWide0750" "ZprimeWide1000" "ZprimeWide1250" "ZprimeWide1500" "ZprimeWide2000" "ZprimeWide2500" "ZprimeWide3000" "ZprimeWide3500" "ZprimeWide4000")
for i in "${arrJets[@]}"
do
  	python TxtDC_limits.py ${i}
        combineCards.py SR1T_muon=SR1T_muon.txt SR0T_muon=SR0T_muon.txt CR1_muon=CR1_muon.txt CR2_muon=CR2_muon.txt > Signal_Region.txt
        combine -M AsymptoticLimits Signal_Region.txt --noFitAsimov >> ZprimeJets_limits.txt
        sed -i 's/Done.*//g' ZprimeJets_limits.txt
        sed -i 's/Will.*//g' ZprimeJets_limits.txt
        sed -i 's/ <<<.*//g' ZprimeJets_limits.txt
        sed -i 's/--.*//g' ZprimeJets_limits.txt
        sed -i 's/>>.*//g' ZprimeJets_limits.txt
        sed -i 's/Observed Limit: r <//g' ZprimeJets_limits.txt
        sed -i 's/Expected  2.5%: r <//g' ZprimeJets_limits.txt
        sed -i 's/Expected 16.0%: r <//g' ZprimeJets_limits.txt
        sed -i 's/Expected 50.0%: r <//g' ZprimeJets_limits.txt
        sed -i 's/Expected 97.5%: r <//g' ZprimeJets_limits.txt
        sed -i 's/Expected 84.0%: r <//g' ZprimeJets_limits.txt
        sed -i '/^$/d' ZprimeJets_limits.txt
done
root -l -b -q Brazil_Jets.C
