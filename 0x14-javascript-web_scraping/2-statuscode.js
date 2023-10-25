#!/usr/bin/node

const request = require('request');
const url = process.argv[2]; // Get the URL from cmd line args

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
