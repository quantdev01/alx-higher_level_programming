#!/usr/bin/node

const myArg = process.argv;

function factorial(n)
{
	if (isNaN(n))
	{
		return 1;
	}
	else
		return n * factorial(n - 1);
}

console.log(factorial(Number(myArg[2])));
console.log(Number(myArg[2]));
