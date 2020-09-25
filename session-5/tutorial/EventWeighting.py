#===============================================================================
# create dataset weighted according tracking ratios
#===============================================================================
def make_trk_ds( dsm, h_trk , get_val = "interpolate" ):
    message("MAKING WEIGHTED DATASET FOR TRACKING","green")

    we     = ROOT.RooRealVar('we','we',        0, 100     )
    varset = ROOT.RooArgSet ( im ,  we )

    ds_lc_fit = ROOT.RooDataSet ( 'ds_lc_fit' , 'ds_lc_fit' , varset )

    for e in dsm :

        p_p    = max( 10.001 , e.p_p )
        p_k    = max(  3.201 , e.p_k )
        p_3    = max(  5.201 , e.p_3 )

        eta_p  = max( 2.001 , e.eta_p )
        eta_k  = max( 2.001 , e.eta_k )
        eta_3  = max( 2.001 , e.eta_3 )

        eta_p  = min( 4.899 , eta_p  )
        eta_k  = min( 4.899 , eta_k  )
        eta_3  = min( 4.899 , eta_3  )

        ntrk   = min( 699 , e.ntrk )

        if get_val == "bin":
            eff_trk_p = h_trk ( p_p , eta_p , interpolate = (0,0,0) )  
            eff_trk_k = h_trk ( p_k , eta_k , interpolate = (0,0,0) )  
            eff_trk_3 = h_trk ( p_3 , eta_3 , interpolate = (0,0,0) )  
        else:
            eff_trk_p = h_trk ( p_p , eta_p                         )  
            eff_trk_k = h_trk ( p_k , eta_k                         )  
            eff_trk_3 = h_trk ( p_3 , eta_3                         )  
    
        eff = eff_trk_p * eff_trk_k * eff_trk_3
        
        if eff>0.005:
            wpid = (1. / eff).value()
        else:
            wpid = 1.

        if e.im > im.getMin() and e.im<im.getMax():
            im .setVal ( e.im   )
            we .setVal ( wpid   )
            ds_lc_fit.add( varset )

        
    dsw_lc_what =   ds_lc_fit.makeWeighted( "we" )
    dhw_lc_what = (dsw_lc_what.reduce(ROOT.RooArgSet(im),"im>0" + cut_im )).binnedClone()
    message("TRACKING WEIGHTED DATASET DONE","green")
    prl(100)
    
    return dsw_lc_what, dhw_lc_what


