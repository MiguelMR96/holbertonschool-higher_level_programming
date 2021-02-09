#!/usr/bin/node
// Returns reversed version of a list
exports.esrever = function (str) {
  const reversed = [];
  for (let i = str.length - 1; i >= 0; i--) {
    reversed.push(str[i]);
  }
  return reversed;
};
