#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of command line arguments are provided
if (process.argv.length !== 5) {
  console.log('Usage: ./concatFiles.js <file1> <file2> <destination>');
  process.exit(1);
}

// Extract file paths from command line arguments
const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

// Read content from the first file
fs.readFile(file1Path, 'utf8', (err, file1Content) => {
  if (err) {
    console.error(`Error reading ${file1Path}: ${err.message}`);
    process.exit(1);
  }

  // Read content from the second file
  fs.readFile(file2Path, 'utf8', (err, file2Content) => {
    if (err) {
      console.error(`Error reading ${file2Path}: ${err.message}`);
      process.exit(1);
    }

    // Concatenate contents of both files
    const concatenatedContent = file1Content + file2Content;

    // Write the concatenated content to the destination file
    fs.writeFile(destinationPath, concatenatedContent, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationPath}: ${err.message}`);
        process.exit(1);
      }
    });
  });
});
