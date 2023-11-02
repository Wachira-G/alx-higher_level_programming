#!/usr/bin/node
// fetches the character name
// from URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character

$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (character) {
      $('div#character').text(character.name);
    },
    error: function (xhr, status, error) {
      console.error(error);
    }
  });
});
