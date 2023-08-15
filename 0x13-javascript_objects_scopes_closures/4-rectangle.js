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

  print (char = 'X') {
    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        process.stdout.write(char);
      }
      console.log();
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}

module.exports = Rectangle;
