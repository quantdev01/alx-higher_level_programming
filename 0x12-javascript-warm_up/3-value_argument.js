#!/usr/bin/node
const myArgs = process.argv;

let i = 1;

while (myArgs[i] != null) {
  i++;
}

if (i === 2) { console.log('No argument'); } else { console.log(myArgs[2]); }
