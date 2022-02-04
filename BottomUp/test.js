

function calcSulfPlusGP(){

    //?         1 : 13
    let roc = 0
    if(GPValue < 750 || sulfValue < 100){
        return;
    }

    while(ratioCheck){
        if(GPValue > 750  && sulfValue > 100) {
            GPValue     = GPValue   - 750
            sulfValue   = sulfValue - 100
            roc++
        }
        else if(sulfValue < 100){
            console.log("not enough sulf for any more rockets")
        }
        else if(sulfValue > 1400){
            while(sulfValue > 1400){
                sulfValue = sulfValue - 1400
                roc++
            }
        }
        else{
            
        }
    }
}