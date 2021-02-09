#!/usr/bin/node
// Display status code of a request

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) throw err;
  console.log('code:', res.statusCode);
});
