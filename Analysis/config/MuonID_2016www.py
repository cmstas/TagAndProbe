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
## Parameters for the selection, plot making, and fitting
## ------------------------------------------------------------- #

tnp_parameters = cms.PSet(

    ## Parameters for the selection and mass plots
    ## --------------------------------------------------------- #

    ## type of lepton
    lepton_type = cms.string("muon"),

    ## output label to give it a unique name
    output_label = cms.string("MuonID_Activity"),

    ## suffix to print the plots (before the fit)
    ## blank means do not print
    ## available options are: eps, png, pdf
    suffix = cms.string("png"),

    ## pile re-weighting histogram
    pileup_hist_file = cms.string(analysis_path + "/data/puWeights_Summer12_53x_Observed.root"),
        pileup_hist_name = cms.string("puWeights"),

    ## max number of events to run on
    max_events = cms.int64(-1),

    ## verbosity (for trouble shooting)
    verbose = cms.bool(False),

    ## mass range for resonance window
    mass_low       = cms.double(70.0),  # GeV
    mass_high      = cms.double(110.0), # GeV
    mass_bin_width = cms.double(1.0),   # GeV

    # datasets to run on
        datasets = cms.VPSet(dy_full, single_mu),
#	        datasets = cms.VPSet(dy_full),
        #datasets = cms.VPSet(dy_test, double_el_test),

    ## bins for the observables
    ## supported pt, eta, phi, and # vertices
    ## note: for eta and phi, no negative bins means use |eta| and |phi|, respectively
    pt_bins   = cms.vdouble(20, 25, 30, 35, 40, 50, 100, 200),
    eta_bins  = cms.vdouble(0., 1.5, 2.5),
    phi_bins  = cms.vdouble(),
    nvtx_bins = cms.vdouble(),
    activity_bins = cms.vdouble(),

        ## W/Z measurement bins
        #pt_bins   = cms.vdouble(25, 40, 55, 200),
        #eta_bins  = cms.vdouble(-2.5, -2, -1.566, -1.442, -1, -0.5, 0, 0.5, 1, 1.4442, 1.566, 2, 2.5),

    ## selection (from Measurements.h/cc)
    numerator   = cms.string("MuTightVVV"),
    denominator = cms.string("MuTightWPDenBoth"),

    ## Parameters for the fitting
    ## --------------------------------------------------------- #

    ## Parameters for the fitting
    ## --------------------------------------------------------- #

    ## models for pt bins
    pt_models = cms.vstring(
    #          sig pass,        sig fail,      bkg pass,      bkg fail
        "MCTemplate" , "MCTemplate" , "Exponential" , "Exponential" , # pt0
        "MCTemplate" , "MCTemplate" , "Exponential" , "Exponential" , # pt1
        "MCTemplate" , "MCTemplate" , "Exponential" , "Exponential" , # pt2
        "MCTemplate" , "MCTemplate" , "Exponential" , "Exponential" , # pt3
        "MCTemplate" , "MCTemplate" , "Exponential" , "Exponential" , # pt4
        "MCTemplate" , "MCTemplate" , "Linear"      , "Linear"      , # pt5
        "MCTemplate" , "MCTemplate" , "Linear"      , "Linear"      , # pt6
    ),

    ## models for eta bins
    eta_models = cms.vstring(
    #          sig pass,        sig fail,      bkg pass,      bkg fail
        "MCTemplate"   , "MCTemplate"   , "Exponential"  , "Exponential", # eta2
        "MCTemplate"   , "MCTemplate"   , "Exponential"  , "Exponential", # eta3
    ),

    activity_models = cms.vstring(
    #          sig pass,        sig fail,      bkg pass,      bkg fail
        "MCTemplate"   , "MCTemplate"   , "Exponential"  , "Exponential",
        "MCTemplate"   , "MCTemplate"   , "Exponential"  , "Exponential",
        "MCTemplate"   , "MCTemplate"   , "Exponential"  , "Exponential",
        "MCTemplate"   , "MCTemplate"   , "Exponential"  , "Exponential",
        "MCTemplate"   , "MCTemplate"   , "Exponential"  , "Exponential",

    ),

    ## models for phi bins
    phi_models = cms.vstring(
    #          sig pass,        sig fail,      bkg pass,      bkg fail
        "BreitWignerCB", "BreitWignerCB", "Exponential", "Exponential", # phi0
        "BreitWignerCB", "BreitWignerCB", "Exponential", "Exponential", # phi1
        "MCTemplate"   , "MCTemplate"   , "Exponential"  , "Exponential"      , # phi2
        "MCTemplate"   , "MCTemplate"   , "Exponential", "Exponential", # phi3
        "MCTemplate"   , "MCTemplate"   , "Chebychev"  , "Chebychev"  , # phi4
        "MCTemplate"   , "MCTemplate"   , "Chebychev"  , "Chebychev"  , # phi5
        "MCTemplate"   , "MCTemplate"   , "Chebychev"  , "Chebychev"  , # phi6
    ),

    ## models for nvtx bins
    nvtx_models = cms.vstring(
    #          sig pass,        sig fail,      bkg pass,      bkg fail
        "BreitWignerCB", "BreitWignerCB", "Exponential", "Exponential", # nvtx0
        "BreitWignerCB", "BreitWignerCB", "Exponential", "Exponential", # nvtx1
        "MCTemplate"   , "MCTemplate"   , "Poly3"      , "Poly3"      , # nvtx2
#	        "MCTemplate"   , "MCTemplate"   , "ErfExp"     , "ErfExp"     , # nvtx3  #### Need to fix ErfExp
        "MCTemplate"   , "MCTemplate"   , "Exponential", "Exponential"     , # nvtx3
        "MCTemplate"   , "MCTemplate"   , "Chebychev"  , "Chebychev"  , # nvtx4
        "MCTemplate"   , "MCTemplate"   , "Chebychev"  , "Chebychev"  , # nvtx5
        "MCTemplate"   , "MCTemplate"   , "Chebychev"  , "Chebychev"  , # nvtx6
        "MCTemplate"   , "BreitWignerCB", "Chebychev"  , "Chebychev"  , # nvtx7
    ),


    pt_vs_eta_models = cms.vstring( # Possibly eta vs pt instead of pt vs eta. need to check
    #          sig pass,        sig fail,      bkg pass,      bkg fail

        "MCTemplate"    , "MCTemplate"    , "Exponential" , "Exponential" , # pt0
        "MCTemplateCB"  , "MCTemplateCB"  , "Exponential" , "Exponential" , # pt0

        "BreitWignerCB" , "BreitWignerCB" , "Exponential" , "Exponential" , # pt1
        "MCTemplateCB"  , "MCTemplateCB"  , "Exponential" , "Exponential" , # pt1

        "MCTemplate"    , "MCTemplate"    , "Exponential" , "Exponential" , # pt2
        "MCTemplateCB"  , "MCTemplateCB"  , "Exponential" , "Exponential" , # pt2

        "MCTemplateCB"  , "MCTemplateCB"  , "Exponential" , "Exponential" , # pt3
        "MCTemplateCB"  , "MCTemplateCB"  , "Exponential" , "Exponential" , # pt3

        "MCTemplateCB"  , "MCTemplateCB"  , "Exponential" , "Exponential" , # pt4
        "MCTemplateCB"  , "MCTemplateCB"  , "Exponential" , "Exponential" , # pt4

        "MCTemplateCB"  , "MCTemplateCB"  , "Linear"      , "Linear"      , # pt5
        "MCTemplateCB"  , "MCTemplateCB"  , "Linear"      , "Linear"      , # pt5

        "MCTemplateCB"  , "MCTemplateCB"  , "Linear"      , "Linear"      , # pt6
        "MCTemplateCB"  , "MCTemplateCB"  , "Linear"      , "Linear"      , # pt6

    ),

        activity_vs_pt_models = cms.vstring(
    #          sig pass,        sig fail,      bkg pass,      bkg fail
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",

        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",

        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",

        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",

        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",
        "MCTemplateCB"   , "MCTemplateCB"   , "Exponential", "Exponential",

    ),

)

## ------------------------------------------------------------- #
## hisogram files to use with MC Templates (if used)
## ------------------------------------------------------------- #

tnp_parameters.mc_template_file = cms.string("%s/plots/%s/%s/%s_%s/%s.root" % (analysis_path,
                                                                               tnp_parameters.output_label.value(),
                                                                               tnp_parameters.lepton_type.value(),
                                                                               tnp_parameters.denominator.value(),
                                                                               tnp_parameters.numerator.value(),
                                                                               dy_full.name.value()))
## ------------------------------------------------------------- #
## process to make the plots
## will make a set of plots for each element of the cms.VPSet
## ------------------------------------------------------------- #

process.tnp_make_plots = tnp_parameters
process.tnp_make_plots.suffix = cms.string("")

## ------------------------------------------------------------- #
## process to fit the plots and extract the efficiency
## ------------------------------------------------------------- #

process.tnp_eff_plots = tnp_parameters
process.tnp_make_plots.suffix = cms.string("png")
