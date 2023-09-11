#!/usr/bin/node

const args = process.argv;
const a = Number(args[2]);
const b = Number(args[3]);

function add (a, b) {
  const sum = a + b;
  return sum;
}

console.log(add(a, b));
