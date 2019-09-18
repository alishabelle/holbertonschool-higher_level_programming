#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let  array = process.argv.sort();
  const see = array[array.length - 2];
  console.log(parseInt(see));
}
