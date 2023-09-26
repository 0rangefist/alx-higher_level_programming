#!/usr/bin/node

const fs = require('fs');

const argc = process.argv.length;
const argv = process.argv;

if (argc < 4) {
  console.log('Usage: ./0-readme.js <file_path> <your_content');
  process.exit();
}

// grab the file path
const filePath = argv[2];
const content = argv[3];

// attempt to write content to path
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err); // print error to standard error
  }
});
