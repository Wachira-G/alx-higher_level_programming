#!/usr/bin/node
// Updates the text color of the <header> element to red #FF0000

$(document).ready(function () {
  const $element = $('header');

  $element.css('color', '#FF0000');
});
