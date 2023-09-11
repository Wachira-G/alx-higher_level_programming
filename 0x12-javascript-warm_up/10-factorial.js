#!/usr/bin/node

let num = Number(process.argv[2]);

if (isNaN(num)) {
  num = 1;
}

function factorial (num) {
  let flag = 1;
  if (num === 0) {
    return 1;
  }

  if (num < 0) {
    flag = -1;
    num = Math.abs(num);
  }

  return flag * num * factorial(num - 1);
}

console.log(factorial(num));
