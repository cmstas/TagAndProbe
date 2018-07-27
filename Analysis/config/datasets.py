import FWCore.ParameterSet.Config as cms
import os

## path the analysis
analysis_path = os.getenv("CMSSW_BASE") + "/src/TagAndProbe/Analysis"

## add the configuration path
import sys
sys.path.append(analysis_path + "/config")

## ------------------------------------------------------------------------------------------------------------------- #
## define the input datasets
## ------------------------------------------------------------------------------------------------------------------- #

## path to the lepton trees
#lepton_tree_tag  = "v1.07TP" 
#lepton_tree_tag  = "v2.04TP"
lepton_tree_tag  = "ReRecoDataMoriondMC_5PF_7Feb17"
lepton_tree_path = "/nfs-7/userdata/leptonTree/" + lepton_tree_tag 
lepton_tree_path = "/nfs-7/userdata/phchang/lepton_babies/v2.0"

## good run list
#run_list = cms.string(analysis_path + "/json/Cert_246908-258159_13TeV_PromptReco_Collisions15_25ns_JSON_v3_snt.txt")
run_list = cms.string("")

## DY fullsim
dy_test = cms.PSet(
	name     = cms.string("dy_test"),
	title    = cms.string("DY test"),
	files    = cms.vstring(['/home/users/gzevi/TagProbe/CMSSW_7_4_1/src/LeptonBabyMaker/DY100k.root']),
	is_data  = cms.bool(False),
	run_list = cms.string('')
)

## DY fullsim
#dy_full = cms.PSet(
#	name     = cms.string("dy_amcnlo"),
#	title    = cms.string("DY amcnlo"),
#	files    = cms.vstring([lepton_tree_path+'/DY_amcnlo.root']),
#	is_data  = cms.bool(False),
#	run_list = cms.string('')
#)

dy_full = cms.PSet(
	name     = cms.string("dy_full"),
	title    = cms.string("DY full"),
	files    = cms.vstring([lepton_tree_path+'/DY_madgraph.root']),
	is_data  = cms.bool(False),
	run_list = cms.string('')
)


# DY 80X
dy_full_80X = cms.PSet(
        name     = cms.string("dy_full_80X"),
        title    = cms.string("DY madgraph"),
        files    = cms.vstring([lepton_tree_path+'/DY_madgraph80X.root']),
        is_data  = cms.bool(False),
        run_list = cms.string('')
)

# DY fullsim
dy_madgraph = cms.PSet(
	name     = cms.string("dy_madgraph"),
	title    = cms.string("DY madgraph"),
	files    = cms.vstring([lepton_tree_path+'/DY_madgraph.root']),
	is_data  = cms.bool(False),
	run_list = cms.string('')
)

## DY fastsim
dy_fast = cms.PSet(
	name     = cms.string("dy_fast"),
	title    = cms.string("DY faststim"),
	files    = cms.vstring([lepton_tree_path+'/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball_Summer12-START52_V9_FSIM-v1_AODSIM/*.root']),
	is_data  = cms.bool(False),
	run_list = cms.string('')
)

## muon triggered data 
double_mu = cms.PSet(
	name     = cms.string("data_double_mu"),
	title    = cms.string("DoubleMu_Run2012"),
	files    = cms.vstring([lepton_tree_path+'/DoubleMu_Run2012*/*.root']),
	is_data  = cms.bool(True),
	run_list = run_list 
)

single_mu = cms.PSet(
	name     = cms.string("data_single_mu"),
	title    = cms.string("SingleMuon"),
#	files    = cms.vstring([lepton_tree_path+'/2015DSingleMuonV4.root']),
	files    = cms.vstring([lepton_tree_path+'/2016SingleMu*.root']),
	is_data  = cms.bool(True),
	run_list = run_list 
)

## electron triggered data 
single_el = cms.PSet(
	name     = cms.string("data_single_el"),
	title    = cms.string("SingleElectron"),
#	files    = cms.vstring([lepton_tree_path+'/2015DSingleEl*.root']),
#	files    = cms.vstring([lepton_tree_path+'/2015DSingleElV4.root']),
	files    = cms.vstring([lepton_tree_path+'/2016SingleEl*.root']),
	is_data  = cms.bool(True),
	run_list = run_list 
)
double_el_test = cms.PSet(
	name     = cms.string("data_double_el"),
	title    = cms.string("DoubleElectron_Run2012"),
	files    = cms.vstring(['/home/users/gzevi/TagProbe/CMSSW_7_4_1/src/LeptonBabyMaker/2012DoubleEleFixedTrailingLeg.root']),
	is_data  = cms.bool(True),
	run_list = run_list 
)


## electron triggered data                                                                                                                                                   
single_el_2016 = cms.PSet(
        name     = cms.string("data_single_el"),
        title    = cms.string("SingleElectron_2016"),
        files    = cms.vstring([lepton_tree_path+'/2016SingleEl.root']),
        is_data  = cms.bool(True),
        run_list = run_list
)

#________________________________________________________________________________________________________
# TnP babies
lepton_tree_path = "/nfs-7/userdata/phchang/WWW_babies/TnP2017_v3.0.1/"

# Test Samples
test_dy = cms.PSet(
        name     = cms.string("dy_full"),
        title    = cms.string("DY full"),
        files    = cms.vstring(['/home/users/phchang/public_html/analysis/www/code/VVVBabyMaker2017/dilepbabymaker/testjobs/output_2017_CMS4_TnPBaby_DYJetsToLL_M-50.root']),
        is_data  = cms.bool(False),
        run_list = cms.string('')
        )

test_el_data = cms.PSet(
        name     = cms.string("data_single_el"),
        title    = cms.string("SingleElectron"),
        files    = cms.vstring(['/home/users/phchang/public_html/analysis/www/code/VVVBabyMaker2017/dilepbabymaker/testjobs/output_2017_CMS4_TnPBaby_SingleElectron_Run2017B.root']),
        is_data  = cms.bool(True),
        run_list = cms.string('')
        )

test_mu_data = cms.PSet(
        name     = cms.string("data_single_mu"),
        title    = cms.string("SingleMuon"),
        files    = cms.vstring(['/home/users/phchang/public_html/analysis/www/code/VVVBabyMaker2017/dilepbabymaker/testjobs/output_2017_CMS4_TnPBaby_SingleMuon_Run2017B.root']),
        is_data  = cms.bool(True),
        run_list = cms.string('')
        )

# DY fullsim
TnP2017_dy_m50_madgraph = cms.PSet(
        name     = cms.string("dy_m50_madgraph"),
        title    = cms.string("DY madgraph"),
        files    = cms.vstring([lepton_tree_path+'/dy_m50_madgraph.root']),
        is_data  = cms.bool(False),
        run_list = cms.string('')
        )

