#!/usr/bin/node

const args = process.argv.slice(2);

function secondBiggest (arr) {
  if (arr.length < 2) {
    return 0;
  }

  const size = arr.length;

  return arr.sort()[size - 2];
}

console.log(secondBiggest(args));
