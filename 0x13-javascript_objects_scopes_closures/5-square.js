#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// This class defines a Square that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
