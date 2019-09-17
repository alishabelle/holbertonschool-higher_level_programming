#!/usr/bin/node

if (process.argv.slice(2).length === 0) {
  console.log('No arguement');
} else if (process.argv.slice(2).length < 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
