#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  const newKey = dict[key];
  /* if 1st time ecountering newKey */
  if (newDict[newKey] === undefined) {
    /* create an empty array and
    assign it as value to newKey
    */
    newDict[newKey] = [];
  }
  newDict[newKey].push(key);
}

console.log(newDict);
