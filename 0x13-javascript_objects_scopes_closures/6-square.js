#!/usr/bin/node

const simpleSquare = require('./5-square');

// This class defines a Square that inherits from simple Sqaure
class Square extends simpleSquare {
  charPrint (c) {
    super.print(c);
  }
}

module.exports = Square;
