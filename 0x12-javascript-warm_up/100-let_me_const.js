#!/usr/bin/node
this.executeXTimes = function(x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
};
function myFunction() {
    console.log("Executing myFunction");
}

executeXTimes(5, myFunction);
