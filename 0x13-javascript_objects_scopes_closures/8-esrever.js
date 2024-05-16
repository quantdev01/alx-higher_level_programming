#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  let i = len - 1;
  let j = 0;

  const newList = [];

  while (i >= 0) {
    newList[j] = list[i];
    i--;
    j++;
  }
  return newList;
};
