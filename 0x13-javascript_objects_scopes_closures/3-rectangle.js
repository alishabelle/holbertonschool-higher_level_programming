#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x;
    let y;
    let make = '';
    for (x = 0; x < this.height; x++) {
      if (x > 0) {
        make += '\n';
      }
      for (y = 0; y < this.width; y++) { make += 'X'; }
    }
    console.log(make);
  }
}
module.exports = Rectangle;
