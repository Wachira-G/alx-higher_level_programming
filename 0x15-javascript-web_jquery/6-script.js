#!/usr/bin/node
// updates the text of the <header> element to New Header!!!
// when the user clicks on DIV#update_header

$(document).ready(function () {
  $('div#update_header').on('click', function () {
    const newText = 'New Header!!!';
    $('header').text(newText);
  });
});
