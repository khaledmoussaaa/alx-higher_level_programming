#!/usr/bin/node
// 101-call_me_moby.js

// Define an object with a method named callMeMoby
const callMeMoby = {};

// Add a method to the object to call the provided function x times
callMeMoby.callMeMoby = function(x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
};

// Export the object containing the callMeMoby method
module.exports = callMeMoby;

