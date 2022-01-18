let land  = {
    navn:'Norge',
    hovedstad:'Oslo',
    myntenhet:'NOK',
    storsteByer:['Oslo','Bergen','Trondheim'],   
}
console.log(land.navn)
console.log(land['navn'])
console.table(land.storsteByer)
function randMinMax(min, max) {return Math.floor(Math.random() * (max - min + 1) ) + min;} 





//!     OPPGAVE 1

let meg = {
navn:'Ben', 
etternavn:'White', 
fodselsaar:'2004', 
favorittfilm:'Baby Driver', 
favorittall:'25',
favorittmat:['Pasta','Taco','Pizza'],
}
//!     OPPGAVE 2

for (let property in meg) {
    console.log('2.  ',property + ':' + meg[property]);}

//!     OPPGAVE 3

for (let property in meg) {
    if(property === 'favorittmat') console.log('3.  ',`${property}: ${meg[property]}`);}

//!     OPPGAVE 4

meg['favortittfarge'] = 'rød' 
//* ELLER  land.favorittfarge = 'rød
console.log('4.  ',meg.favortittfarge)

//!     OPPGAVE 5

function utskrift(obj){console.log('5.  ',obj)}
utskrift(meg)

//!     OPPGAVE 6
meg.fulltnavn = function(){console.log('6  ', this.navn, this.etternavn)}
meg.fulltnavn()

//!     OPPGAVE 7
meg.visMat = function() {console.log('7.  ', this.favorittmat)}
meg.visMat()

//!     OPPGAVE 8
meg.hvaSkalJegHaTilMiddag = 
function() {console.log('8.  ',this.favorittmat[randMinMax(0,this.favorittmat.length-1)])}
meg.hvaSkalJegHaTilMiddag()

//!     OPPGAVE 9

let informasjonsteknologi1 = { 
    spraak: ["HTML", "CSS"], 
    likerFaget: false, 
    timetall: 5, 
    klasserom: "320.60", 
    antallElever: 24 
}

informasjonsteknologi1.spraak.push('JAVASRIPT')
console.log('9. A)  ',informasjonsteknologi1)
informasjonsteknologi1.antallElever =  informasjonsteknologi1.antallElever + 4
console.log('9. B)  ',informasjonsteknologi1)
informasjonsteknologi1.likerFaget = true
console.log('9. C)  ',informasjonsteknologi1)
delete informasjonsteknologi1.timetall
console.log('9. D)  ',informasjonsteknologi1)
for (let property in informasjonsteknologi1) {
    if(property === 'spraak') console.log('9. E)  ',informasjonsteknologi1[property]);}
for (let property in informasjonsteknologi1) {
    console.log('9  F)  ',property);}
for (let property in informasjonsteknologi1) {
    console.log('9  G)  ',informasjonsteknologi1[property]);}