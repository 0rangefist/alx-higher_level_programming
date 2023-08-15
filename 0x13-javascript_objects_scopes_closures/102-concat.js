#!/usr/bin/node

const fs = require('fs');

/* if destination path exists, then src paths do too */
if (process.argv[4]) {
  const srcPath1 = process.argv[2];
  const srcPath2 = process.argv[3];
  const destPath = process.argv[4];

  /* read file 1 and 2 */
  const srcContent1 = fs.readFileSync(srcPath1);
  const srcContent2 = fs.readFileSync(srcPath2);

  /* merge/concat content 1 and 2  */
  const destContent = srcContent1 + srcContent2;

  /* write dest content to dest path */
  fs.writeFileSync(destPath, destContent);
}
