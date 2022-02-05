function averageSpeed(distanceInitial, distanceFinal, timeInitial, timeFinal) {
    distanceTraveled = distanceFinal - distanceInitial
    timeTraveled = timeFinal - timeInitial
    averageSpeed = distanceTraveled / timeTraveled
    return `The average speed is ${averageSpeed} m/s`
}

console.log(averageSpeed(0, 10, 2, 4))