#!/usr/bin/node

const request = require('request');

const argc = process.argv.length;
const argv = process.argv;

if (argc < 3) {
  console.log('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit();
}

// Grab the URL and file path
const url = argv[2];

// Initialize an empty object for usersWithCompletedTasks
const usersWithCompletedTasks = {};

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error(error || `code: ${response.statusCode}`);
  } else {
    const todos = JSON.parse(body);

    for (const todo of todos) {
      if (todo.completed) {
        if (!(todo.userId in usersWithCompletedTasks)) {
          // userId property doesnt already exist, so initialize it
          usersWithCompletedTasks[todo.userId] = 0;
        }
        usersWithCompletedTasks[todo.userId]++;
      }
    }
    // print the usersWithCompletedTasks object
    console.log(usersWithCompletedTasks);
  }
});
