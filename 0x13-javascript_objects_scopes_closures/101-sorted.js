#!/usr/bin/node

const dict = require('./101-data');

let mydict = dict.dict;

let newdict = {}

const keys = Object.keys(mydict);
keys.forEach(key => {
	console.log(`${key}: ${dictionary[key]}`);
});
