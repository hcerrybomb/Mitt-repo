function randMinMax(min, max) {
    return Math.floor(Math.random() * (max - min + 1) ) + min;
    } 
function rockPaperScissor(x){
    if(x === 1){
        return "stein"
    }
    else if(x === 2){
        return "papir"
    }
    else if(x === 3){
        return "saks"
    }
}
var vinnerIkkeFunnet = true
while(vinnerIkkeFunnet){
    var dittKast = randMinMax(1,3)
    dittKast = rockPaperScissor(dittKast)
    var maskinKast = randMinMax(1,3)
    maskinKast = rockPaperScissor(maskinKast)
    console.log(dittKast,maskinKast)

    //document.write("<br>du fikk: ",dittKast,"<br>maskinen fikk:  ",maskinKast,"<br>")
    if(dittKast === maskinKast){
        //document.write("<br>samme kast")
        //document.write("<br>spiller igjen<br><br><br>")
        vinnerIkkeFunnet = true
    }
    else if(dittKast === "stein" && maskinKast === "saks"){
        //document.write("du vant!")
        vinnerIkkeFunnet = false
    }
    else if(dittKast === "papir" && maskinKast === "stein"){
        //document.write("du vant!")
        vinnerIkkeFunnet = false
    }
    else if(dittKast === "saks" && maskinKast === "papir"){
        //document.write("du vant!")
        vinnerIkkeFunnet = false
    }
    else if(dittKast === "saks" && maskinKast === "stein"){
        //document.write("maskinen vant")
        vinnerIkkeFunnet = false
    }
    else if(dittKast === "stein" && maskinKast === "papir"){
        //document.write("maskinen vant")
        vinnerIkkeFunnet = false
    }
    else if(dittKast === "papir" && maskinKast === "saks"){
        //document.write("maskinen vant")
        vinnerIkkeFunnet = false
    }
}
//! OPPGAVE 2

function returnerTilfeldigTall(min, max, runs = 1) { //setter parameter min max og antall tall
    for(let i = 1; i <= runs; i++){                  //printer ut et tall for antall tall
        //document.write("tilfeldig tall: ", Math.floor(Math.random() * (max - min + 1) ) + min,
        //"<br>run nr:  ",i,"<br><br>")
    }
    } 

returnerTilfeldigTall(10,30)


//! OPPGAVE 3.0
var tall1 = 50
var tall2 = 85
//document.write(tall1,"   ",tall2,"<br><br>")
function byttTall(førstetall, andretall){
    placeholder1 = førstetall
    placeholder2 = andretall
    førstetall = placeholder2
    andretall  = placeholder1
    byttedetall = førstetall+"  "+andretall
    return byttedetall
}
//document.write(byttTall(tall1,tall2))


//! OPPGAVE 4


function erImellom(variab, intervall1, intervall2){
    if(variab >= intervall1 && intervall2 >= variab){
        document.write("taller er imellom")
    }
    else{
        document.write("det er ikke imellom")
    }
}


//! OPPGAVE 5


function primtall(tall){
    if(tall%1===0){
        
    }
}