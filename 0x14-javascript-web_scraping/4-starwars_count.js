#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, (err, response) => {
  if (err) {
    return console.log(err);
  }
  const jsonData = JSON.parse(response.body);
  for (let step = 0; jsonData.results[step]; step++) {
    for (let j = 0; jsonData.results[step].characters[j]; j++) {
      if (jsonData.results[step].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        count++;
      }
    }
  }
  return console.log(count);
});
