#!/usr/bin/node

const { argv } = require('node:process');

const argsCount = argv.length;

if (argsCount < 3) {
  console.log('No argument');
} else if (argsCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
