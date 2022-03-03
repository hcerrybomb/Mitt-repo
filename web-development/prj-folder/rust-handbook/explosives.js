let getElem = function getE(id){
    return document.getElementById(id)
}

function startFunction(){
    let LGF, frags, explosives, pipes, pureGPSulf, GPForExplosives, sulfurForExplosives, exploGPSulf, amtOfRockets
    let sulfValue = 0
    let GPValue = 0
    let roc = 0
}

function innerHtmlID(idString, textString){
    return getElem(idString).innerHTML = textString;
}

function calcValues(){
    pipes = amtOfRockets * 2
        rocketGP = amtOfRockets * 150
            pureGPSulf = rocketGP * 2

        explosives = amtOfRockets * 10
            LGF = explosives * 3
            frags = explosives * 10
            sulfurForExplosives = explosives * 10
            GPForExplosives = explosives * 50
                exploGPSulf = GPForExplosives * 2}
             
function printStuff(){
    innerHtmlID("pipes",            `<pre>Pipes needed                       ${pipes}</pre><br>`)
    innerHtmlID("rocketGP",         `<pre>Rocket gp needed                   ${rocketGP}</pre><br>`)
    innerHtmlID("explosives",       `<pre>Sulf for that gp needed            ${pureGPSulf}</pre><br>`)
    innerHtmlID("pureGPsulf",       `<pre>Explosives needed                  ${explosives}</pre><br>`)
    innerHtmlID("LGF",              `<pre>Low grade fuel needed              ${LGF}</pre><br>`)
    innerHtmlID("frags",            `<pre>Metal fr needed                    ${frags}</pre><br>`)
    innerHtmlID("sulfForExplosives",`<pre>Sulfur for the explosives needed   ${sulfurForExplosives} </pre><br>`)
    innerHtmlID("GPForExplosives",  `<pre>Gp for that explosives needed      ${GPForExplosives}</pre><br>`)
    innerHtmlID("exploGPSulf",      `<pre>Sulf for that gp needed            ${exploGPSulf}</pre><br>`)
}

function getValuesRockets(){

    amtOfRockets = getElem("amtOfRockets").value

    calcValues()
    
    printStuff()

    getElem("totalSulf").value = amtOfRockets * 1400}

function calcSulfPlusGP(){
    roc = 0
    let ratioCheck = true
    while(ratioCheck){
        if(sulfValue < 100){
            ratioCheck = false
        }
        if((GPValue < 650)){
            if(GPValue > 0 ){
                let gpToSulf = GPValue * 2
                sulfValue = sulfValue + gpToSulf
                GPValue = 0
            }
            if(GPValue<0) GPValue = 0
            if(sulfValue >= 1400){
                while(sulfValue >= 1400){
                    sulfValue = sulfValue - 1400
                    roc++  
                }
                ratioCheck = false
            }
        }
        if(GPValue >= 650  && sulfValue >= 100) {
            while(GPValue >= 650  && sulfValue >= 100){
                GPValue     = GPValue   - 650
                sulfValue   = sulfValue - 100
                roc++
            }
        }
    }
    return
}

function getValuesSulfur(){
    GPValue = Number(getElem("inputGP").value) 
    sulfValue = Number(getElem("totalSulf").value)

    if(GPValue === ""){ 
        
        innerHtmlID("inputGPLabel",`How much GP? (optional) :`)

        amtOfRockets = Math.floor(getElem("totalSulf").value/1400)
    }

    else if(GPValue === 0){

        innerHtmlID("inputGPLabel",`How much GP? :`)

        amtOfRockets = Math.floor(getElem("totalSulf").value/1400)
    }

    else{
        calcSulfPlusGP()
        amtOfRockets = roc
    }

    calcValues()
    printStuff()

    getElem("amtOfRockets").value = amtOfRockets 

}
function addGP(){
    GPValue = Number(getElem("inputGP").value) 
    sulfValue = Number(getElem("totalSulf").value)

    if(sulfValue === ""){
        getElem("inputSulfLabel").innerHTML = `How much sulfur? :`}

    else if(sulfValue === 0){
        getElem("inputSulfLabel").innerHTML = `How much sulfur? :`}

    calcSulfPlusGP()
    amtOfRockets = roc
    calcValues()
    printStuff()
    getElem("amtOfRockets").value = amtOfRockets 
}