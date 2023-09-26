#!/usr/bin/node

const request = require('request');

const argc = process.argv.length;
const argv = process.argv;

function isInteger (str) {
  const num = parseInt(str, 10);
  return !isNaN(num) && Number.isInteger(num);
}

if (argc < 3) {
  console.log('Usage: ./3-starwars_title.js <id>');
  process.exit();
}

// grab the url
const movieId = argv[2];
if (!isInteger(movieId)) {
  console.log('Usage: ./3-starwars_title.js <id>');
  process.exit();
}

// api url
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// make a GET request to the url
request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    body = JSON.parse(body);
    console.log(body.title); // Print status code
  }
});
