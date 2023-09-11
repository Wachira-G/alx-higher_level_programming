#!/usr/bin/node

const args = process.argv;
const arg1 = args[2];
const invalidResponse = 'Not a number';
const validResponse = `My number: ${Math.floor(Number(arg1))}`;

if (args.length < 3 || isNaN(Number(arg1)) || arg1.trim() === '') {
  console.log(invalidResponse);
} else {
  console.log(validResponse);
}
