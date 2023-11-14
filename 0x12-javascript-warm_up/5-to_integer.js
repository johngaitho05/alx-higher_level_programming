#!/usr/bin/node

// Convert the first argument to an integer
const firstArgument = process.argv[2];
const integerNumber = parseInt(firstArgument);

// Check if the conversion is successful
if (!isNaN(integerNumber)) {
  console.log(`My number: ${integerNumber}`);
} else {
  console.log('Not a number');
}
