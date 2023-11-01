#!/usr/bin/node
// adds the class red to the <header> element when the user clicks
// on the tag DIV#red_header

$(document).ready(function () {
  const $element = $('div#red_header');

  $element.on('click', function () {
    $('header').addClass('red');
  });
});
