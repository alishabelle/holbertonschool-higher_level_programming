#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fp = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(fp, body, 'utf8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
