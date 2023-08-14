#!/usr/bin/node

/* if first arg exists and is a number */
if (process.argv[2] && !isNaN(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  /* print each row */
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      /* print each char */
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
