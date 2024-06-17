#!/usr/bin/node

try {
  const filename = process.argv[2];

  const fs = require('fs');

  fs.readFile(filename, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
} catch {
  console.log('Error : no file added');
}
