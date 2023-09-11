#!/usr/bin/node

const args = process.argv;

if (args.length < 3 || args[2].trim() === '' || isNaN(Number(args[2]))) {
  console.log('Missing number of occurrences');
} else {
  let i = args[2];
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
