#!/usr/bin/node

/* class creation */

class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(h) || isNaN(w)) {
      delete this.width;
      delete this.height;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;

    while (i < this.height) {
      j = 0;

      while (j < this.width) {
        process.stdout.write('X');
        j++;
      }
      console.log('');
      i++;
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
