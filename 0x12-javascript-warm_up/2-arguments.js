#!/usr/bin/node

/*console.log(process.argv);
console.log(process.argv.slice(2).length);*/
if (process.argv.slice(2).length === 0) {
  console.log('No arguement');
} else if (process.argv.slice(2).length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
