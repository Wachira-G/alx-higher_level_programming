#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  if (typeof theFunction === 'function') {
    number++;
    theFunction(number);
  }
};
