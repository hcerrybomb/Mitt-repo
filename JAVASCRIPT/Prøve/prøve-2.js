//! A

function randOneTen() {

    return Math.floor(Math.random() * (10 - 1 + 1) ) + 1;
    
}
console.log(randOneTen())

//! B

let randomTall = [];

function fillwithrandom(array,amount){
    for(let i = 0; i < amount; i++){
        array.push(randOneTen())
    }
}

fillwithrandom(randomTall,20)
console.table(randomTall)

document.write("Her er arrayen før vi fjerner 7 tallene:")
for(let i = 0; i < randomTall.length; i++){
    if(i%5===0){
        document.write("<br>")
    }
    document.write(`${randomTall[i]} - `)
}

//! C

function removeSeven(array){
    for(let i = 0; i < array.length; i++){
        if(array[i]===7){
            array.splice(i,1)
            i = i-1
        }
    }
}

removeSeven(randomTall)
console.table(randomTall)

document.write("<br><br>Her er arrayen etter vi fjerner 7 tallene:")
for(let i = 0; i < randomTall.length; i++){
    if(i%5===0){
        document.write("<br>")
    }
    document.write(`${randomTall[i]} - `)
}

document.write("<br><br>")

//! D

function skrivUtArray(array){

    for(let i = 0; i < array.length; i++){
        document.write(`<br>Verdi med indeks ${i} : ${array[i]}`)
    }  

}
skrivUtArray(randomTall)