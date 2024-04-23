#!/usr/bin/node

const myArgs = process.argv;

function add(a, b)
{
	return a + b;
}

let sum = add(myArgs[2], myArgs[3]);

console.log(sum);
