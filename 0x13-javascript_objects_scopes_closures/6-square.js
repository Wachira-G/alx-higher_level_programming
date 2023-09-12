#!/usr/bin/node

const Squa = require('./5-square');

class Square extends Squa {
  charPrint (c) {
    if (c === null || c === undefined) {
      this.print();
    } else {
      let i = this.width;
      while (i > 0) {
        console.log(`${c.repeat(this.width)}`);
        i--;
      }
    }
  }
}

module.exports = Square;
