#!/usr/bin/node

const myArgs = process.argv;

if (myArgs.length === 2)
	console.log('Missing number of occurrences')
else
{
	i = 0;
	while (i < myArgs[2])
	{
		console.log('C is fun');
		i++;
	}
}
