#!/usr/bin/node

try {
	let filepath = process.argv[2];
	let filecontent = process.argv[3];

	const file = require('fs');

	file.writeFile(filepath, filecontent, (err) => {
		if (err) {
			console.error(err);
		}
	});

} catch {
	console.log("Missing a parameter")
}
