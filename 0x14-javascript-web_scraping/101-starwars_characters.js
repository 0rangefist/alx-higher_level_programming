#!/usr/bin/node

const request = require('request');

const argc = process.argv.length;
const argv = process.argv;

if (argc < 3) {
  console.log('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit();
}

// Grab the movie id
const movieId = argv[2];

// API url
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Make a GET request to the url
request(url, (error, _response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  const film = JSON.parse(body);

  // Create a function to fetch character names
  function fetchCharacterName (characterURL) {
    return new Promise((resolve, reject) => {
      request(characterURL, (error, _response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  }

  // Create an array of promises for character name requests
  const characterPromises = film.characters.map(fetchCharacterName);

  // Resolve all character promises
  Promise.all(characterPromises)
    .then(characterNames => {
      // Print each character name from the promise array
      characterNames.forEach(characterName => {
        console.log(characterName);
      });
    })
    .catch(err => {
      console.error(err);
      process.exit(1);
    });
});
