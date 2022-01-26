

function getValuesRockets(){
    let LGF, frags, explosives, pipes, pureGPSulf, GPForExplosives, sulfurForExplosives, exploGPSulf
    let amtOfRockets = document.getElementById("amtOfRockets").value
    
        pipes = amtOfRockets * 2
        rocketGP = amtOfRockets * 150
            pureGPSulf = rocketGP * 2

        explosives = amtOfRockets * 10
            LGF = explosives * 3
            frags = explosives * 10
            sulfurForExplosives = explosives * 10
            GPForExplosives = explosives * 50
                exploGPSulf = GPForExplosives * 2

    document.write("pipes needed ",pipes,"<br>")
    document.write("rocket gp needed ",rocketGP,"<br>")
    document.write("sulf for that gp needed ",pureGPSulf,"<br>")
    document.write("explosives needed ",explosives,"<br>")
    document.write("LGF needed ",LGF,"<br>")
    document.write("frags needed ",frags,"<br>")
    document.write("sulfur for the explosives needed ",sulfurForExplosives,"<br>")
    document.write("gp for that explosives needed ",GPForExplosives,"<br>")
    document.write("sulf for that gp needed ",exploGPSulf,"<br>")
}