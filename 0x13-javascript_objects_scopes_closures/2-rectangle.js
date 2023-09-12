#!/usr/bin/node

class Rectangle {
  constructor (w = undefined, h = undefined) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
