//? enumerate through arrays AKA for(let property in object)        ARRAY:  for(let element of array)
//!     OPPGAVE 1

let bilMerker = []

let aston = {
    forkortelse: 'AM',
    bilmerke: 'Aston Martin',
    land: 'Storbritania'
}
let mercedes = {
    forkortelse: 'MB',
    bilmerke: 'Mercedes Benz',
    land: 'Tyskland'
}
let alfa = {
    forkortelse: 'AR',
    bilmerke: 'Alfa Romeo',
    land: 'Italia'
}
bilMerker.push(aston);bilMerker.push(mercedes);bilMerker.push(alfa)
console.log('1. A)  ',bilMerker)


for(let i = 0; i <bilMerker.length;i++){
    for (let property in bilMerker[i]) {
        console.log('1. B) ',property + ':' + bilMerker[i][property]);}
}
function sammenlignString(a,b){
    if(a.bilmerke>b.bilmerke){
        return 1 
    }
    else if(a.bilmerke < b.bilmerke){
        return -1
    }
    else{
        return 0 
    }

}
console.log('1. C)  ')
console.table(bilMerker)
bilMerker.sort(sammenlignString)
console.log('1. C)  ')
console.table(bilMerker)


//*function sammenlignString(a,b){
//*    if(a.property > b.property){
//*        return 1 
//*    }
//*    else if(a.property < b.property){
//*        return -1
//*    }
//*    else{
//*        return 0 
//*    }
//*}
//TODO      C + D
//??????????????????????????????????????????????????????????????????
//!     OPPGAVE 2

let filmer = [
    babyDriver = {
        tittel: 'Baby Driver',
        regissør: 'Edgar Wright',
        sett: true
    },
    shaunOfTheDead = {
        tittel: 'Shaun Of The Dead',
        regissør: 'Edgar Wright',
        sett: true
    },
    theWorldsEnd = {
        tittel: 'The Worlds End',
        regissør: 'Edgar Wright',
        sett: true
    },
    hotFuzz = {
        tittel: 'Hot Fuzz',
        regissør: 'Edgar Wright',
        sett: true
    },
    djangoUnchained = {
        tittel: 'Django Unchained',
        regissør: 'Quentin Tarantino',
        sett: true
    },
    killBill = {
        tittel: 'Kill Bill',
        regissør: 'Quentin Tarantino',
        sett: false
    },
    shutterIsland = {
        tittel: 'Shutter Island',
        regissør: 'Martin Scorsese',
        sett: false
    },
    titanic = {
        tittel: 'Titanic',
        regissør: 'James Cameron',
        sett: false
    },
    theDeparted = {
        tittel: 'The Departed',
        regissør: 'Martin Scorsese',
        sett: false
    },
    theGreatGatsby = {
        tittel: 'The Great Gatsby',
        regissør: 'Baz Luhrmann',
        sett: false
    }
]
console.log('2. A)   ')
console.table(filmer)

for(let i = 0; i <filmer.length;i++){
    for (let property in filmer[i]) {
        if(property === 'tittel' || property === 'regissør'){
            console.log('2. B) ',property + ':' + filmer[i][property]);}
        }
}
filmer.sort((a,b)=> (a.tittel > b.tittel ? 1 : -1))
console.log('2. C)   ')
console.table(filmer)
for(let i = 0; i <filmer.length;i++){
    if(filmer[i].sett === true){
        filmer[i].tittel = 'har sett ' + filmer[i].tittel
    }
    if(filmer[i].sett === false){
        filmer[i].tittel = 'har ikke sett ' + filmer[i].tittel
    }
}
console.log('2. D)  ')
console.table(filmer)


let figur1 = {
    form: "rektangel", 
    lengde: 4, 
    bredde: 6, 
    areal: 24, 
    omkrets: 20 
    }
for (let property in figur1) {
        console.log('3. A) ',property);}

figur1.printProperty = function(){
    for (let property in this) {
        console.log('3. B) ',property);}
}
figur1.printProperty()

figur1.printProperty = function(){
    for (let property in this) {
        console.log('3. C) ',property, this[property]);}
}

figur1.printProperty()

figur1.countProperties = function(){
   let propCount = 0;
   for (let property in this){
       propCount++;

   }
   console.log('3. D)   antall properties',propCount)
}
figur1.countProperties()

figur1 = { form: "rektangel", lengde: 4, bredde: 6, areal: 24, omkrets: 20 }

let figur2 = { form: "rektangel", lengde: 4, bredde: 6, areal: 24, omkrets: 20 };

let figur3 = { form: "rektangel", lengde: 9, bredde: 1, omkrets: 20 };

let figur4 = { form: "kvadrat", lengde: 4, bredde: 4, areal: 16 };

let figur5 = { form: "kvadrat", lengde: 6, bredde: 6 };

function checkIdentical(a, b){
    let identical = true

    keyNames1 = Object.keys(a)
    keyNames2 = Object.keys(b)
    console.table(keyNames1)
    console.table(keyNames2)
    if(keyNames1.length !== keyNames2.length){
        identical = false
        console.log('3. E)   De er ikke like!')
        return
    }
    for(let i = 0; i < keyNames1.length; i++){
        if(keyNames1[i] !== keyNames2[i]){
            identical = false
            console.log('3. E)   De er ikke like!')
            return
        }
    }
    for(let property in a){
        if(a[property] !==b[property]){
            identical = false
            console.log('3. E)   De er ikke like!')
            return
        }
    }

    if(identical){
        console.log('3. E)   De er like!')
    }
}
checkIdentical(figur1,figur2)

function checkIdenticalCreate(a,b){
    let newObj = {}
    for(let property in a){
        if(a[property] === b[property]){
            newObj[property] = a[property]
        }
    }
    return newObj
}

let identicalValues = checkIdenticalCreate(figur1,figur1)
console.log('3. F)  ',identicalValues)