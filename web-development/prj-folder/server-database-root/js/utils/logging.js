let start = Date.now();
let duration
let eventCount = 0, testCount = 0





function logEvent(str){

    duration = Date.now() - start
    console.log(`%cEvent:`,`color:rgb(0, 140, 255); font-weight:bolder; font-size:16px;`,`[${eventCount}] | ${str} `)
    console.log(`%cScope:`,`color:rgb(120, 190, 248);font-weight:bold;`,`${duration}ms\n\n`)
    eventCount++
    start = Date.now();
}

function logTest(str){

    duration = Date.now() - start
    console.log(`%cTest: `,`color:rgb(124, 255, 36); font-weight:bolder; font-size:16px;`,`[${testCount}] | ${str} `)
    console.log(`%cScope:`,`color:rgb(165, 245, 112);font-weight:bold;`,`${duration}ms\n\n`)
    testCount++
    start = Date.now();
}

export { logEvent, logTest }