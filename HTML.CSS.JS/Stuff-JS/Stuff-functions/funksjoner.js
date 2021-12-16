function skrivUt(){
    console.log("test text")
}
skrivUt()
let navnet = "William"

//? let navnet = prompt("skriv inn navn: ")

console.log("<br><br>")

function siHeiTil(navn){      
    console.log("hei ", navn)
}
siHeiTil(navnet)
console.log("<br>")

function siHeiIgjen(navn){
    console.log(`hei ${navn}!`)
}

console.log("<br>")

siHeiIgjen(navnet)

function rektangel(lengde, bredde){
    let areal = lengde * bredde;
    console.log("<br> Arealet av rekt er ", areal)
}
console.log("<br>")
rektangel(3,4);
console.log("<br>")
console.log("<br>", Math.PI.toFixed(2))

//* getRndInteger
function randMinMax(min, max) {
return Math.floor(Math.random() * (max - min + 1) ) + min;
} 
  
console.log("<br><br>")

//! OPPGAVE 1
let valg = randMinMax(1,3)
console.log(valg)
if(valg===1){
    console.log("Hei")
}
else if(valg===2){
    console.log("Hallo")
}
else if(valg===3){
    console.log("God dag")
}

console.log("<br><br>")

//! OPPGAVE 7
function alder(){

    //? let input = Number(prompt("alder: "))
    let input = 25
    if(input>=18){
        console.log("du er voksen")
        return true;
    }
    

    else if(input >= 16 && input < 18){
        console.log("du er ungdom")
    }

    else if(input<16){
        console.log("du er barn")
    }
}   
alder()

console.log("<br><br>")





//! OPPGAVE 13
var treLike = false
var totalsum = 0 
var antallkast = 0 
while(!treLike){
    var kast1 = randMinMax(1,3),kast2 = randMinMax(1,3),kast3 = randMinMax(1,3);
    antallkast++;
    totalsum = kast1 + kast2 + kast3 + totalsum;
    console.log(kast1,'  ',kast2,'  ',kast3,'  ',totalsum,'  ',antallkast);
    if(kast1 === kast2 && kast2 === kast3){
        treLike = true;
        document.write("antall kast: ",antallkast)
        document.write("<br><br>total sum: ",totalsum)
        document.write("<br><br>tre like!")   
    }
}

