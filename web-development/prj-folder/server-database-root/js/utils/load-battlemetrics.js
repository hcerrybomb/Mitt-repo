import { logEvent, logTest} from "./logging.js"

function updateApiDatabase(){
    logTest("reach?")
    logEvent("api server init")
}

export { updateApiDatabase }