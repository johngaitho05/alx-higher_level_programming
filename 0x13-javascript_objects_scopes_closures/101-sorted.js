#!/usr/bin/node
const { dict } = require('./101-data');

// Initialize a new dictionary for user ids by occurrence
const userIdsByOccurrence = {};

// Iterate over the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // Check if occurrences is already a key in the new dictionary
  if (occurrences in userIdsByOccurrence) {
    userIdsByOccurrence[occurrences].push(userId);
  } else {
    userIdsByOccurrence[occurrences] = [userId];
  }
}

// Print the new dictionary
console.log(userIdsByOccurrence);
