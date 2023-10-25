#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2]; // Get the file path from cmd line args

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Handle the error by printing the error object
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
