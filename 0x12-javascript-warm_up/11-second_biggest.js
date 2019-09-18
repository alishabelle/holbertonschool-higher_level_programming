#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const array = process.argv.sort();
  const see = array[process.argv.length - 2];
  console.log(parseInt(see));
}
