#!/usr/bin/node

const request = require('request');

const argc = process.argv.length;
const argv = process.argv;

if (argc < 3) {
  console.log('Usage: ./2-statuscode.js <url>');
  process.exit();
}

// grab the url
const url = argv[2];

// make a GET request to the url
request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    console.log('code:', response.statusCode); // Print status code
  }
});
