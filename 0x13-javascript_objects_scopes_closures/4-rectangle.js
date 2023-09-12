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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}
module.exports = Rectangle;
