#!/usr/bin/node

exports.logMe = function (item)
{
	let logTime = 0;
	return function () {
		return `${logTime++}: ${item}`;
	}
}
