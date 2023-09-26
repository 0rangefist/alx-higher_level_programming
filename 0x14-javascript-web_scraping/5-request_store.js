#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const argc = process.argv.length;
const argv = process.argv;

if (argc < 4) {
  console.log('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit();
}

// Grab the URL and file path
const url = argv[2];
const filePath = argv[3];

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error(error || `code: ${response.statusCode}`);
  } else {
    // Write response body to specified file
    fs.writeFile(filePath, body, 'utf8', (writeError) => {
      if (writeError) {
        console.error('Error writing to file:', writeError);
      }
    });
  }
});
