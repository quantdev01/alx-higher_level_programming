#!/usr/bin/node

const array = require('./100-data');

const myarray = array.list;

console.log(myarray);

let n = 0;

const map1 = myarray.map((x) => n++ * x);

console.log(map1);
