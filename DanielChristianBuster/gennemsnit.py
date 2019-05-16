def FraværGennemsnit (uge, fravær):
    antaluge = len(uge)
    fraværialt = sum(fravær)
    gennemsnit = fraværialt/antaluge

    return(gennemsnit)