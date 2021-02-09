#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const wedgeUrl = 'https://swapi.co/api/people/18/';
let i = 0;
let matchCount = 0;

request.get(url, function (err, res, results) {
  if (err) {
    return console.log(err);
  }
  const jsonFormat = JSON.parse(results);
  const movieList = jsonFormat.results;
  for (; i < movieList.length; i++) {
    const charList = movieList[i].characters;
    for (let j = 0; j < charList.length; j++) {
      if (charList[j] === wedgeUrl) {
        matchCount++;
      }
    }
  }
  console.log(matchCount);
});
