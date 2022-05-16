import { updateApiDatabase } from "./utils/load-battlemetrics.js"
import { logEvent, logTest } from "./utils/logging.js"

let useApi = false


let serverElements = []

let db, collectionName = `servers`, dbDocs

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

function update(){
    db.collection(collectionName)
    .orderBy(`rank`,`desc`)
    .get().then((snapshot)=> {
        dbDocs = snapshot.docs;
    })
    logEvent("general database updated")
}

db.collection(collectionName).onSnapshot(snapshot => {
    update()
})











function makeServerElements(docs, array){
    array = []
    let serverContainerEl = document.createElement("div")
    serverContainerEl.className = "server-container"

    let serverTitleEl  = document.createElement("div")
    serverTitleEl.className = "server-title"
    serverContainerEl.appendChild(serverTitleEl)

    let serverDescriptionEl = document.createElement("div")
    serverDescriptionEl.className = "description"




}






export { logEvent, logTest}