import { updateApiDatabase } from "./utils/load-battlemetrics.js"
import { logEvent, logTest } from "./utils/logging.js"

let useApi = false

let validAdd = false

let 
officialChecked = false,  
onlineChecked = false,  
rankChecked = true,  
popChecked = false

let feedEl = document.getElementById("feed")

let db, collectionName = `servers`, orderBy = `rank`, way=`asc`, dbDocs

const firebaseConfig = {
    apiKey: "AIzaSyAAR_0o6XXCf66RK8ck2cnjJTO3SKJqy1g",
    authDomain: "rust-server-db.firebaseapp.com",
    projectId: "rust-server-db",
    storageBucket: "rust-server-db.appspot.com",
    messagingSenderId: "1026127148712",
    appId: "1:1026127148712:web:4a54c73bae6420d929349d"
  };

firebase.initializeApp(firebaseConfig);
logEvent("app init")

db = firebase.firestore();
logEvent("firestore init")

if(useApi){
    updateApiDatabase()
    collectionName = `server-api`
    logEvent("api database updated + loaded")

}

function update(order, way){
    db.collection(collectionName).orderBy(order, way).get().then((snapshot)=> {
        dbDocs = snapshot.docs;
        printServers(officialChecked, onlineChecked, rankChecked, popChecked, dbDocs)
    })
}
update(orderBy, way)


db.collection(collectionName).onSnapshot(snapshot => {
    update(orderBy, way)
})



let officialButton = document.getElementById("official-button-input")
officialButton.addEventListener("click",function(){
    if(officialChecked){
        officialChecked = false
        officialButton.style.backgroundImage = "none"
    }
    else{
        officialChecked = true
        officialButton.style.backgroundImage = "linear-gradient(to right, rgba(46, 240, 204, 0.5), rgba(46, 240, 204, 0.9))"
    }

    logEvent(`official being checked is now: ${officialChecked}`)
    update(orderBy, way)
})


let onlineButton = document.getElementById("online-button-input")
onlineButton.addEventListener("click",function(){
    if(onlineChecked){
        onlineChecked = false
        onlineButton.style.backgroundImage = "none"
    }
    else{
        onlineChecked = true
        onlineButton.style.backgroundImage = "linear-gradient(to right, rgba(46, 240, 204, 0.5), rgba(46, 240, 204, 0.9))"
    }

    logEvent(`online being checked is now: ${onlineChecked}`)
    update(orderBy, way)

})


let rankButton = document.getElementById("rank-button-input")
rankButton.addEventListener("click", function(){
    if(rankChecked){
        rankChecked = true
        popChecked = false
        popButton.style.backgroundImage = "none"
        rankButton.style.backgroundImage = "linear-gradient(to right, rgba(46, 240, 204, 0.5), rgba(46, 240, 204, 0.9))"
        orderBy = `population`, way=`desc`
    }
    if(popChecked){
        rankChecked = true
        popChecked = false
        popButton.style.backgroundImage = "none"
        rankButton.style.backgroundImage = "linear-gradient(to right, rgba(46, 240, 204, 0.5), rgba(46, 240, 204, 0.9))"
        orderBy = `rank`, way = `asc`
    }

    logEvent(`rankbutton checked is now: ${rankChecked},  popbutton checked is now ${popChecked}`)
    update(orderBy, way)

})




let popButton = document.getElementById("pop-button-input")
popButton.addEventListener("click",function(){
    if(rankChecked){
        rankChecked = false
        popChecked = true
        rankButton.style.backgroundImage = "none"
        popButton.style.backgroundImage = "linear-gradient(to right, rgba(46, 240, 204, 0.5), rgba(46, 240, 204, 0.9))"
        orderBy = `rank`, way = `asc`
    }
    if(popChecked){
        rankChecked = false
        popChecked = true
        rankButton.style.backgroundImage = "none"
        popButton.style.backgroundImage = "linear-gradient(to right, rgba(46, 240, 204, 0.5), rgba(46, 240, 204, 0.9))"
        orderBy = `population`, way=`desc`
    }

    logEvent(`rankbutton checked is now: ${rankChecked},  popbutton checked is now ${popChecked}`)
    update(orderBy, way)

})





function printServers(official, online, rank, pop, docs){
    logEvent(`\nShow only Official:${official},   \nShow only Online:${online},   \nSort by Rank:${rank},   \nSort by Pop:${pop}`)


    let addOnlineChecked = false, addOfficialChecked = false


    feedEl.innerHTML = ""

    feedEl.innerHTML = feedEl.innerHTML + `
<div id="add-container">
    <div class="server-title" id="add-server-title">
        <input type="text" placeholder="ADD SERVER" id="add-name-input">
        <label class="add-label">ADD
            <button class="add-button" id="add-server-button">

            </button>
        </label>                            
    </div>
    <br>
    <div class="description">
        <div class="rank">
            <div class="column">RANK:</div>
            <div class="rank-content">
                <input id="rank-input" type="number" max="999" placeholder="000">
            </div>
        </div>  
        <div class="population">
            <div class="column">POPULATION:</div>
            <div class="population-content">
                <input id="population-input" type="number"  max="999" placeholder="000">
            </div>
        </div>
        <div class="ip">
            <div class="column">IP ADDRESS:</div>
            <div class="ip-content">
                <input id="ip-input" type="text" placeholder="000.000.000.000:00000">
            </div>
        </div>
        <div class="status">
            <div class="column">ONLINE:</div>
            <div class="status-content" id="add-online-container">
                <label id="add-online-label">
                    <button id="add-online-button">

                    </button>
                </label>
            </div>
        </div>
        <div class="official">
            <div class="column">OFFICIAL:</div>
            <div class="official-content" id="add-official-container">
                <label id="add-official-label">
                    <button id="add-official-button">

                    </button>
                </label>
            </div>
        </div>  
        <div class="uptime">
            <div class="column">UPTIME:</div>
            <div class="uptime-content">
                <input id="uptime-input" type="number" max="100" placeholder="00">% last 30 days
            </div>
        </div>
    </div>
    <br><br><br><br>
</div>
    `




    let buttonIds = []
    for (let i = 0; i < docs.length; i++){
        

        let statusBool = docs[i].data().data.status
        if(online && !statusBool)continue
        statusBool ? statusBool = "online": statusBool = "offline"

        let moddedBool = docs[i].data().data.modded
        if(official && moddedBool)continue
        moddedBool ? moddedBool = "no" : moddedBool = "yes"

        
        

        let serverId = docs[i].id
        let serverTitle = docs[i].data().name
        let rankNumber = docs[i].data().rank
        let popNumber = docs[i].data().population
        let ipString = docs[i].data().data.ip



        let uptimeNumber = docs[i].data().data.uptime

        feedEl.innerHTML = feedEl.innerHTML + `
    <div class="server-container">
        <div class="server-title">${serverTitle}
            <label class="delete-label">DELETE
                <button class="delete-button" id='${serverId}'>

                </button>
            </label>                             
        </div>
        <br>
        <div class="description">
            <div class="rank">
                <div class="column">RANK:</div>
                <div class="rank-content">#${rankNumber}</div>
            </div>  
            <div class="population">
                <div class="column">POPULATION:</div>
                <div class="population-content">${popNumber}</div>
            </div>
            <div class="ip">
                <div class="column">IP ADDRESS:</div>
                <div class="ip-content">${ipString}</div>
            </div>
            <div class="status">
                <div class="column">STATUS:</div>
                <div class="status-content">${statusBool}</div>
            </div>
            <div class="official">
                <div class="column">OFFICIAL:</div>
                <div class="official-content">${moddedBool}</div>
            </div>  
            <div class="uptime">
                <div class="column">UPTIME:</div>
                <div class="uptime-content">${uptimeNumber}% last 30 days</div>
            </div>
        </div>
        <br><br><br><br>
    </div>`

    buttonIds.push(serverId)
    }

    for (let j = 0; j < buttonIds.length; j++){
        document.getElementById(buttonIds[j]).addEventListener("click", function(e){
            console.log("BUTTON PRESSED", e.target.id)
            db.collection(collectionName).doc(e.target.id).delete();
            update(orderBy, way)
        })
    }





    document.getElementById('add-online-button').addEventListener("click", function(e){
        console.log("ADD ONLINE TICKED")
        if(addOnlineChecked){
            addOnlineChecked = false
            e.target.style.backgroundImage = "none"
        }
        else{
            addOnlineChecked = true
            e.target.style.backgroundImage = "linear-gradient(to right, rgba(46, 240, 204, 0.5), rgba(46, 240, 204, 0.9))"
        }
        console.log("ADD ONLINE IS NOW:",addOnlineChecked)
    })
    document.getElementById('add-official-button').addEventListener("click",function(e){
        console.log("ADD OFFICIAL TICKED")
        if(addOfficialChecked){
            addOfficialChecked = false
            e.target.style.backgroundImage = "none"
        }
        else{
            addOfficialChecked = true
            e.target.style.backgroundImage = "linear-gradient(to right, rgba(46, 240, 204, 0.5), rgba(46, 240, 204, 0.9))"
        }
        console.log("ADD OFFICIAL IS NOW:",addOfficialChecked)
    })

    
    document.getElementById('add-server-button').addEventListener("click",function(){
        

        let addServerTitleEl = document.getElementById("add-server-title")
        let invalidInputEl = document.createElement("label")
        invalidInputEl.className = "invalid-label"
        invalidInputEl.setAttribute('id', 'invalid-label') 
        invalidInputEl.innerHTML = "INVALID INPUT&nbsp&nbsp:&nbsp&nbspCHECK FOR MISSING OR WRONGLY FORMATTED INPUTS"
        console.log("ADD PRESSED")

        let serverTitleInput = document.getElementById("add-name-input")

        let rankInput = document.getElementById("rank-input")
        
        let popInput = document.getElementById("population-input")
        
        let ipInput = document.getElementById("ip-input")

        let str = ipInput.value
        let docId = ipInput.value
        str = str.substring(str.length - 6)

        let uptimeInput = document.getElementById("uptime-input")

        docId = docId.replace(/[^a-zA-Z0-9]/g, '')

        for(let n = 0; n < buttonIds.length; n++){
            if(docId.toLowerCase() == buttonIds[n].toLowerCase()){
                validAdd = false

                
            }
        }

        if(serverTitleInput.value == ""){
            validAdd = false
        }

        else if(rankInput.value < 0 || rankInput.value > 999){
            validAdd = false
        }


        else if(popInput.value < 0 || popInput.value > 999){
            validAdd = false
        }


        else if(str.charAt(0) !== ":"){
            validAdd = false
        }
        else if(str.substring(str.length - 5).match(/^[0-9]+$/) == null){
            validAdd = false
        }


        else if(uptimeInput.value < 0 || uptimeInput.value > 100){
            validAdd = false
        }
        else{
            validAdd = true
        }
        




        if(validAdd){
            try{
                document.getElementById("invalid-label").remove()  
            }
            catch{
                logEvent("NO LABEL TO REMVE")
            }
           //TODO SUBMIT THE WHOLE SERVER OBJECT

            


            db.collection(collectionName).add(



            )

        }
        else{
            try{
                document.getElementById("invalid-label").remove()  
            }
            catch{
                logEvent("NO LABEL TO REMVE")
            }
            addServerTitleEl.appendChild(invalidInputEl)
        }
    })

}
//TODO STYLE INPUTS AND ADD LISTENER FOR ADD BUTTON THAT CHECKS THAT EVERY REQUIREMENT IS MET

//TODO ADD EDIT BUTTON FOR EACH INDIVIDUAL FIELD IN EACH SERVER











export { logEvent, logTest}