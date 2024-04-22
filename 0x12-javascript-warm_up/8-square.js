#!/usr/bin/node

const myArgs = process.argv;

if (myArgs.length === 2)
{
	console.log('Missing size');
}
else if (typeof(myArgs[2]) === String)
	console.log('Not a numbe');
else
{
	let i = 0;
	let j = 0;
	while (i < myArgs[2])
	{
		j = 0;
		while (j < myArgs[2])
		{
			process.stdout.write('X');
			j++;
		}
		console.log('');
		i++;
	}

}
