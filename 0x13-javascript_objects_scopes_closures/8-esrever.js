#!/usr/bin/node

exports.esrever = function (list) {
  const jawn = [];
  for (let x = list.length - 1; x >= 0; x--) {
    jawn.push(list[x]);
  }
  return jawn;
};
