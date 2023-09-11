#!/usr/bin/node

const args = process.argv.slice(2);

function secondBiggest (arr) {
  const size = arr.length;

  if (size < 2) {
    return 0;
  }

  const newArr = Array.from(new Set(arr)); // remove duplicates
  const newArrSize = newArr.length;
  const index = [newArrSize - 2];

  if (index < 0) {
    return newArr.sort()[0];
  } else {
    return newArr.sort()[index];
  }
}

console.log(secondBiggest(args));
