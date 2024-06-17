#!/usr/bin/node

try {
  const filepath = process.argv[2];
  const filecontent = process.argv[3];

  const file = require('fs');

  file.writeFile(filepath, filecontent, (err) => {
    if (err) {
      console.error(err);
    }
  });
} catch {
  console.log('Missing a parameter');
}
