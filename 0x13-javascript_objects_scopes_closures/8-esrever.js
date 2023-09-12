#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (const item of list) {
    newList.unshift(item);
  }
  return newList;
};
