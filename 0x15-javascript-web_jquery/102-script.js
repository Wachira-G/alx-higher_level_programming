#!/usr/bin/node
// fetches and prints how to say “Hello” depending on the language
// You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation must be fetched when the user clicks on INPUT#btn_translate
// The translation of “Hello” must be displayed in the HTML tag DIV#hello
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API
// You script must work when imported from the <head> tag

$(document).ready(function () {
  const translateBtn = $('input#btn_translate');
  const languageInput = $('input#language_code');
  const helloDiv = $('DIV#hello');

  translateBtn.on('click', function () {
    const languageCode = languageInput.val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

    $.ajax({
      url: apiUrl,
      data: { lang: languageCode },
      success: function (response) {
        helloDiv.text(response.hello);
      },
      error: function (xhr, status, error) {
        console.error(error);
      }
    });
  });
});
