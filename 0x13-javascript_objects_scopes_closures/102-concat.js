#!/usr/bin/node

const fs = require('fs');

const f1 = fs.readFileSync(process.argv[2]);
const f2 = fs.readFileSync(process.argv[3]);
fs.appendFile(process.argv[4], f1, (err) => {
  if (err) throw err;
});
fs.appendFile(process.argv[4], f2, (err) => {
  if (err) throw err;
});
