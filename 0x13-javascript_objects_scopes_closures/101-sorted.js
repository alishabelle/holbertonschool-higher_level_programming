#!/usr/bin/node
const dict = require('./101-data.js').dict;
const d = {};
for (const k in dict) {
  if (d[dict[k]] === undefined) {
    d[dict[k]] = [];
  }
  d[dict[k]].push(k);
}
console.log(d);
