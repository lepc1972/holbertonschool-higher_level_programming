#!/usr/bin/node

const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c = 'X') {
    for (let x = 0; x < this.width; x++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
