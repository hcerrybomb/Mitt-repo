//!         OPPGAVE 1 

const   opg1List = [[1,2,3],[4,5,6],[7,8,9]]

console.log("1. B)  ",opg1List[1][2])

for(let i = 0; i < opg1List.length; i++){
    console.log("1. C)  ",opg1List[i])
}

for(let i = 0; i < opg1List.length; i++){
    for(let x = 0; x < opg1List[i].length; x++){
        console.log("1. D)  ",opg1List[i][x])
    }
}
for(let i = 0; i < opg1List.length; i++){
    x = 0
    console.log("1. E)",opg1List[i][x],opg1List[i][x+1],opg1List[i][x+2])
}

//!     OPPGAVE 2

const opg2List = []
for(let i = 1; i < 11; i++){opg2List.push([i])}
for (let x = 0; x < 10; x++) {for (let y = 1; y < 11; y++){opg2List[x].push((x+1)*y)}}
console.log('2.');console.table(opg2List)

//!     OPPGAVE 3

const opg3List = [['audi',    'rød',  'AK 12345'],['opel',    'blå',  'BG 97345'],['mercedes','sølv', 'GH 10835']]
console.table(opg3List)
//*let nyBilMerke = prompt('Please enter car label')
let nyBilMerke = 'Aston Martin'
//*let nyBilFarge = prompt('Please enter car color')
let nyBilFarge = 'grå'
//*let nyBilNummer = prompt('Please enter car license plate')
let nyBilNummer = 'UD 18567'
let alreadyIn = false
for (let i = 0; i < opg3List.length; i++) {
if(opg3List[i].indexOf(nyBilNummer) !== -1){alreadyIn = true}}
if(!alreadyIn){
    opg3List.push([nyBilMerke,nyBilFarge,nyBilNummer])
    console.log('3. a + b)')
    console.table(opg3List)}
else{console.log('plate already registered')}
