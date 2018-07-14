# TagAndProbe

To set things up on UAF:

   export SCRAM_ARCH=slc6_amd64_gcc491
   source /cvmfs/cms.cern.ch/cmsset_default.sh
   cmsrel CMSSW_7_4_2
   cd CMSSW_7_4_2/src
   cmsenv

   git clone git@github.com:gzevi/AnalysisTools.git 
   git clone git@github.com:cmstas/TagAndProbe.git

   scramv1 b -j10

To also have the LeptonBabyMaker available

   git clone git@github.com:cmstas/LeptonBabyMaker.git
   cd LeptonBabyMaker
   git checkout master
   . setupCORE.sh
   cd ../

To run the first steps (make dilepMass plots and fit them to 
extrac efficiencies) on a small LeptonTree:
   cd TagAndProbe/Analysis
   tnp_make_plots config/ElectronID_2015test.py
   tnp_eff_plots  config/ElectronID_2015test.py
   tnp_compare config/compare.py 

-------
For detailed instructions, look at Ryan's twiki, skipping the babymaking 
http://www.t2.ucsd.edu/tastwiki/bin/view/CMS/TagAndProbe#Calculate_the_Efficiency
Main file to modify when defining new IDs: Measurement.cc
-------

Regarding LeptonTrees:

Useful tool to remake LeptonTree.h/cc files after changing the LeptonTree
    TagAndProbe/Analysis/tools/makeLeptonTreeClassFiles.sh

