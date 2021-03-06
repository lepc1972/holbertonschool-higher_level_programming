#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let row = '';
      for (let y = 0; y < this.width; y++) {
        row = row + 'X';
      }
      console.log(row);
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }
}

module.exports = Rectangle;
