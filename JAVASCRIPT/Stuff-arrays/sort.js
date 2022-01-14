const drikke = ["te","vann","kaffe","appelsinsaft"]

//*drikke.sort();

//*console.log(drikke);

const tallArr = [4,41,1,101,82,14]

//*tallArr.sort();

//*console.log(tallArr);

function sammenligningsFunksjon(a,b){
    console.log(a + " - " + b + " = " + (a - b))
    return a - b;
}

function omvendtSammenligningsFunksjon(a,b){
    //*console.log(a + " - " + b + " = " + (a - b))
    return b - a;
}

//*tallArr.sort(sammenligningsFunksjon)

//*console.log(tallArr)

tallArr.reverse()

//*console.log(tallArr)



//!     OPPGAVE 1

let array1 = [2, 1, 7, 5]

array1.sort(sammenligningsFunksjon)

console.log("1.",array1)

let array2 = ["melon", "eple", "appelsin", "ananas", "pære"]

array2.sort()

console.log("1.",array2)

let array3 = [2, 10, 104, 17, 82, 109]

array3.sort(sammenligningsFunksjon)

console.log("1.",array3)

//!     OPPGAVE 2

console.log("2.den sorterer ved å finne differansen mellom hvert indeks fra venstre til høyre")

//!     OPPGAVE 3

let opg3List = [2, 10, 104, 17, 82, 109]

opg3List.sort(omvendtSammenligningsFunksjon)

console.log("3.",opg3List)

array2.sort(omvendtSammenligningsFunksjon)

console.log("3.",array2)


//TODO      BLI  F E R D I G 


//!     OPPGAVE 4

let personer = [["Hans", 12], ["Nils", 3], ["Sofie", 5]];

for(let i = 0; i < personer.length; i++){
    

    
}
