#!/usr/bin/node
// update the text color of the <header> element to red #FF0000
// when the user clicks on the tag DIV#red_header

$(document).ready(function () {
  const $element = $('div#red_header');

  $element.on('click', function () {
    $('header').css('color', '#FF0000');
  });
});
