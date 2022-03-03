let input1 = prompt("sett in tall: ");

//* hadde orginalt prompt som Number(prompt(""))
//* men så at vi ikke måtte ta høyde for om inputen var tekst
//* som gir mulighet for å sjekke for en tom string 
//* istedenfor 0, som gir brukeren muligheten til å skrive 0 og under
//* og fortsatt få printet ut alle tall fra 25 og ned.

if(input1 === ""){
    document.write("du må skrive inn et tall!")
    console.log("du må skrive inn et tall")
}

else if(input1 < 25){
    for(let i = 0; i < 26; i++){
        document.write(`<br>${25-i}`)
    }
}
else if(input1 <= 50){
    document.write("<br> dette går greit")
}
else{
    if(input1%2 === 0){
        document.write("<br>tallet er et partall")
    }
    else{
        document.write("<br>tallet er et oddetall")
    }
}