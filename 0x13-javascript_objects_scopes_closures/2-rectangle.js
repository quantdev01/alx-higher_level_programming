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
}

module.exports = Rectangle;
