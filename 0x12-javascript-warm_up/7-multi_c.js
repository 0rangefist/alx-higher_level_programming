#!/usr/bin/node

/* if first arg exists and is a number */
if (process.argv[2] && !isNaN(process.argv[2])) {
  /* print the statement up to the provided number of times */
  for (let i = 0; i < parseInt([process.argv[2]]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
