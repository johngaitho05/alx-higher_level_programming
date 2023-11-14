#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

// Add the incr function to the myObject
myObject.incr = function incr () {
  this.value++;
};

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
