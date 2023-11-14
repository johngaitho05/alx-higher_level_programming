#!/usr/bin/node

// Check if the first argument exists
const firstArgument = process.argv[2];

// Print the corresponding message based on the existence of the first argument
if (firstArgument !== undefined) {
  console.log(firstArgument);
} else {
  console.log('No argument');
}
