#!/usr/bin/node

const args = process.argv.slice(2);

function secondBiggest (arr) {
  const size = arr.length;

  if (size < 2) {
    return 0;
  }

  const newArr = Array.from(new Set(arr.map(Number)));// - duplicates
  newArr.sort();
  console.log(arr);
  console.log(newArr);
  const newArrSize = newArr.length;
  const index = [newArrSize - 2];

  if (index < 0) {
    return newArr[0];
  } else {
    return newArr[index];
  }
}

console.log(secondBiggest(args));
