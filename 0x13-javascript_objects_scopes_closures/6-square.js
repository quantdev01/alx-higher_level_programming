#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
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
    } else {
      let i = 0;
      let j = 0;

      while (i < this.height) {
        j = 0;

        while (j < this.width) {
          process.stdout.write(c);
          j++;
        }
        console.log('');
        i++;
      }
    }
  }
}
module.exports = Square;
