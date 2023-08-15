#!/usr/bin/node

// This class defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || !Number.isInteger(h) || w <= 0 || h <= 0) {
      // return empty object
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
