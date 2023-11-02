#!/usr/bin/node
//  fetches and lists the title for all movies
// URL: https://swapi-api.alx-tools.com/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (films) {
      $.each(films.results, function (i, film) {
        $('ul#list_movies').append('<li>' + film.title + '</li>');
      });
    },
    error: function (xhr, status, error) {
      console.error(error);
    }
  });
});
