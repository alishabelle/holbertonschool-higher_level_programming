#!/usr/bin/node


/*let array = process.argv;

if (process.argv.length === 0 || process.argv.length === 1) {
  console.log(0);
} else {
  array = array.sort();
  let see = array[array.length - 2];
}
  console.log(parseInt(see));*/

console.log(process.argv.slice(2).length);
console.log(process.argv.length);
