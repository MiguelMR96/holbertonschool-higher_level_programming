#!/usr/bin/node
// Diplay the episode name for the give id

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    return console.log(err);
  }
  const jsonData = JSON.parse(response.body);
  console.log(jsonData.title);
});
