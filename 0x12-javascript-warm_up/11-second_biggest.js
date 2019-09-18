#!/usr/bin/node

let array = process.argv;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  array = array.sort();
  const see = array[array.length - 2];
  console.log(parseInt(see));
}
