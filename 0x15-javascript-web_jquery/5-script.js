#!/usr/bin/node
// add a <li> element to a list when the user clicks on the tag DIV#add_item
// added element is <li>Item</li> and added to UL.my_list

$(document).ready(function () {
  $('div#add_item').on('click', function () {
    $('<li>Item</li>').appendTo($('ul.my_list'));
  });
});
