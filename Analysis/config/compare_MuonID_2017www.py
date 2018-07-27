import FWCore.ParameterSet.Config as cms
import os

## path the analysis (THIS SHOULD NOT CHANGE)
analysis_path = os.getenv("CMSSW_BASE") + "/src/TagAndProbe/Analysis"

## add the configuration path (THIS SHOULD NOT CHANGE)
import sys
sys.path.append(analysis_path + "/config")

## process to parse (THIS SHOULD NOT CHANGE)
process = cms.PSet()

## ------------------------------------------------------------- #
## define the input datasets
## ------------------------------------------------------------- #

from datasets import *

## ------------------------------------------------------------- #
## Parameters for the comparison
## ------------------------------------------------------------- #

# muon ID comparison
list_id = [
    cms.PSet(
        verbose = cms.bool(False),
        output_label = cms.string("compare"),
        eff_results_path = cms.string(analysis_path+"/plots/MuonID_2017www/muon/MuMediumPOG_MuTightVVV"),
        dataset1 = test_mu_data,
        dataset2 = test_dy,
        suffix = cms.string("png"),
    ),
]

process.tnp_compare = cms.VPSet(*list_id)
