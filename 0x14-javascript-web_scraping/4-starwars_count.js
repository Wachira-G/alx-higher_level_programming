#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2]; // Get the API URL from the cmd line args

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeAntillesFilms = films.filter((film) => {
      return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    });

    console.log(wedgeAntillesFilms.length);
  }
});
