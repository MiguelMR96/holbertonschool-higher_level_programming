#!/usr/bin/node
// script that reads and prints the content of a file

const process = require('process');

const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
