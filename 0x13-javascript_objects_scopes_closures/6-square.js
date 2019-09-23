#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      const maker = c;
      const line = maker.repeat(this.width);
      for (let x = 0; x < this.height; x++) {
        console.log(line);
      }
    }
  }
}
module.exports = Square;
