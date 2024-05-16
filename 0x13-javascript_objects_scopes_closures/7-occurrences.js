#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let [i, j] = [0, 0];

  while (i < list.length) {
    if (list[i] === searchElement && typeof (list[i]) === typeof (searchElement)) {
      j++;
    }
    i++;
  }
  return j;
};
