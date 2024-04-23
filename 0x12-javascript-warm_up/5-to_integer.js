#!/usr/bin/node

const myArgs = process.argv;

if (myArgs.length === 2 || isNaN(Number(myArgs[2]))) { console.log('Not a number'); } else {
  console.log('My number: ' + Number(myArgs[2]));
}
