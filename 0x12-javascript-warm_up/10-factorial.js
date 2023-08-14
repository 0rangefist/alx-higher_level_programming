#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  }

  return num * factorial(num - 1);
}

if (process.argv[2] && !isNaN(process.argv[2])) {
  console.log(factorial(parseInt(process.argv[2])));
} else {
  console.log('1');
}
