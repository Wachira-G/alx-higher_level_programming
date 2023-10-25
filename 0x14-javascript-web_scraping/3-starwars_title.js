#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2]; // Get the movie ID from the cmd line args

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
