#!/usr/bin/node
const SquareBase = require('./5-square');

// Square class that inherits from SquareBase
class Square extends SquareBase {
  constructor (size) {
    super(size, size); // Call the SquareBase constructor with the size for both width and height
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
