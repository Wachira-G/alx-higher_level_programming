#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const arr = list.filter(number => number === searchElement);
  return arr.length;
};
