#!/usr/bin/node
// fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello in the HTML tag DIV#hello.
// The translation of “hello” must be displayed in the HTML tag DIV#hello
// Your script must work when it is imported from the <head> tag

$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (hello) {
      $('div#hello').text(hello.hello);
    },
    error: function (xhr, status, error) {
      console.error(error);
    }
  });
});
