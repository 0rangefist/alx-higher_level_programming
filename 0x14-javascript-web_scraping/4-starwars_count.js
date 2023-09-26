#!/usr/bin/node

const request = require('request');

// grab the api url
const url = process.argv[2];

// number of times char 'Wedge Antilles' is preset
let wedgeCount = 0;

// make a GET request to the url
request(url, (_error, _response, body) => {
  const films = JSON.parse(body).results;

  for (const film of films) {
    for (const character of film.characters) {
      const characterId = character.split('/')[5];
      if (characterId === '18') {
        // Wedge Antilles found, so add to count
        wedgeCount++;
      }
    }
  }
  // Print total count of char 'Wedge Antilles'
  console.log(wedgeCount);
});
