#!/usr/bin/node

function add (a, b) {
  return a + b;
}

let arg1;
let arg2;
/* if the first arg exists and is a number  */
if (process.argv[2] && !isNaN(process.argv[2])) {
  arg1 = parseInt(process.argv[2]);
}

/* if the second arg exists and is a number  */
if (process.argv[3] && !isNaN(process.argv[3])) {
  arg2 = parseInt(process.argv[3]);
}

console.log(add(arg1, arg2));
