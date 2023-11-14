#!/usr/bin/node

// Define the addMeMaybe function
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

// Make the function visible from outside
module.exports.addMeMaybe = addMeMaybe;
