def horloge(seconde) :
    joura=0
    heur= seconde//3600
    if(heur >= 24) :
        heur= heur//24
        joura= heur%24



    rest= seconde%3600
    if( rest >= 60) :
        minu= rest//60
        while minu>=60 :
            minu -= 60
            heur += 1
    second= rest%60
    return joura, heur, minu, second



    
 
