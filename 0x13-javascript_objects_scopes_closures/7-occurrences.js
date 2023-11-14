#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Initialize a variable to store the count of occurrences
  let count = 0;

  // Iterate through the list and increment count when the searchElement is found
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  // Return the final count
  return count;
};
