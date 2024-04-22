#!/usr/bin/node

const myArgs = process.argv;

if (myArgs.length === 2)
	console.log('Not a number');
else
{
	if (Number(myArgs[2]) == NaN)
		console.log('Not a number');
	else
		console.log(Number(myArgs[2]));
}
