#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2]; // Get the movie ID from the command line arguments

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characterURLs = movie.characters;

    // Iterate through the character URLs and make additional requests
    characterURLs.forEach((characterURL) => {
      request.get(characterURL, (error, response, characterBody) => {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(characterBody);
          console.log(character.name);
        }
      });
    });
  }
});
