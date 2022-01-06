//!         ARRAYS

const tall2 = [4,6,15,75,2,2,2,2];

const byer = ["Bergen","Bodø","Oslo"]

//console.log(byer[0])

//console.log(byer)

byer.push("Berlin")             //*       =     .append

byer.unshift("Kristiansand")    //*       =     .append at 0 

byer.pop()                      //*       =     .del at last elem

byer.shift()                    //*       =     .del at index 0

let length = tall2.length        //*       =     .len


//console.log(length)

//!     OPPGAVE 1.0

const opg1 = [0,1,2,3,4,6,7,8,9,10]
for(let i = 0; i < opg1.length; i++){
    if(opg1[i]%2===0){
        console.log("1)  ",opg1[i]);
    }
}
let sum = 0
let gjennomsnitt = 0 
for(let i = 0; i < opg1.length; i++){
    sum = sum + opg1[i];
}
gjennomsnitt = sum / opg1.length
console.log("1)  ",sum,gjennomsnitt)


//!     OPPGAVE 1.1

const navn = ["Mari","Benjamin","Tiril","Joakim","Andrea","Anders"]

//let legTilNavn = prompt("navn: ")
legTilNavn = "William"


if(legTilNavn==""){
}
else{
navn.push(legTilNavn)

navn.sort()     //*     sorteres alfabetisk

for(let i = 0; i < navn.length; i++){
    document.write("1.1)  ",navn[i],"<br>")
}
document.write("<br><br>")
navn.reverse()
for(let i = 0; i < navn.length; i++){
    document.write("1.1)  ",navn[i],"<br>")
}  
}


//!     OPPGAVE 2

const tall = [2,4,6,8]

tall.pop()
tall.shift()

console.log("2.a)  ",tall)

tall.push(5)

console.log("2.b)  ",tall)

tall.sort()

console.log("2.c)  ",tall)

tall.push(7)
tall.unshift(3)

console.log("2.d)  ",tall)

const tallstr = ["tre","fem","syv"]

let x=0
for(let i = 0; i < tall.length; i++){
    if(tall[i]%2==1){
        tall[i] = tallstr[x]
        x++
    }
}
console.log("2.e)  ",tall)


//!     OPPGAVE 3

const andretall = [4,3,2,6]

//*var flertall = Number(prompt("hallo heisann: "))



var flertall = 4

andretall.push(flertall)

for(let i = 0; i < andretall.length; i++) {
    console.log("3.1)  ",andretall[i])
}

let summen = 0
for(let i = 0; i < andretall.length; i++){
    summen = summen + andretall[i]
}
console.log("3.2)  ",summen)

let summen2 = 1

for(let i = 0; i < andretall.length; i++){
    
    summen2 = summen2 * (andretall[i])
}
console.log("3.3)  ",summen2)

    
//!     OPPGAVE 4


const maksliste = [1, 4, 41, 82, 101, 14]

console.log("4.a)  høyeste tall)  ",Math.max(...maksliste))

console.log("4.b)  variasjonsbredden)  ",Math.max(...maksliste) - Math.min(...maksliste))


//!     OPPGAVE 6

function findmax(array){

    console.log("6.a)  høyeste tall)  ",Math.max(...array))
}
function findvariation(array){

    console.log("6.b)  variasjonsbredden)  ",Math.max(...array) - Math.min(...array))
}
function findaverage(array){

    let summen = 0
    for(let i = 0; i < array.length; i++){
        summen = summen + array[i]
    }
    console.log("6.c)  gjennomsnittet)  ",summen/array.length)
}
findmax(maksliste)
findvariation(maksliste)
findaverage(maksliste)



//!     OPPGAVE 7 

let testlist = [1,2,3,4,5,6]

function reversearray(opg,array){
    console.log("before",array)
    let lengde = array.length
    
    for(let i = 0; i < lengde; i++){
        array.unshift(array[1])
    }
    
    console.log(opg,array)
}
reversearray("7)  ",testlist)


//!     OPPGAVE 8
function randMinMax(min, max) {
    return Math.floor(Math.random() * (max - min + 1) ) + min;
    } 

function fillwithrandom(array,amount){

    for(let i = 0; i < amount; i++){
        array.push(randMinMax(1,100))
    }
    console.log("8.b)  ",array)
}

const randomnumber = []

fillwithrandom(randomnumber,50)



function fjernpartall(array){
    for (let i = 0; i < array.length; i++){
        if(array[i] % 2 == 0){
            array.splice(i, 1)
        }
    }
    console.log("8.c)  ",array)
}
fjernpartall(randomnumber)



//!     OPPGAVE OPPSTART

let partallliste = []

for(let i = 1; i <= 15; i++){
    partallliste.push(i)
}
console.log(partallliste)
for(let i = 0; i < partallliste.length; i++){
    if(partallliste[i] % 2 == 0){
        partallliste.splice(i,1,"par")
    }
}
console.log(partallliste)


//!     OPPGAVE 9

let primtallliste = [7, 11, 13, 17, 19, 23, 43, 47, 53, 59, 61, 67]

function print(array,opg){
    for(let i=0; i<array.length; i++){
        console.log(opg,array[i])
    }
}
print(primtallliste,"9.a)  ")

primtallliste = []

for (let i = 0; i <= 100; i++) {
    let check = true;
    for (let j = 2; j < i; j++) {
        if (i % j == 0) {
            check = false;
            break;
        }
    }
    if (i > 1 && check===true) {
        primtallliste.push(i);
    }
}

print(primtallliste,"9.b)  ")



