#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let num = 0;
    const results = JSON.parse(body).results;
    for (const film of results) {
      for (const pers of film.characters) {
        if (pers.includes('/18/')) {
          num++;
        }
      }
    }
    console.log(num);
  }
});
