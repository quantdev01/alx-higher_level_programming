#!/usr/bin/node

const myArgs = process.argv;

if (myArgs.length === 2 || isNaN(myArgs[2])) {
  console.log('Missing size');
} else {
  let i = 0;
  let j = 0;
  const num = Number(myArgs[2]);

  while (i < num) {
    j = 0;
    while (j < num) {
      process.stdout.write('X');
      j++;
    }
    console.log('');
    i++;
  }
}
