// Speed Limit = 70
// 5 -> point
// Math.floor
// 12 points -> suspended
checkSpeed(71);

function checkSpeed(speed) {
    let speedLimit = 70
    let kmPerPoint = 5
    if (speed <= speedLimit)
        console.log("Oki")
    else {
        let point = Math.floor((speed - speedLimit) / kmPerPoint)
        if (point >= 12)
            console.log("Licens Suspended")
        else
            console.log("Point :" + point)
    }


}