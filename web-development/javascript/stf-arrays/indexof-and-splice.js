
function randMinMax(min, max) {
    return Math.floor(Math.random() * (max - min + 1) ) + min;
    } 

function fillWithRandom(array,amount,min,max){

    for(let i = 0; i < amount; i++){
        let newNumber = randMinMax(min,max)
        if(array.includes(newNumber)){
            amount++
        }
        else{
            array.push(newNumber)
        }
    }
}

function fillWithWholeNumber(array,amount){
    for(let i = 0; i < amount;i++){
        array.push(i+1)
    }
}


//!     OPPGAVE 1

const opg1Liste = [3,6,2,7,8,3,5]
console.log("1.","liste før")
console.log("1.",opg1Liste)
let opg1Var = 22

if(!opg1Liste.includes(opg1Var)) {
    console.log("1.","not in list, added")
    
    opg1Liste.push(opg1Var)
    console.log("1.","liste etter")
    console.log("1.",opg1Liste)
}
else{
    console.log("1.","already in list")
}


//!     OPPGAVE 2

let opg2Var = 7
console.log("2.","liste før")
console.log("2", opg1Liste)
if(opg1Liste.includes(opg2Var)){
    opg1Liste.splice(opg1Liste.indexOf(opg2Var),1)
}
console.log("2.","liste etter")
console.log("2",opg1Liste)

//!     OPPGAVE 3

const opg3List = []

fillWithRandom(opg3List,9,1,34)

console.log("3.",opg3List)

//!     OPPGAVE 4

const opg4List = []

fillWithWholeNumber(opg4List,30)

console.log("4.",opg4List)

function pullFromArray(array,amount){

    if(amount > array.length){
        console.log("cannot pull more elements than the list has, exiting program")
        return
    }

    const pulledElems = []

    for(let i=0;i<amount;i++){
        let randomIndex = randMinMax(array[0],array.length - 1)
        pulledElems.push(array[randomIndex])
        array.splice(randomIndex,1)
    }

    console.log("4. pulled elems:",pulledElems)
    console.log("4. left of original list:",array)
}

pullFromArray(opg4List,15)

//!     OPPGAVE 5

function fillWithRandomHundred(array,amount){
    for(let i = 0; i < amount; i++){
        array.push(randMinMax(1,100))
    }
}
const opg5List = [];

fillWithRandomHundred(opg5List,500)
console.log("5.",opg5List)

const dupes = []

function findRepeats(array,dupelist){
    for(let i = 0; i < array.length; i++){
        if(array.indexOf(array[i], array.indexOf(array[i]) + 1) !== -1){
            if(dupelist.indexOf(array[i]) === -1 )dupelist.push(array[i])
        } 
    }
}

findRepeats(opg5List, dupes)
console.log("5. ",dupes)
//!     OPPGAVE 6

const opg6List = ["Per", "Pål", "Espen"];

//*let input = prompt("nytt navn: ")

let input = "pÅtTeTREnt"

let firstLetter = input.charAt(0).toUpperCase()

var theRest = input.slice(1)

theRest = theRest.toLowerCase()

let inputFixed = firstLetter + theRest

if(opg6List.indexOf(inputFixed) === -1){
    opg6List.push(inputFixed)
    console.log("6.",opg6List)
}
else{
    console.log("6. navnet er allerede i listen")
    console.log("6.",opg6List)
}

//!     OPPGAVE 7 

const opg7List = [];
var amtOfOne = 0;var amtOfTwo = 0;var amtOfThree = 0;
var amtOfFour = 0;var amtOfFive = 0;var amtOfSix = 0;
for(let i = 0; i < 1000; i++){
    let newNumber = randMinMax(1,6)
    switch(newNumber){
        case 1:
            amtOfOne = amtOfOne + 1
        break;
        case 2:
            amtOfTwo = amtOfTwo + 1
        break;
        case 3:
            amtOfThree = amtOfThree + 1
        break;
        case 4:
            amtOfFour = amtOfFour + 1
        break;
        case 5:
            amtOfFive = amtOfFive + 1
        break;
        case 6:
            amtOfSix = amtOfSix + 1
        break;
    }
    opg7List.push(newNumber)
}

console.log("7.",opg7List)
onePercentage = amtOfOne / 10
twoPercentage = amtOfTwo / 10
threePercentage = amtOfThree / 10
fourPercentage = amtOfFour / 10
fivePercentage = amtOfFive / 10
sixPercentage = amtOfSix / 10
console.log("7. prosent 1'ere:",onePercentage,"%")
console.log("7. prosent 2'ere:",twoPercentage,"%")
console.log("7. prosent 3'ere:",threePercentage,"%")
console.log("7. prosent 4'ere:",fourPercentage,"%")
console.log("7. prosent 5'ere:",fivePercentage,"%")
console.log("7. prosent 6'ere:",sixPercentage,"%")