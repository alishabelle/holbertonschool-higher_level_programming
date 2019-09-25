#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const ret = {};
  const tsk = JSON.parse(body);
  for (const num of tsk) {
    if (num.completed === true) {
      if (ret[num.userId] === undefined) {
        ret[num.userId] = 0;
      }
      ret[num.userId]++;
    }
  }
  console.log(ret);
});
