def intToAv(intensity):
    '''
    Takes a CO intensity and turns it into an extinction value Av
    '''
    def intToMsunPerPc(intensity):
        Mpc = intensity * 6.3/1.36
        return(Mpc)
    
    def MPcToHcm(Mpc):
        PcToCm = 3.086E18
        massH = 1.673E-24  #grams
        massSun = 1.989E33 #grams 
        MsunToNumH = massSun/massH
        Hcm = Mpc * MsunToNumH / PcToCm**2
        return(Hcm)
    
    def HcmToAv(Hcm):
        Ebv = Hcm/(5.8E21)
        Av = 3.1*Ebv
        return(Av)
    
    MPc = intToMsunPerPc(intensity)
    Hcm = MPcToHcm(MPc)
    Av  = HcmToAv(Hcm)
    return(Av)