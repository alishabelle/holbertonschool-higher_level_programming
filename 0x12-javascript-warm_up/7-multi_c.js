#!/usr/bin/node


if (process.argv[2] === undefined) {
    console.log('Missing number of occurrences')
}

for (let a = 0; a < process.argv[2]; a++) {
    console.log('C is fun');
}
