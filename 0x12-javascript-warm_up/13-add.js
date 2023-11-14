#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

// Make the function visible from outside
module.exports.add = add;
