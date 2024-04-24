#!/usr/bin/node

const myArgs = process.argv;

let ln = myArgs.length;

if (ln <= 3)
	console.log(0);
else
{
	function getBiggest(myarray)
	{
		let i = 2;
		let n = 0;
		
		while (i <= ln)
		{
			if (myarray[i] > myarray[i+1])
			{
				let temp = myArgs[i];
				myarray[i] = myarray[i+1];
				myarray[i+1] = temp; 
			}
			i++;
		}
		console.log(myarray[myarray.length - 1]);
		return myarray[ln - 1];
	}

	getBiggest(myArgs);

	myArgs[getBiggest(myArgs)] = 0;

	console.log(myArgs);

	getBiggest(myArgs);
}
