"use strict";

let statesNeeded = new Set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]);

const stations = {};
stations["kone"] = new Set(["id", "nv", "ut"]);
stations["ktwo"] = new Set(["wa", "id", "mt"]);
stations["kthree"] = new Set(["or", "nv", "ca"]);
stations["kfour"] = new Set(["nv", "ut"]);
stations["kfive"] = new Set(["ca", "az"]);


function mySetCovering(statesNeeded, stations) {
    const finalStations = new Set();
    while (statesNeeded.size) {
        let bestStation = null;
        let statesCovered = new Set();
        for (let station in stations) {
            const states = stations[station];
            const covered = new Set([...statesNeeded].filter(x => states.has(x)));   // это типа пересечение множеств
            if (covered.size > statesCovered.size) {
                bestStation = station;
                statesCovered = covered;
            }
        }
        if (bestStation !== null) {
            statesNeeded = new Set([...statesNeeded].filter(x => !statesCovered.has(x)));  // а это типа вычитание множеств
            finalStations.add(bestStation);
            delete stations[bestStation];
        } else {
            return null;
        }
    }

    return finalStations;
}

const result = mySetCovering(statesNeeded, stations);
console.log(result);

