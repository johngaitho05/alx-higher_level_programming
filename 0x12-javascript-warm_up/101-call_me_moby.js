#!/usr/bin/node

// Define the callMeMoby function
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Make the function visible from outside
module.exports.callMeMoby = callMeMoby;
