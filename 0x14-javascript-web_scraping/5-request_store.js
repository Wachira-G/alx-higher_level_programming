#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // Get the URL from the cmd line args
const filePath = process.argv[3]; // Get the file path from the cmd line args

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Write the response to the specified file with UTF-8 encoding
    fs.writeFileSync(filePath, body, 'utf-8');
    // console.log('File has been saved successfully.');
  }
});
