#!/usr/bin/node

const request = require('request');

const argc = process.argv.length;
const argv = process.argv;

if (argc < 3) {
  console.log('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit();
}

// Grab the movie id
const movieId = argv[2];

// API url
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Make a GET request to the url
request(url, (_error, _response, body) => {
  const film = JSON.parse(body);

  for (const characterURL of film.characters) {
    // Make a request to the characterURL to get name
    request(characterURL, (_error, _response, body) => {
      const characterName = JSON.parse(body).name;
      // Print the character name
      console.log(characterName);
    });
  }
});
