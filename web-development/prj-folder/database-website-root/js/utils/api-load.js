
let dataObj = []
let link="https://api.battlemetrics.com/servers?filter[game]=rust"


async function updateApiDatabase(){
    testEvent("reach?")
    for(let i = 0; i < 10; i++){
        let response = await fetch(link)
        let data = await response.json()
        dataObj.push(data.data)
        link = data.links.next
    }
    console.log(dataObj)
}