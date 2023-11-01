#!/usr/bin/node
// toggle the class of the <header> element when the user clicks
// on the tag DIV#red_header
// if current class is red, when user click , class must be updated to green
// and reverse

$(document).ready(function () {
  $('header').on('click', function () {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      $('header').addClass('green');
    } else {
      $('header').removeClass('green');
      $('header').addClass('red');
    }
  });
});
