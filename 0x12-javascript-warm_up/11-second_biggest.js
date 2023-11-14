#!/usr/bin/node

// Get the arguments from the command line
const args = process.argv.slice(2);

// Check the number of arguments
const numArgs = args.length;

// If no argument or only one argument is passed, print 0
if (numArgs <= 1) {
  console.log(0);
} else {
  // Convert the arguments to integers and sort them in descending order
  const sortedIntegers = args.map(Number).sort((a, b) => b - a);

  // Print the second-biggest integer
  console.log(sortedIntegers[1]);
}
