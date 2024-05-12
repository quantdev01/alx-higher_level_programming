#!/usr/bin/node

exports.esrever = function (list) {
	let len = list.length;
	let i = len;
	let j = 0;

	let new_list = list;

	while (i >= 0){
		new_list[j] = list[i];
		i--;
		j++;
	}

	return new_list;
}
