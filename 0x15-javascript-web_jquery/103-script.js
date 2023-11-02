#!/usr/bin/node
// Fetches and prints how to say “Hello” depending on the language
// using this API service: https://www.fourtonfish.com/hellosalut/hello/
// Language code will be the value entered
//    in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation is fetched when the user clicks on INPUT#btn_translate
//    OR presses ENTER when the focus is on INPUT#language_code
// The translation of “Hello” is displayed in the HTML tag DIV#hello
// can’t use document.querySelector
// use the JQuery API
// Script should work when imported from the <head> tag

$(document).ready(function () {
  let isINputFocused = false;

  function fetchTranslation () {
    const languageCode = $('#language_code').val();

    if (isINputFocused && languageCode.trim() !== '') {
      const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

      $.ajax({
        url: apiUrl,
        success: function (response) {
          $('#hello').text(response.hello);
        },
        error: function (xhr, status, error) {
          $('#hello').text('Translation not found');
        }
      });
    }
  }

  // event handlers
  $('input#btn_translate').on('click', function () {
    fetchTranslation();
  });

  $('input#language_code').on('keydown', function (event) {
    if (isINputFocused && event.key === 'Enter') {
      fetchTranslation();
    }
  });

  $('input#language_code').on('focus', function () {
    isINputFocused = true;
  });

  $('input#language_code').on('blur', function () {
    isINputFocused = false;
  });
});
