#!/usr/bin/node

const args = process.argv;

if (args.length < 3 || args[2].trim() === '' || isNaN(Number(args[2]))) {
  console.log('Missing size');
} else {
  let i = args[2];
  const size = i;
  while (i > 0) {
    console.log(`${'X'.repeat(size)}`);
    i--;
  }
}
