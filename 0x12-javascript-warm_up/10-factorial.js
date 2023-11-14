#!/usr/bin/node

// Define a recursive function to compute the factorial
const computeFactorial = (n) => {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }

  n = parseInt(n);

  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
};

// Get the first argument from the command line
const input = process.argv[2];

// Compute and print the factorial
const result = computeFactorial(input);
console.log(result);
