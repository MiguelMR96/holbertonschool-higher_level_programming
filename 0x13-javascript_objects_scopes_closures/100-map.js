#!/usr/bin/node
// Imports an array and computes a new array
const list = require('./100-data.js').list;
const array = [];
console.log(list);
list.map(function (i, j) {
  const value = i * j;
  array.push(value);
  return array;
});

console.log(array);
