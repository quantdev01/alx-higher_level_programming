#!/usr/bin/node

const myArgs = process.argv;

if (myArgs.length === 2)
{
	console.log('Missing size');
}
else if (typeof(myArgs[2]) === String)
	console.log('Not a number');
else
{
	let i = 0;
	let j = 0;
	let num = Number(myArgs[2]);

	if (num !== NaN)
	{
		console.log('The type is ' + typeof(num));
		console.log('The conteng is ' + num);
		while (i < num)
		{
			j = 0;
			while (j < num)
			{
				process.stdout.write('X');
				j++;
			}
			console.log('');
			i++;
		}
	}
	else
		console.log('Not a number from inside');

}
