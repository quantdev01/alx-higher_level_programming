#!/usr/bin/node

const myArgs = process.argv;

function add (a, b) {
  return a + b;
}

const sum = add(Number(myArgs[2]), Number(myArgs[3]));

console.log(sum);
