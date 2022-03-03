let getElem = function getElem(id){
    return document.getElementById(id)
}

function startFunction(){
    let rockets, 
            pipes,
            rocketGunpowder, 
                rocketGunpowderSulfur,
            explosives, 
                lowGrade, 
                metalFrags, 
                explosivesSulfur, 
                explosivesGunpowder, 
                    explosivesGunpowderSulfur
           
    let sulfurValue = 0
    let gunPowderValue   = 0
    let roc       = 0
}

function innerHtmlID(idString, textString){
    return getElem(idString).innerHTML = textString;
}

function calcValues(){
    pipes = rockets * 2
        rocketGunpowder = rockets * 150
            rocketGunpowderSulfur = rocketGunpowder * 2

        explosives = rockets * 10
            lowGrade = explosives * 3
            metalFrags = explosives * 10
            explosivesSulfur = explosives * 10
            explosivesGunpowder = explosives * 50
                explosivesGunpowderSulfur = explosivesGunpowder * 2}
             
function printStuff(){
    innerHtmlID("pipes_tag",                        `<pre>Pipes needed                       ${pipes}</pre><br>`)
    innerHtmlID("rocketGunpowder_tag",              `<pre>Rocket gp needed                   ${rocketGunpowder}</pre><br>`)
    innerHtmlID("explosives_tag",                   `<pre>Sulf for that gp needed            ${rocketGunpowderSulfur}</pre><br>`)
    innerHtmlID("rocketGunpowderSulfur_tag",        `<pre>Explosives needed                  ${explosives}</pre><br>`)
    innerHtmlID("lowGrad_tag",                      `<pre>Low grade fuel needed              ${lowGrade}</pre><br>`)
    innerHtmlID("metalFrags_tag",                   `<pre>Metal fr needed                    ${metalFrags}</pre><br>`)
    innerHtmlID("explosivesSulfur_tag",             `<pre>Sulfur for the explosives needed   ${explosivesSulfur} </pre><br>`)
    innerHtmlID("explosivesGunpowder_tag",          `<pre>Gp for that explosives needed      ${explosivesGunpowder}</pre><br>`)
    innerHtmlID("explosivesGunpowderSulfur_tag",    `<pre>Sulf for that gp needed            ${explosivesGunpowderSulfur}</pre><br>`)
}


function getValuesRockets(){

    rockets = getElem("rockets_input").value

    calcValues()
    
    printStuff()

    getElem("sulfur_input").value = rockets * 1400}

function calcSulfPlusGP(){
    roc = 0
    let ratioCheck = true
    let sulfRocketLoop = 0
    let sulfAndGpRocketLoop = 0
    let runs = 0
    while(ratioCheck){
        runs++
        console.log(`starting ratio run nr${runs}`)

        if(sulfurValue < 100){
            console.log(`${sulfurValue} Sulfur was less than 100 on ratio run ${runs}`)
            console.log(`exiting loop on ratio run ${runs}, ${sulfurValue} sulfur and ${gunPowderValue} GP`)
            ratioCheck = false
        }
        if((gunPowderValue < 650)){
            if(gunPowderValue > 0 ){
                console.log(`${gunPowderValue} gp value was between 650 and 0 and was turned into sulf on ratio run ${runs}`)
                console.log(`${sulfurValue} before sulf value on ratio run ${runs}`)
                sulfurValue += (gunPowderValue*2)
                console.log(`${sulfurValue} after sulf value on ratio run ${runs}`)
                gunPowderValue = 0
                console.log(`${gunPowderValue} after on ratio run ${runs}`)
            }
            if(gunPowderValue<0){ 
                console.log(`${gunPowderValue} gp value was less than 0 and therefore turned into 0 on ratio run ${runs}`)
                gunPowderValue = 0
                console.log(`${gunPowderValue} gp value is now 0 on ratio run ${runs}`)
            }
            if(sulfurValue >= 1400){
                console.log(`${sulfurValue} was more than 1400 on ratio run ${runs}, starting sulf rocket loop`)
                while(sulfurValue >= 1400){
                    sulfRocketLoop++
                    console.log(`${sulfurValue} was more than 1400 on sulf rocket loop nr ${sulfRocketLoop}`)
                    sulfurValue -= 1400
                    roc++
                    console.log(`added a rocket! now ${roc} rockets`)
                }
                console.log(`exiting loop on ratio run ${runs}, ${sulfurValue} sulfur and ${gunPowderValue} GP`)
                ratioCheck = false
            }
            if(sulfurValue < 1400){
                console.log(`${sulfurValue} sulf was less than 1400, meaning no more rockets on ratio run ${runs}`)
                console.log(`spare sulfur is ${sulfurValue}`)
                console.log(`exiting loop on ratio run ${runs}, ${sulfurValue} sulfur and ${gunPowderValue} GP`)
                ratioCheck = false
            }
        }
        if(gunPowderValue >= 650  && sulfurValue >= 100) {
            console.log(`${gunPowderValue} GP was more than or the same as 650, ${sulfurValue} sulfur was more than or the same as 100`)
            console.log(`starting rocket craft loop on ratio run ${runs}`)
            while(gunPowderValue >= 650  && sulfurValue >= 100){
                sulfAndGpRocketLoop++
                console.log(`${gunPowderValue} GP was more then 650, ${sulfurValue} sulf was more than 100 on sulf+gp rocket loop nr ${sulfAndGpRocketLoop}`)
                gunPowderValue -= 650
                sulfurValue -= 100
                roc++
                console.log(`added a rocket! now ${roc} rockets`)
            }
        }
    }
    console.log(`exiting loop on ratio run ${runs}, ${sulfurValue} sulfur and ${gunPowderValue} GP`)
    return
}

function getValuesSulfur(){
    gunPowderValue = Number(getElem("gunpowder_input").value) 
    sulfurValue = Number(getElem("sulfur_input").value)

    if(gunPowderValue === ""){ 
        
        innerHtmlID("gunpowder_label",`How much GP? (optional) :`)

        rockets = Math.floor(getElem("sulfur_input").value/1400)
    }

    else if(gunPowderValue === 0){

        innerHtmlID("gunpowder_label",`How much GP? :`)

        rockets = Math.floor(getElem("sulfur_input").value/1400)
    }

    else{
        calcSulfPlusGP()
        rockets = roc
    }

    calcValues()
    printStuff()

    getElem("rockets_input").value = rockets 

}
function addGP(){
    gunPowderValue = Number(getElem("gunpowder_input").value) 
    sulfurValue = Number(getElem("sulfur_input").value)

    if(sulfurValue === ""){
        getElem("sulfur_label").innerHTML = `How much sulfur? :`}

    else if(sulfurValue === 0){
        getElem("sulfur_label").innerHTML = `How much sulfur? :`}

    calcSulfPlusGP()
    rockets = roc
    calcValues()
    printStuff()
    getElem("rockets_input").value = rockets 
}