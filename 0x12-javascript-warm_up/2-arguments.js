#!/usr/bin/node

/* if only first arg exists  */
if (process.argv[2] && !process.argv[3]) {
  console.log('Argument found');
  /* if 2 or more args exists  */
} else if (process.argv[3]) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
