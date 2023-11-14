#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// Square class that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the Rectangle constructor with the size for both width and height
  }
}

module.exports = Square;
