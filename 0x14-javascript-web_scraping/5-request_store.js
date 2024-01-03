#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <url> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve webpage content. Status code:', response.statusCode);
  } else {
    // Write the body response to the specified file path in UTF-8 encoding
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
