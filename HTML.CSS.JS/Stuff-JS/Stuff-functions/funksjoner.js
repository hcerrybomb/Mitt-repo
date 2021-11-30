function skrivUt(){
    document.write("test text")
}
skrivUt()
let navnet = "William"

//? let navnet = prompt("skriv inn navn: ")

document.write("<br><br>")

function siHeiTil(navn){      
    document.write("hei ", navn)
}
siHeiTil(navnet)
document.write("<br>")

function siHeiIgjen(navn){
    document.write(`hei ${navn}!`)
}

document.write("<br>")

siHeiIgjen(navnet)

function rektangel(lengde, bredde){
    let areal = lengde * bredde;
    document.write("<br> Arealet av rekt er ", areal)
}
document.write("<br>")
rektangel(3,4);
document.write("<br>")
document.write("<br>", Math.PI.toFixed(2))

//* getRndInteger
function getRndInteger(min, max) {
return Math.floor(Math.random() * (max - min + 1) ) + min;
} 
  
document.write("<br><br>")

//! OPPGAVE 1
let valg = getRndInteger(1,3)
console.log(valg)
if(valg===1){
    document.write("Hei")
}
else if(valg===2){
    document.write("Hallo")
}
else if(valg===3){
    document.write("God dag")
}

document.write("<br><br>")

//! OPPGAVE 7
function alder(){

    //? let input = Number(prompt("alder: "))
    let input = 25
    if(input>=18){
        document.write("du er voksen")
        return true;
    }
    

    else if(input >= 16 && input < 18){
        document.write("du er ungdom")
    }

    else if(input<16){
        document.write("du er barn")
    }
}   
alder()

document.write("<br><br>")

//! OPPGAVE 13
let treLike = "false"
let totalsum = 0 
let antallkast = 0 
while(treLike == "false"){
    let kast1 = getRndInteger(1,3)
    let kast2 = getRndInteger(1,3)
    let kast3 = getRndInteger(1,3)
    totalsum = kast1 + kast2 + kast3 + totalsum
    antallkast = antallkast + 1
    if(kast1 === kast2 && kast2 === kast3){
        treLike = "true"
        document.write("antall kast: ",antallkast)
        document.write("<br><br>total sum: ",totalsum)
        document.write("<br><br>tre like!")
        break;
    }
}

