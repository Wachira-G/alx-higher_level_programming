#!/usr/bin/node

class Rectangle {
  constructor (w = undefined, h = undefined) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let height = this.height;
    while (height > 0) {
      console.log(`${'X'.repeat(this.width)}`);
      height--;
    }
  }
}
module.exports = Rectangle;
