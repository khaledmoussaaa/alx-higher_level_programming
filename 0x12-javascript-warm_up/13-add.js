#!/usr/bin/node
// 13-add.js

// Define an object with a method named add
const mathFunctions = {};

// Add a method to the object to add two integers
mathFunctions.add = function(a, b) {
    return a + b;
};

// Export the object containing the add method
module.exports = mathFunctions;
const add = require('./13-add').add;
console.log(add(3, 5));
