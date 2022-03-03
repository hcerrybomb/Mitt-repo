//! A

let olympics = [
    {
        land:'Norge',
        sted:'Lillehammer',
        arstall:1994,
    },
    {
        land:'Japan',
        sted:'Nagano',
        arstall:1998,
    },
    {
        land:'USA',
        sted:'Salt Lake City',
        arstall:2002,
    },
    {
        land:'Italia',
        sted:'Torino',
        arstall:2006,
    }
];console.table(olympics);

//! B

function printListObjects(array){

    for(let i = 0; i < array.length; i++){
        document.write(`Vinter-OL i ${array[i].arstall} ble arrangert i ${array[i].sted} i ${array[i].land} <br>`)
    }

}

printListObjects(olympics)

document.write("<br>")

//! C

printListObjects = function(array){
    for(let i = 0; i < array.length; i++){
        if(array[i].arstall > 2000){
            document.write(`Vinter-OL i ${array[i].arstall} ble arrangert i ${array[i].sted} i ${array[i].land} <br>`)
        }
    }
}

//! D

function sammenlignString(a,b){
    if(a.land > b.land){
        return 1 
    }
    else if(a.land < b.land){
        return -1
    }
    else{
        return 0 
    }
    //* Sorterer etter lengden av landets navn
}

olympics.sort(sammenlignString);console.table(olympics);

printListObjects(olympics)