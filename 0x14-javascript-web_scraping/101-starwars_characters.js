#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2]; // Get the movie ID from the cmd line args

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characterURLs = movie.characters;

    // Iterate through the character URLs and make additional requests
    const characters = [];
    let characterCounter = 0;

    characterURLs.forEach((characterURL, index) => {
      request.get(characterURL, (error, response, characterBody) => {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(characterBody);
          characters[index] = character.name;
          characterCounter++;

          if (characterCounter === characterURLs.length) {
            // All characters retrieved, now print them in correct order
            characters.forEach((characterName) => {
              console.log(characterName);
            });
          }
        }
      });
    });
  }
});
