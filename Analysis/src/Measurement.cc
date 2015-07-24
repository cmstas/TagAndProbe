#include "TagAndProbe/Analysis/interface/Measurement.h"

#include <iostream>

using namespace tnp;
using namespace std;

// Tools
#include "AnalysisTools/RootTools/interface/RootTools.h"
#include "AnalysisTools/LanguageTools/interface/LanguageTools.h"
#include "TagAndProbe/Analysis/interface/LeptonTree.h"
#include "TagAndProbe/Analysis/interface/LeptonSelections.h"

namespace tnp
{
    Lepton::value_type GetLeptonFromString(const std::string& lepton_name)
    {
        if (lt::string_lower(lepton_name) == "muon"    ) {return Lepton::Muon;    }
        if (lt::string_lower(lepton_name) == "electron") {return Lepton::Electron;}
        throw std::invalid_argument("[tnp::GetLeptonFromString]: ERROR - invalid value!"); 
    }

    std::string GetStringFromLepton(const Lepton::value_type lepton_type)
    {
        if (lepton_type == Lepton::Muon    ) return "muon";
        if (lepton_type == Lepton::Electron) return "electron";
        throw std::invalid_argument(Form("[tnp::GetStringFromLepton]: ERROR - invalid value! %u", lepton_type)); 
    }

    Selection::value_type GetSelectionFromString(const std::string& sel_name)
    {
        if (lt::string_lower(sel_name) == lt::string_lower("EGammaMediumWPDenID"  )) {return Selection::EGammaMediumWPDenID;  } 
        if (lt::string_lower(sel_name) == lt::string_lower("EGammaMediumWPDenIso" )) {return Selection::EGammaMediumWPDenIso; } 
        if (lt::string_lower(sel_name) == lt::string_lower("EGammaMediumWPDenBoth")) {return Selection::EGammaMediumWPDenBoth;} 
        if (lt::string_lower(sel_name) == lt::string_lower("EGammaMediumWPNum"    )) {return Selection::EGammaMediumWPNum;    } 
        if (lt::string_lower(sel_name) == lt::string_lower("MuTightWPDenID"       )) {return Selection::MuTightWPDenID;       } 
        if (lt::string_lower(sel_name) == lt::string_lower("MuTightWPDenIso"      )) {return Selection::MuTightWPDenIso;      } 
        if (lt::string_lower(sel_name) == lt::string_lower("MuTightWPDenBoth"     )) {return Selection::MuTightWPDenBoth;     } 
        if (lt::string_lower(sel_name) == lt::string_lower("MuTightWPNum"         )) {return Selection::MuTightWPNum;         } 
        throw std::invalid_argument("[tnp::GetSelectionFromString]: ERROR - invalid value!"); 
    }

    std::string GetStringFromSelection(const Selection::value_type sel_type)
    {
        if (sel_type == Selection::EGammaMediumWPDenID  ) return "EGammaMediumWPDenID";
        if (sel_type == Selection::EGammaMediumWPDenIso ) return "EGammaMediumWPDenIso";
        if (sel_type == Selection::EGammaMediumWPDenBoth) return "EGammaMediumWPDenBoth";
        if (sel_type == Selection::EGammaMediumWPNum    ) return "EGammaMediumWPNum";
        if (sel_type == Selection::MuTightWPDenID       ) return "MuTightWPDenID";
        if (sel_type == Selection::MuTightWPDenIso      ) return "MuTightWPDenIso";
        if (sel_type == Selection::MuTightWPDenBoth     ) return "MuTightWPDenBoth";
        if (sel_type == Selection::MuTightWPNum         ) return "MuTightWPNum";
        throw std::invalid_argument("[tnp::GetStringFromSelection]: ERROR - invalid value!"); 
    }

    // passes selection based on above enum
    bool PassesSelection(const Lepton::value_type lepton_type, const Selection::value_type selection, const bool is_data)
    {
        using namespace lepton_tree;

        // --------------------------------------------------------------------------- //
        // electrons
        // --------------------------------------------------------------------------- //

        if (lepton_type == Lepton::Electron)
        {
            // cut values and variables
	    //const bool el_is_barrel   = fabs(etaSC()) < 1.479;
            //const bool el_is_endcap   = !el_is_barrel;
            const bool el_is_crack    = false;
            const float el_tag_pt      = tag_p4().pt(); 
            const float el_tag_pt_cut  = 30.0;

            // cut decisions 
            const bool el_passes_pt       = (el_tag_pt > el_tag_pt_cut);
            const bool el_passes_trig_tag = evt_isRealData() ? tag_HLT_Ele27_eta2p1_WPLoose_Gsf() > 0: true; //true; //GZ need update
            const bool el_passes_id_iso   = passes_HAD_veto_v3(); 
            const bool el_passes_id       = passes_HAD_veto_noiso_v3(); 
	    // necessary when comparing MC with 2012 ZElectron skim, where probe is biassed
						    

            // EGamma Medium WP (2012)
            // https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaCutBasedIdentification 
            // --------------------------------------------------------------------------- //

            // Isolation
            if (selection == Selection::EGammaMediumWPDenIso)
            {
                if (el_is_crack)            {return false;}
                if (not el_passes_pt)       {return false;}
                if (not el_passes_trig_tag) {return false;}
                if (not el_passes_id)       {return false;}
            }
	    //GZ 
            //GZ // ID
            //GZ if (selection == Selection::EGammaMediumWPDenID)
            //GZ {
            //GZ     if (el_is_crack)            {return false;}
            //GZ     if (not el_passes_pt)       {return false;}
            //GZ     if (not el_passes_trig_tag) {return false;}
            //GZ     if (not el_passes_eg_iso)   {return false;}
            //GZ }

            // Both ID and isolation 
            if (selection == Selection::EGammaMediumWPDenBoth)
            {
                if (el_is_crack)            {return false;}
                if (not el_passes_pt)       {return false;}
                if (not el_passes_trig_tag) {return false;}
            }

            // Numerator
            if (selection == Selection::EGammaMediumWPNum)
            {
                if (el_is_crack)             {return false;}
                if (not el_passes_pt)        {return false;}
                if (not el_passes_trig_tag)  {return false;}
                if (not el_passes_id)        {return false;}
                if (not el_passes_id_iso)    {return false;}
            }

        }

        // --------------------------------------------------------------------------- //
        // muons
        // --------------------------------------------------------------------------- //

        if (lepton_type == Lepton::Muon)
        {
            // cut values and variables
            const float mu_tag_pt      = tag_p4().pt();
            const float mu_iso         = miniiso();
            const float mu_iso_pog_cut = 0.15;  
            const float mu_tag_pt_cut  = 30.0;

            // cut decisions 
            const bool mu_passes_pt       = (mu_tag_pt > mu_tag_pt_cut);
            const bool mu_passes_trig_tag = true; //GZ need update
            const bool mu_passes_pog_iso  = (mu_iso < mu_iso_pog_cut); 
            const bool mu_passes_pog_id   = passes_SS_tight_noiso_v3(); 

            // Muon POG Selections (2012)
            // From: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId
            // --------------------------------------------------------------------------- //

            // Isolation
            if (selection == Selection::MuTightWPDenIso)
            {
                if (not mu_passes_pt)       {return false;}
                if (not mu_passes_trig_tag) {return false;}
                if (not mu_passes_pog_id)   {return false;}
            }
	    
            // ID
            if (selection == Selection::MuTightWPDenID)
            {
                if (not mu_passes_pt)        {return false;}
                if (not mu_passes_trig_tag)  {return false;}
                if (not mu_passes_pog_iso)   {return false;}
            }

            // Both ID and isolation
            if (selection == Selection::MuTightWPDenBoth)
            {
                if (not mu_passes_pt)       {return false;}
                if (not mu_passes_trig_tag) {return false;}
            }

            // Numerator
            if (selection == Selection::MuTightWPNum)
            {
                if (not mu_passes_pt)       {return false;}
                if (not mu_passes_trig_tag) {return false;}
                if (not mu_passes_pog_id)   {return false;}
                if (not mu_passes_pog_iso)  {return false;}
            }

            
        }

        // other values are invalid
        if (lepton_type == Lepton::static_size)
        {
            std::cout << "lepton_type is invalid" << std::endl;
            return false;
        }

        // if we got here -- it's selected
        return true;
    }

} // namespace tnp
 
