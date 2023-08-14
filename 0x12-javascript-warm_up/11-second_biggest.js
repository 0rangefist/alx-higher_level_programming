#!/usr/bin/node

function findSecondBiggestInt (integers) {
  if (integers.length === 0 || integers.length === 1) {
    return 0;
  }

  /*  sort the array and return last but one */
  integers.sort((a, b) => a - b); // Sort in ascending order

  return integers[integers.length - 2]; // Return second-to-last element
}

/* pass a subarray of args list to the function */
console.log(findSecondBiggestInt(process.argv.slice(2)));
