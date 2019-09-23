#!/usr/bin/node

exports.converter = function (base) {
  function num (input) {
    return input.toString(base);
  }
  return num;
};
