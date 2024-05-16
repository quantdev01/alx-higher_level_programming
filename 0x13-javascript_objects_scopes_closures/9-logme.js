#!/usr/bin/node

let logTime = 0;

exports.logMe = function (item) {
  console.log(`${logTime++}: ${item}`);
};
