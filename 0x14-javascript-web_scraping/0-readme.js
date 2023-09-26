#!/usr/bin/node

const fs = require('fs');

const argc = process.argv.length;
const argv = process.argv;

if (argc < 3) {
  console.log('Usage: ./0-readme.js <file_path>');
}

// grab the file path
const filePath = argv[2];

// attempt to read the file from path
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // print error to standard error
  } else {
    console.log(data); // print file to standard out
  }
});
