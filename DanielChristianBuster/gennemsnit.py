def FraværGennemsnit (uge, fravær):
    #Hej
    antaluge = len(uge)
    fraværialt = sum(fravær)
    gennemsnit = fraværialt/antaluge

    return(gennemsnit)