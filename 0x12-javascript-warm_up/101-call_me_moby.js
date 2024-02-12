#!/usr/bin/node
const myFunctions = {};

myFunctions.executeXTimes = function(x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
};

function myFunction() {
    console.log("Executing myFunction");
}

myFunctions.executeXTimes(5, myFunction);
